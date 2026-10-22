"""Strict and lax validation: rules of the spec, responses that do not match it."""

import logging
import pickle
from collections.abc import Mapping
from decimal import Decimal
from typing import Annotated, Literal

import httpx2
import pytest
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter, ValidationError

from hetzner_api import (
    NOT_GIVEN,
    RequestValidationError,
    ResponseValidationError,
    RetryPolicy,
    UnknownValue,
)
from hetzner_api._base_client import SyncTransport
from hetzner_api._validation import STRICT, Check, ValueType, is_strict, lenient, parse_payload

type Kind = Literal["a", "b"]


class _Model(BaseModel):
    model_config = ConfigDict(frozen=True, strict=True, extra="ignore")


class Child(_Model):
    name: Annotated[str, Check(max_length=3)]


class Cat(_Model):
    type: Literal["cat"]
    lives: int


class Dog(_Model):
    type: Literal["dog"]
    bark: str


type Pet = Annotated[Cat | Dog, Field(discriminator="type")]


class Parent(_Model):
    id: Annotated[int, Check(minimum=1)]
    label: str = Field(alias="label-name")
    child: Child | None = None
    children: tuple[Child, ...] = ()
    tags: Mapping[str, Child] | None = None
    pair: tuple[int, str] | None = None
    pet: Pet | None = None
    kind: Kind | UnknownValue | None = None


def _transport(validation: Literal["lax", "strict"], payload: object) -> SyncTransport:
    def handler(_: httpx2.Request) -> httpx2.Response:
        return httpx2.Response(200, json=payload)

    return SyncTransport(
        credentials={},
        base_urls={"main": "https://api.example.test"},
        default_server="main",
        retry=RetryPolicy(max_retries=0),
        timeout=5.0,
        http_client=httpx2.Client(transport=httpx2.MockTransport(handler)),
        validation=validation,
    )


def _constructed(model: type[BaseModel], **values: object) -> BaseModel:
    """A model holding what does not fit its types (as lax mode builds it)."""
    return model.model_construct(None, **values)


def _parse(validation: Literal["lax", "strict"], payload: object) -> Parent:
    transport = _transport(validation, payload)
    return transport.parse(Parent, transport.request("GET", "/x"))


# --- Rules ------------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("check", "value", "problem"),
    [
        (Check(min_length=2), "a", "shorter than 2 characters"),
        (Check(max_length=2), "abc", "longer than 2 characters"),
        (Check(pattern="^[a-z]+$"), "A1", "does not match '^[a-z]+$'"),
        (Check(minimum=1), 0, "0 is less than 1"),
        (Check(maximum=1.5), 2, "2 is greater than 1.5"),
        (Check(exclusive_minimum=0), 0, "0 is not greater than 0"),
        (Check(exclusive_maximum=10), Decimal(10), "10 is not less than 10"),
        (Check(multiple_of=0.25), 0.3, "0.3 is not a multiple of 0.25"),
        (Check(min_items=1), [], "fewer than 1 entries"),
        (Check(max_items=1), (1, 2), "more than 1 entries"),
        (Check(unique_items=True), [{"a": 1}, {"a": 1}], "entries are not unique"),
        (Check(items=Check(minimum=0)), [1, -1], "[1]: -1 is less than 0"),
        (Check(min_properties=1), {}, "fewer than 1 entries"),
        (Check(max_properties=0), {"a": 1}, "more than 0 entries"),
        (Check(keys=Check(max_length=1)), {"ab": 1}, "['ab']: longer than 1 characters (key)"),
        (Check(values=Check(maximum=0)), {"a": 1}, "['a']: 1 is greater than 0"),
        (
            Check(fields=(("name", Check(min_length=1)),)),
            {"name": ""},
            ".name: shorter than 1 characters",
        ),
        (
            Check(fields_of=lambda: Check(fields=(("name", Check(min_length=1)),))),
            {"name": ""},
            ".name: shorter than 1 characters",
        ),
    ],
)
def test_check_reports_broken_rules(check: Check, value: object, problem: str) -> None:
    assert check.problems(value, "") == [problem]
    assert check.problems(value, "arg") == [
        f"arg{problem}" if problem[0] in "[." else f"arg: {problem}"
    ]


@pytest.mark.parametrize(
    "value",
    [None, True, "ab", 1, 1.0, 0.5, [1], {"a": 1}, b"bytes", object()],
)
def test_check_accepts_what_keeps_the_rules(value: object) -> None:
    check = Check(
        max_length=2,
        pattern="^a",
        minimum=0,
        maximum=1,
        multiple_of=0.5,
        max_items=1,
        unique_items=True,
        items=Check(minimum=0),
        max_properties=1,
        keys=Check(max_length=1),
        values=Check(minimum=0),
        fields=(("missing", Check(minimum=5)),),
    )
    assert check.problems(value, "x") == []


def test_strict_context() -> None:
    assert is_strict(STRICT)
    assert not is_strict(None)
    assert not is_strict({"validation": "lax"})


# --- Responses ---------------------------------------------------------------------------

VALID: dict[str, object] = {
    "id": 1,
    "label-name": "x",
    "child": {"name": "abc"},
    "children": [{"name": "a"}],
    "tags": {"t": {"name": "b"}},
    "pair": [1, "a"],
    "pet": {"type": "cat", "lives": 7},
    "kind": "new",
}


@pytest.mark.parametrize("validation", ["lax", "strict"])
def test_valid_response_is_validated_in_both_modes(validation: Literal["lax", "strict"]) -> None:
    parsed = _parse(validation, VALID)
    assert parsed.child == Child(name="abc")
    assert parsed.pet == Cat(type="cat", lives=7)
    assert isinstance(parsed.kind, UnknownValue)


def test_broken_rules_count_in_strict_mode_only() -> None:
    broken = {**VALID, "id": 0, "child": {"name": "abcd"}}
    assert _parse("lax", broken).id == 0
    with pytest.raises(ResponseValidationError) as raised:
        _parse("strict", broken)
    assert [error["msg"] for error in raised.value.errors] == [
        "0 is less than 1",
        "longer than 3 characters",
    ]


def test_lax_mode_keeps_what_does_not_match(caplog: pytest.LogCaptureFixture) -> None:
    broken: dict[str, object] = {
        "id": "one",
        "child": {"name": None},
        "children": [{"name": "a"}, {"name": 5}],
        "tags": {"t": {}},
        "pair": [1, 2],
        "pet": {"type": "dog", "bark": 3},
    }
    with caplog.at_level(logging.WARNING, logger="hetzner_api"):
        parsed = _parse("lax", broken)
    assert "the response does not match the spec" in caplog.text
    assert "(and " in caplog.text  # more than three problems
    # The values the types promise do not hold - that is the price of lax mode
    kept: dict[str, object] = dict(parsed)
    assert kept["id"] == "one"
    assert kept["label"] is None  # required, but missing
    assert kept["child"] == _constructed(Child, name=None)
    assert parsed.children[0] == Child(name="a")
    assert parsed.children[1] == _constructed(Child, name=5)
    assert kept["tags"] == {"t": _constructed(Child, name=None)}
    assert kept["pair"] == (1, 2)
    assert kept["pet"] == _constructed(Dog, type="dog", bark=3)
    assert parsed.kind is None  # optional and missing
    with pytest.raises(ResponseValidationError):
        _parse("strict", broken)


@pytest.mark.parametrize("content", [b"not json", b"[1, 2]"])
def test_lax_mode_rejects_what_is_no_object(content: bytes) -> None:
    def handler(_: httpx2.Request) -> httpx2.Response:
        return httpx2.Response(200, content=content)

    transport = SyncTransport(
        credentials={},
        base_urls={"main": "https://api.example.test"},
        default_server="main",
        retry=RetryPolicy(max_retries=0),
        timeout=5.0,
        http_client=httpx2.Client(transport=httpx2.MockTransport(handler)),
    )
    with pytest.raises(ResponseValidationError):
        transport.parse(Parent, transport.request("GET", "/x"))


def test_values_that_are_no_model() -> None:
    value_type = ValueType(
        TypeAdapter(tuple[int, ...], config=ConfigDict(strict=True)), tuple[int, ...]
    )
    lax = _transport("lax", [1, "a"])
    kept: object = lax.parse_value(value_type, lax.request("GET", "/x"))
    assert kept == (1, "a")
    strict = _transport("strict", [1, "a"])
    with pytest.raises(ResponseValidationError):
        strict.parse_value(value_type, strict.request("GET", "/x"))
    assert strict.parse_value(value_type, _transport("strict", [1]).request("GET", "/x")) == (1,)


@pytest.mark.parametrize(
    ("annotation", "value", "expected"),
    [
        (tuple[int, str], [1], [1]),  # wrong length: kept
        (Pet, {"type": "fish"}, {"type": "fish"}),  # no variant fits
        (Pet, "cat", "cat"),
        (Kind | UnknownValue, 7, 7),
        (Cat | Dog, {"type": "cat", "lives": "many"}, _constructed(Cat, type="cat", lives="many")),
        (int | None, None, None),
        (str, 5, 5),
        (Annotated[list[int], {"unhashable": True}], ["a"], ["a"]),
    ],
)
def test_lenient(annotation: object, value: object, expected: object) -> None:
    assert lenient(annotation, value) == expected


# --- Requests ----------------------------------------------------------------------------

CHECKS: Mapping[str, Check] = {"name": Check(max_length=3), "count": Check(minimum=1)}


def test_arguments_are_checked_in_strict_mode_only() -> None:
    _transport("lax", {}).validate(CHECKS, name="long", count=0)
    strict = _transport("strict", {})
    strict.validate(CHECKS, name="abc", count=1)
    with pytest.raises(RequestValidationError) as raised:
        strict.validate(CHECKS, name="long", count=0)
    assert raised.value.problems == ("name: longer than 3 characters", "count: 0 is less than 1")
    assert isinstance(raised.value, ValueError)
    restored = pickle.loads(pickle.dumps(raised.value))  # noqa: S301 - our own data
    assert restored.problems == raised.value.problems


def test_arguments_not_given_are_not_checked() -> None:
    _transport("strict", {}).validate(CHECKS, name=NOT_GIVEN, count=None)


def test_numbers_are_compared_exactly() -> None:
    assert Check(maximum=9223372036854775807).problems(9223372036854775807, "") == []
    assert Check(maximum=10).problems(10**400, "") == [f"{10**400} is greater than 10"]
    assert Check(multiple_of=2).problems(2_000_000_001, "") == ["2000000001 is not a multiple of 2"]
    assert Check(multiple_of=0.1).problems(0.3, "") == []
    assert Check(multiple_of=0.01).problems(Decimal("9.99"), "") == []


def test_patterns_mean_what_json_schema_says() -> None:
    assert Check(pattern="^[a-z]+$").problems("abc\n", "") != []  # $ ends the text
    assert Check(pattern="^\\d+$").problems("١٢", "") != []  # \d is ASCII
    assert Check(pattern="^[$]+$").problems("$$", "") == []
    assert Check(pattern="^a\\$$").problems("a$", "") == []


def test_unique_items_compare_like_json() -> None:
    check = Check(unique_items=True)
    assert check.problems([1, 1.0], "") == ["entries are not unique"]
    assert check.problems([{"a": 1, "b": 2}, {"b": 2, "a": 1}], "") == ["entries are not unique"]
    assert check.problems([True, 1, None, "1", [1], {"a": [1]}, b"x", object(), object()], "") == []


def test_payloads_are_validated_like_responses(caplog: pytest.LogCaptureFixture) -> None:
    value_type = ValueType(TypeAdapter(Child), Child)
    assert parse_payload(value_type, b'{"name": "abc"}', "strict") == Child(name="abc")
    with pytest.raises(ValidationError):
        parse_payload(value_type, b'{"name": "abcd"}', "strict")  # breaks maxLength
    with caplog.at_level(logging.WARNING, logger="hetzner_api"):
        kept: object = parse_payload(value_type, b'{"name": 5}', "lax")
    assert kept == _constructed(Child, name=5)
    assert "does not match the spec" in caplog.text
    with pytest.raises(ValidationError):
        parse_payload(value_type, b"no json", "lax")

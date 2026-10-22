"""How strictly the client holds the API to its spec.

``validation="lax"`` (the default) keeps the client working when the API and its spec disagree -
which happens in practice:

- rules of the spec (``maxLength``, ``pattern``, ``minimum`` …) are not checked;
- a response that does not match the spec (a missing field, ``null`` where none is allowed, a
  wrong type) is still returned: everything that fits is validated as usual, the rest is kept as
  the API sent it. A warning is logged, since the types of those values do not hold.

``validation="strict"`` is for checking that an API delivers exactly what its spec promises:

- arguments that break a rule raise :class:`~hetzner_api.errors.RequestValidationError`
  before anything is sent;
- responses that break a rule or do not match the spec raise
  :class:`~hetzner_api.errors.ResponseValidationError`.
"""

import logging
import re
import types
import typing
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from decimal import Decimal
from functools import cache
from typing import Final, Literal, TypeAliasType, cast, final

import pydantic_core
from pydantic import BaseModel, GetCoreSchemaHandler, TypeAdapter, ValidationError, ValidationInfo
from pydantic_core import CoreSchema, PydanticCustomError, core_schema

__all__ = [
    "STRICT",
    "Check",
    "Validation",
    "ValueType",
    "is_strict",
    "lenient",
    "parse_payload",
]

type Validation = Literal["lax", "strict"]
"""``"lax"``: get along with what the API sends; ``"strict"``: hold it to the spec."""

STRICT: Final[Mapping[str, object]] = {"validation": "strict"}
"""Validation context of strict mode (``model_validate_json(..., context=STRICT)``)."""

_LOG: Final = logging.getLogger("hetzner_api")


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Check:
    """Rules of the spec for one value (JSON Schema keywords), checked in strict mode only.

    As metadata of a response field (``Annotated[str, Check(max_length=63)]``) pydantic applies
    them; request arguments are checked by the transport. ``items``, ``values`` and ``keys`` hold
    the rules for the entries of lists and maps, ``fields`` those of the keys of an object (or
    ``fields_of`` a model's, from :mod:`hetzner_api.rules`).
    """

    min_length: int | None = None
    max_length: int | None = None
    pattern: str | None = None
    minimum: float | None = None
    maximum: float | None = None
    exclusive_minimum: float | None = None
    exclusive_maximum: float | None = None
    multiple_of: float | None = None
    min_items: int | None = None
    max_items: int | None = None
    unique_items: bool = False
    min_properties: int | None = None
    max_properties: int | None = None
    items: Check | None = None
    values: Check | None = None
    keys: Check | None = None
    fields: tuple[tuple[str, Check], ...] = ()
    fields_of: Callable[[], Check] | None = None
    """The rules of the fields of an object model, looked up when checking (models may contain
    each other)."""

    def problems(self, value: object, where: str) -> list[str]:
        """What is wrong with ``value`` (empty: nothing); ``where`` names it in the messages."""
        if value is None or isinstance(value, bool):
            return []
        if isinstance(value, str):
            return self._text(value, where)
        if isinstance(value, (int, float, Decimal)):
            return self._number(value, where)
        if isinstance(value, Mapping):
            return self._object(cast("Mapping[object, object]", value), where)
        if isinstance(value, Sequence) and not isinstance(value, (bytes, bytearray)):
            return self._list(cast("Sequence[object]", value), where)
        return []

    def _text(self, value: str, where: str) -> list[str]:
        found: list[str] = []
        if self.min_length is not None and len(value) < self.min_length:
            found.append(_at(where, f"shorter than {self.min_length} characters"))
        if self.max_length is not None and len(value) > self.max_length:
            found.append(_at(where, f"longer than {self.max_length} characters"))
        if self.pattern is not None and _compiled(self.pattern).search(value) is None:
            found.append(_at(where, f"does not match {self.pattern!r}"))
        return found

    def _number(self, value: float | Decimal, where: str) -> list[str]:
        # Compared as they are: int and Decimal stay exact (no detour through float)
        found: list[str] = []
        if self.minimum is not None and value < self.minimum:
            found.append(_at(where, f"{value} is less than {self.minimum}"))
        if self.maximum is not None and value > self.maximum:
            found.append(_at(where, f"{value} is greater than {self.maximum}"))
        if self.exclusive_minimum is not None and value <= self.exclusive_minimum:
            found.append(_at(where, f"{value} is not greater than {self.exclusive_minimum}"))
        if self.exclusive_maximum is not None and value >= self.exclusive_maximum:
            found.append(_at(where, f"{value} is not less than {self.exclusive_maximum}"))
        if self.multiple_of is not None and not _is_multiple(value, self.multiple_of):
            found.append(_at(where, f"{value} is not a multiple of {self.multiple_of}"))
        return found

    def _list(self, value: Sequence[object], where: str) -> list[str]:
        found: list[str] = []
        if self.min_items is not None and len(value) < self.min_items:
            found.append(_at(where, f"fewer than {self.min_items} entries"))
        if self.max_items is not None and len(value) > self.max_items:
            found.append(_at(where, f"more than {self.max_items} entries"))
        if self.unique_items and len({_comparable(entry) for entry in value}) < len(value):
            found.append(_at(where, "entries are not unique"))
        if self.items is not None:
            for index, entry in enumerate(value):
                found.extend(self.items.problems(entry, f"{where}[{index}]"))
        return found

    def _object(self, value: Mapping[object, object], where: str) -> list[str]:
        found: list[str] = []
        if self.min_properties is not None and len(value) < self.min_properties:
            found.append(_at(where, f"fewer than {self.min_properties} entries"))
        if self.max_properties is not None and len(value) > self.max_properties:
            found.append(_at(where, f"more than {self.max_properties} entries"))
        for key, entry in value.items():
            if self.keys is not None:
                found.extend(
                    f"{problem} (key)" for problem in self.keys.problems(key, f"{where}[{key!r}]")
                )
            if self.values is not None:
                found.extend(self.values.problems(entry, f"{where}[{key!r}]"))
        for key, check in self.fields:
            if key in value:
                found.extend(check.problems(value[key], f"{where}.{key}"))
        if self.fields_of is not None:
            found.extend(self.fields_of().problems(value, where))
        return found

    def __get_pydantic_core_schema__(
        self,
        source_type: object,
        handler: GetCoreSchemaHandler,
    ) -> CoreSchema:
        """Pydantic: check the validated value - in strict mode only."""
        return core_schema.with_info_after_validator_function(self._validate, handler(source_type))

    def _validate(self, value: object, info: ValidationInfo) -> object:
        if is_strict(info.context):
            problems = self.problems(value, "")
            if problems:
                kind, template = "spec_rule", "{problems}"
                raise PydanticCustomError(kind, template, {"problems": "; ".join(problems)})
        return value


def is_strict(context: object) -> bool:
    """Is ``context`` the validation context of strict mode?"""
    if not isinstance(context, Mapping):
        return False
    return cast("Mapping[object, object]", context).get("validation") == "strict"


def _at(where: str, problem: str) -> str:
    return f"{where}: {problem}" if where else problem


@cache
def _compiled(pattern: str) -> re.Pattern[str]:
    r"""``pattern`` with the meaning JSON Schema gives it (ECMAScript, not Python).

    ``$`` ends the text (in Python it also matches before a final newline), ``\d`` and ``\w``
    are ASCII only.
    """
    return re.compile(_ecma(pattern), re.ASCII)


def _ecma(pattern: str) -> str:
    r"""Replaces ``$`` outside of character classes by ``\Z``."""
    translated: list[str] = []
    escaped = in_class = False
    for char in pattern:
        if escaped:
            escaped = False
        elif char == "\\":
            escaped = True
        elif char == "[":
            in_class = True
        elif char == "]":
            in_class = False
        elif char == "$" and not in_class:
            translated.append("\\Z")
            continue
        translated.append(char)
    return "".join(translated)


def _is_multiple(number: float | Decimal, of: float) -> bool:
    """Exact in decimal: ``0.3`` is no multiple of ``0.25``, ``2_000_000_001`` none of ``2``."""
    return _decimal(number) % _decimal(of) == 0


def _decimal(number: float | Decimal) -> Decimal:
    return number if isinstance(number, Decimal) else Decimal(repr(number))


def _comparable(value: object) -> object:
    """``value`` as something hashable that is equal where JSON Schema says so (``uniqueItems``).

    ``1`` and ``1.0`` are the same number, objects do not depend on the order of their keys,
    ``true`` is no ``1``.
    """
    if isinstance(value, bool) or value is None or isinstance(value, str):
        return (type(value).__name__, value)
    if isinstance(value, (int, float, Decimal)):
        return ("number", _decimal(value).normalize())
    if isinstance(value, Mapping):
        entries = cast("Mapping[object, object]", value).items()
        return ("object", frozenset((key, _comparable(entry)) for key, entry in entries))
    if isinstance(value, Sequence) and not isinstance(value, (bytes, bytearray)):
        return ("array", tuple(_comparable(entry) for entry in cast("Sequence[object]", value)))
    return ("other", repr(value))


@final
@dataclass(frozen=True, slots=True)
class ValueType[T]:
    """A response that is no object model (list, union, scalar): its adapter and its type."""

    adapter: TypeAdapter[T]
    annotation: object


def parse_payload[T](value_type: ValueType[T], body: bytes | str, validation: Validation) -> T:
    """A JSON body the API sent (a webhook), validated like a response.

    Raises:
        ValidationError: ``validation="strict"`` and the body does not match the spec - or the
            body is no JSON at all.
    """
    context = STRICT if validation == "strict" else None
    try:
        return value_type.adapter.validate_json(body, context=context)
    except ValidationError as error:
        if validation == "strict":
            raise
        try:
            data = pydantic_core.from_json(body)
        except ValueError:
            raise error from None
        _LOG.warning(
            "a payload does not match the spec, kept as sent: %d problems", error.error_count()
        )
        return cast("T", lenient(value_type.annotation, data))


def lenient(annotation: object, value: object) -> object:
    """``value`` as ``annotation`` as far as it fits; what does not fit stays as it was sent.

    Lax mode only, after the strict validation failed: objects become their models field by field
    (a missing required field becomes ``None``), lists and maps entry by entry.
    """
    try:
        return _adapter(annotation).validate_json(pydantic_core.to_json(value))
    except ValidationError:
        pass
    target = _unaliased(annotation)
    model = _model_class(target)
    if model is not None and isinstance(value, dict):
        return _model(model, cast("dict[str, object]", value))
    return _container(target, value)


def _container(target: object, value: object) -> object:
    """Tuples, maps and unions entry by entry (see :func:`lenient`)."""
    origin = typing.get_origin(target)
    arguments = cast("tuple[object, ...]", typing.get_args(target))
    if origin is tuple and isinstance(value, list):
        return _tuple(arguments, cast("list[object]", value))
    if origin is Mapping and isinstance(value, dict):
        mapping = cast("dict[str, object]", value)
        return {key: lenient(arguments[1], entry) for key, entry in mapping.items()}
    if origin is types.UnionType:
        return _variant(arguments, value)
    return value


def _tuple(arguments: tuple[object, ...], entries: list[object]) -> object:
    if len(arguments) == 2 and arguments[1] is Ellipsis:  # noqa: PLR2004 - tuple[X, ...]
        return tuple(lenient(arguments[0], entry) for entry in entries)
    if len(arguments) == len(entries):
        return tuple(lenient(kind, entry) for kind, entry in zip(arguments, entries, strict=True))
    return entries


def _adapter(annotation: object) -> TypeAdapter[object]:
    try:
        return _cached_adapter(annotation)
    except TypeError:  # not hashable (Annotated with unhashable metadata)
        return TypeAdapter[object](cast("type[object]", annotation))


@cache
def _cached_adapter(annotation: object) -> TypeAdapter[object]:
    return TypeAdapter[object](cast("type[object]", annotation))


def _unaliased(annotation: object) -> object:
    """Without ``type`` aliases and ``Annotated`` (rules and discriminators do not matter here)."""
    while True:
        if isinstance(annotation, TypeAliasType):
            annotation = cast("object", annotation.__value__)
        elif typing.get_origin(annotation) is typing.Annotated:
            annotation = cast("object", typing.get_args(annotation)[0])
        else:
            return annotation


def _model_class(target: object) -> type[BaseModel] | None:
    if isinstance(target, type) and issubclass(target, BaseModel):
        return target
    return None


def _model(model: type[BaseModel], data: dict[str, object]) -> BaseModel:
    values: dict[str, object] = {}
    for name, info in model.model_fields.items():
        key = info.alias or name
        if key in data:
            annotation = cast("object", info.annotation)
            if info.metadata:
                annotation = typing.Annotated[annotation, *info.metadata]
            values[name] = lenient(annotation, data[key])
        elif info.is_required():
            values[name] = None
    return model.model_construct(None, **values)


def _variant(variants: tuple[object, ...], value: object) -> object:
    """``X | None`` as ``X``; of several models the one whose literal fields match ``value``."""
    others = [variant for variant in variants if variant is not types.NoneType]
    if len(others) == 1:
        return lenient(others[0], value)
    if not isinstance(value, dict):
        return value
    data = cast("dict[str, object]", value)
    models = [model for model in map(_model_class, map(_unaliased, others)) if model is not None]
    fitting = [model for model in models if _literals_match(model, data)]
    return _model(fitting[0], data) if len(fitting) == 1 else data


def _literals_match(model: type[BaseModel], data: dict[str, object]) -> bool:
    for name, info in model.model_fields.items():
        annotation = _unaliased(info.annotation)
        if typing.get_origin(annotation) is Literal:
            allowed = cast("tuple[object, ...]", typing.get_args(annotation))
            if data.get(info.alias or name) not in allowed:
                return False
    return True

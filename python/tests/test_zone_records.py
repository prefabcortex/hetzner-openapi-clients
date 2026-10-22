"""Hand-written helpers for zone records (``hetzner_api.zone_records``)."""

import pytest

from hetzner_api.zone_records import format_txt_record, is_quoted


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("", '""'),
        ("hello world", '"hello world"'),
        ('say "hi"', '"say \\"hi\\""'),
        ("back\\slash", '"back\\\\slash"'),
    ],
)
def test_short_values_become_one_quoted_string(value: str, expected: str) -> None:
    assert format_txt_record(value) == expected


def test_long_values_are_split_into_strings_of_255_bytes() -> None:
    value = "k" * 600
    assert format_txt_record(value) == f'"{"k" * 255}" "{"k" * 255}" "{"k" * 90}"'


def test_characters_are_never_cut_in_two() -> None:
    value = "ü" * 200  # 2 bytes each: byte 255 would be the second half of a character
    parts = format_txt_record(value).split(" ")
    assert [len(part.strip('"').encode()) for part in parts] == [254, 146]
    assert "".join(part.strip('"') for part in parts) == value


def test_escaping_does_not_count_towards_the_limit() -> None:
    value = '"' * 255
    assert format_txt_record(value) == '"' + '\\"' * 255 + '"'


@pytest.mark.parametrize(
    ("value", "quoted"),
    [('"a"', True), ('"a" "b"', True), ("a", False), ('"', False), ('"a', False)],
)
def test_is_quoted(value: str, quoted: bool) -> None:  # noqa: FBT001 - parameter
    assert is_quoted(value) is quoted

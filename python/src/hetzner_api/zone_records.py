"""Values of DNS records in zones (written by hand - not in the spec, kept on regeneration).

A TXT record holds one or more quoted *character-strings* of at most 255 bytes each
(RFC 1035). Long values such as DKIM keys have to be split, quotes and backslashes escaped::

    from hetzner_api.zone_records import format_txt_record

    record = {"value": format_txt_record(dkim_key)}
    client.zone_rrsets.create_zone_rrset(zone, name="mail._domainkey", type="TXT", records=[record])
"""

from collections.abc import Iterator
from typing import Final

__all__ = ["format_txt_record", "is_quoted"]

_MAX_BYTES: Final = 255  # one character-string (RFC 1035, section 3.3)
# A UTF-8 continuation byte is 10xxxxxx: the top two bits under the mask are 10
_CONTINUATION_MASK: Final = 0b1100_0000
_CONTINUATION: Final = 0b1000_0000


def format_txt_record(value: str) -> str:
    r"""The value of a TXT record as the API expects it.

    Split into quoted strings of at most 255 bytes - never inside a character - with ``"`` and
    ``\`` escaped::

        >>> format_txt_record('v=spf1 include:"mail" -all')
        '"v=spf1 include:\\"mail\\" -all"'
        >>> format_txt_record("")
        '""'
    """
    return " ".join(f'"{_escaped(chunk)}"' for chunk in _chunks(value)) or '""'


def is_quoted(value: str) -> bool:
    """Is ``value`` already written as quoted strings (``"a" "b"``)?"""
    return len(value) >= 2 and value.startswith('"') and value.endswith('"')  # noqa: PLR2004 - two quotes


def _chunks(value: str) -> Iterator[str]:
    data = value.encode()
    start = 0
    while start < len(data):
        end = min(start + _MAX_BYTES, len(data))
        # Never cut a character in two: step back over continuation bytes
        while end < len(data) and data[end] & _CONTINUATION_MASK == _CONTINUATION:
            end -= 1
        yield data[start:end].decode()
        start = end


def _escaped(chunk: str) -> str:
    return chunk.replace("\\", "\\\\").replace('"', '\\"')

"""Helper types shared by all modules of the client."""

from typing import Final, Literal, final, override

from pydantic import GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema

__all__ = ["NOT_GIVEN", "NotGiven", "StrSequence", "UnknownValue"]

type StrSequence = list[str] | tuple[str, ...]
"""A list of strings as an argument. Deliberately not ``Sequence[str]``, which accepts ``"abc"``."""


@final
class NotGiven:
    """Marks an argument that was not passed.

    ``None`` means "send JSON ``null``", ``NOT_GIVEN`` means "leave the field out".
    """

    __slots__ = ()

    def __bool__(self) -> Literal[False]:
        return False

    @override
    def __repr__(self) -> str:
        return "NOT_GIVEN"


NOT_GIVEN: Final = NotGiven()
"""Default of optional body arguments: the field is not sent."""


@final
class UnknownValue(str):
    """An enum value the spec does not know (yet).

    The API may introduce new values (e.g. a new server status). Instead of rejecting the whole
    response, such a value arrives as ``UnknownValue`` - a ``str`` you can compare and print,
    whose type makes it visible that it is unknown::

        match server.status:
            case "running": ...
            case UnknownValue(): ...
    """

    __slots__ = ()

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        source_type: object,
        handler: GetCoreSchemaHandler,
    ) -> CoreSchema:
        """Pydantic: accept any string and store it as ``UnknownValue``."""
        _ = (source_type, handler)
        return core_schema.no_info_after_validator_function(
            cls,
            core_schema.str_schema(strict=True),
        )

    @override
    def __repr__(self) -> str:
        return f"UnknownValue({str.__repr__(self)})"

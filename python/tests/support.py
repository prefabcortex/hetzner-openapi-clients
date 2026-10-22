"""Test helpers: a recording mock transport and client factories."""

import json
from collections.abc import Mapping, Sequence
from typing import Final, Self

import httpx2
import pydantic_core
from pydantic import BaseModel, JsonValue, TypeAdapter

from hetzner_api import AsyncHetzner, Hetzner, RetryPolicy

NO_RETRY: Final = RetryPolicy(max_retries=0)
_JSON: Final[TypeAdapter[JsonValue]] = TypeAdapter(JsonValue)


class Recorder:
    """Answers with prepared responses in order and records every request."""

    def __init__(
        self,
        status: int,
        payload: JsonValue | bytes = None,
        *,
        headers: Mapping[str, str] | None = None,
    ) -> None:
        """``payload``: JSON, or ``bytes`` sent as they are (a file)."""
        self.responses: list[tuple[int, JsonValue | bytes, Mapping[str, str]]] = [
            (status, payload, headers or {})
        ]
        self.requests: list[httpx2.Request] = []

    @classmethod
    def sequence(cls, responses: Sequence[tuple[int, JsonValue | bytes]]) -> Self:
        """Several responses in order (the last one repeats)."""
        recorder = cls(*responses[0])
        recorder.responses.extend((status, payload, {}) for status, payload in responses[1:])
        return recorder

    def __call__(self, request: httpx2.Request) -> httpx2.Response:
        index = min(len(self.requests), len(self.responses) - 1)
        self.requests.append(request)
        status, payload, headers = self.responses[index]
        if payload is None:
            return httpx2.Response(status, headers=headers)
        if isinstance(payload, bytes):
            return httpx2.Response(status, content=payload, headers=headers)
        return httpx2.Response(status, json=payload, headers=headers)

    def only(self) -> httpx2.Request:
        """The only recorded request."""
        assert len(self.requests) == 1, self.requests
        return self.requests[0]


def sync_client(recorder: Recorder, *, retry: RetryPolicy = NO_RETRY) -> Hetzner:
    """Synchronous client that only talks to ``recorder``."""
    http_client = httpx2.Client(transport=httpx2.MockTransport(recorder))
    return Hetzner(token="test-token", http_client=http_client, retry=retry)


def async_client(recorder: Recorder, *, retry: RetryPolicy = NO_RETRY) -> AsyncHetzner:
    """Asynchronous client that only talks to ``recorder``."""
    http_client = httpx2.AsyncClient(transport=httpx2.MockTransport(recorder))
    return AsyncHetzner(token="test-token", http_client=http_client, retry=retry)


def json_of(request: httpx2.Request) -> JsonValue:
    """JSON body of a request."""
    return _JSON.validate_json(request.content)


def to_jsonable(value: object) -> JsonValue:
    """Serialize Python values the way the client does (datetime, Decimal ...)."""
    return _JSON.validate_json(pydantic_core.to_json(value))


def validated[M: BaseModel](model: type[M], payload: JsonValue) -> M:
    """Validate ``payload`` like a real response."""
    return model.model_validate_json(json.dumps(payload))


def validated_value[T](adapter: TypeAdapter[T], payload: JsonValue) -> T:
    """Validate ``payload`` like a real response that is not an object model."""
    return adapter.validate_json(json.dumps(payload))


def with_status(payload: JsonValue, key: str, status: str) -> JsonValue:
    """Copy of ``payload`` with ``payload[key]["status"] = status``."""
    assert isinstance(payload, dict)
    inner = payload[key]
    assert isinstance(inner, dict)
    return {**payload, key: {**inner, "status": status}}

"""Generated tests for ``server_types``."""

import asyncio

from hetzner_api.models import GetServerTypeResponse, ListServerTypesResponse
from tests.payloads import GET_SERVER_TYPE_RESPONSE, LIST_SERVER_TYPES_RESPONSE
from tests.support import Recorder, async_client, sync_client, validated


def test_server_types_list_server_types() -> None:
    recorder = Recorder(200, LIST_SERVER_TYPES_RESPONSE)
    with sync_client(recorder) as client:
        result = client.server_types.list_server_types()
        assert result == validated(ListServerTypesResponse, LIST_SERVER_TYPES_RESPONSE)
        assert hash(result) == hash(validated(ListServerTypesResponse, LIST_SERVER_TYPES_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/server_types"


def test_async_server_types_list_server_types() -> None:
    recorder = Recorder(200, LIST_SERVER_TYPES_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_types.list_server_types()
            assert result == validated(ListServerTypesResponse, LIST_SERVER_TYPES_RESPONSE)
            assert hash(result) == hash(
                validated(ListServerTypesResponse, LIST_SERVER_TYPES_RESPONSE)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/server_types"


def test_server_types_get_server_type() -> None:
    recorder = Recorder(200, GET_SERVER_TYPE_RESPONSE)
    with sync_client(recorder) as client:
        result = client.server_types.get_server_type(42)
        assert result == validated(GetServerTypeResponse, GET_SERVER_TYPE_RESPONSE)
        assert hash(result) == hash(validated(GetServerTypeResponse, GET_SERVER_TYPE_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/server_types/42"


def test_async_server_types_get_server_type() -> None:
    recorder = Recorder(200, GET_SERVER_TYPE_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_types.get_server_type(42)
            assert result == validated(GetServerTypeResponse, GET_SERVER_TYPE_RESPONSE)
            assert hash(result) == hash(validated(GetServerTypeResponse, GET_SERVER_TYPE_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/server_types/42"

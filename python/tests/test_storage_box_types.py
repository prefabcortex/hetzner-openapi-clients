"""Generated tests for ``storage_box_types``."""

import asyncio

from hetzner_api.models import GetStorageBoxTypeResponse, ListStorageBoxTypesResponse
from tests.payloads import GET_STORAGE_BOX_TYPE_RESPONSE, LIST_STORAGE_BOX_TYPES_RESPONSE
from tests.support import Recorder, async_client, sync_client, validated


def test_storage_box_types_list_storage_box_types() -> None:
    recorder = Recorder(200, LIST_STORAGE_BOX_TYPES_RESPONSE)
    with sync_client(recorder) as client:
        result = client.storage_box_types.list_storage_box_types()
        assert result == validated(ListStorageBoxTypesResponse, LIST_STORAGE_BOX_TYPES_RESPONSE)
        assert hash(result) == hash(
            validated(ListStorageBoxTypesResponse, LIST_STORAGE_BOX_TYPES_RESPONSE)
        )
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_box_types"


def test_async_storage_box_types_list_storage_box_types() -> None:
    recorder = Recorder(200, LIST_STORAGE_BOX_TYPES_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_box_types.list_storage_box_types()
            assert result == validated(ListStorageBoxTypesResponse, LIST_STORAGE_BOX_TYPES_RESPONSE)
            assert hash(result) == hash(
                validated(ListStorageBoxTypesResponse, LIST_STORAGE_BOX_TYPES_RESPONSE)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_box_types"


def test_storage_box_types_get_storage_box_type() -> None:
    recorder = Recorder(200, GET_STORAGE_BOX_TYPE_RESPONSE)
    with sync_client(recorder) as client:
        result = client.storage_box_types.get_storage_box_type(42)
        assert result == validated(GetStorageBoxTypeResponse, GET_STORAGE_BOX_TYPE_RESPONSE)
        assert hash(result) == hash(
            validated(GetStorageBoxTypeResponse, GET_STORAGE_BOX_TYPE_RESPONSE)
        )
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_box_types/42"


def test_async_storage_box_types_get_storage_box_type() -> None:
    recorder = Recorder(200, GET_STORAGE_BOX_TYPE_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_box_types.get_storage_box_type(42)
            assert result == validated(GetStorageBoxTypeResponse, GET_STORAGE_BOX_TYPE_RESPONSE)
            assert hash(result) == hash(
                validated(GetStorageBoxTypeResponse, GET_STORAGE_BOX_TYPE_RESPONSE)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_box_types/42"

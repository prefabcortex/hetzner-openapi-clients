"""Generated tests for ``storage_boxes``."""

import asyncio

from hetzner_api.models import (
    ActionResponse,
    CreateStorageBoxResponse,
    ListStorageBoxesResponse,
    ListStorageBoxFoldersResponse,
    StorageBoxResponse,
)
from tests.payloads import (
    ACTION_RESPONSE,
    CREATE_STORAGE_BOX_RESPONSE,
    LIST_STORAGE_BOX_FOLDERS_RESPONSE,
    LIST_STORAGE_BOXES_RESPONSE,
    STORAGE_BOX_RESPONSE,
)
from tests.support import Recorder, async_client, json_of, sync_client, to_jsonable, validated


def test_storage_boxes_list_storage_boxes() -> None:
    recorder = Recorder(200, LIST_STORAGE_BOXES_RESPONSE)
    with sync_client(recorder) as client:
        result = client.storage_boxes.list_storage_boxes()
        assert result == validated(ListStorageBoxesResponse, LIST_STORAGE_BOXES_RESPONSE)
        assert hash(result) == hash(
            validated(ListStorageBoxesResponse, LIST_STORAGE_BOXES_RESPONSE)
        )
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes"


def test_async_storage_boxes_list_storage_boxes() -> None:
    recorder = Recorder(200, LIST_STORAGE_BOXES_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_boxes.list_storage_boxes()
            assert result == validated(ListStorageBoxesResponse, LIST_STORAGE_BOXES_RESPONSE)
            assert hash(result) == hash(
                validated(ListStorageBoxesResponse, LIST_STORAGE_BOXES_RESPONSE)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes"


def test_storage_boxes_create_storage_box() -> None:
    recorder = Recorder(200, CREATE_STORAGE_BOX_RESPONSE)
    with sync_client(recorder) as client:
        result = client.storage_boxes.create_storage_box(
            name="example", location="fsn1", storage_box_type="bx20", password="example"
        )
        assert result == validated(CreateStorageBoxResponse, CREATE_STORAGE_BOX_RESPONSE)
        assert hash(result) == hash(
            validated(CreateStorageBoxResponse, CREATE_STORAGE_BOX_RESPONSE)
        )
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes"
    assert json_of(request) == to_jsonable(
        {"name": "example", "location": "fsn1", "storage_box_type": "bx20", "password": "example"}
    )


def test_async_storage_boxes_create_storage_box() -> None:
    recorder = Recorder(200, CREATE_STORAGE_BOX_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_boxes.create_storage_box(
                name="example", location="fsn1", storage_box_type="bx20", password="example"
            )
            assert result == validated(CreateStorageBoxResponse, CREATE_STORAGE_BOX_RESPONSE)
            assert hash(result) == hash(
                validated(CreateStorageBoxResponse, CREATE_STORAGE_BOX_RESPONSE)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes"
    assert json_of(request) == to_jsonable(
        {"name": "example", "location": "fsn1", "storage_box_type": "bx20", "password": "example"}
    )


def test_storage_boxes_get_storage_box() -> None:
    recorder = Recorder(200, STORAGE_BOX_RESPONSE)
    with sync_client(recorder) as client:
        result = client.storage_boxes.get_storage_box(42)
        assert result == validated(StorageBoxResponse, STORAGE_BOX_RESPONSE)
        assert hash(result) == hash(validated(StorageBoxResponse, STORAGE_BOX_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42"


def test_async_storage_boxes_get_storage_box() -> None:
    recorder = Recorder(200, STORAGE_BOX_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_boxes.get_storage_box(42)
            assert result == validated(StorageBoxResponse, STORAGE_BOX_RESPONSE)
            assert hash(result) == hash(validated(StorageBoxResponse, STORAGE_BOX_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42"


def test_storage_boxes_update_storage_box() -> None:
    recorder = Recorder(200, STORAGE_BOX_RESPONSE)
    with sync_client(recorder) as client:
        result = client.storage_boxes.update_storage_box(42)
        assert result == validated(StorageBoxResponse, STORAGE_BOX_RESPONSE)
        assert hash(result) == hash(validated(StorageBoxResponse, STORAGE_BOX_RESPONSE))
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_async_storage_boxes_update_storage_box() -> None:
    recorder = Recorder(200, STORAGE_BOX_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_boxes.update_storage_box(42)
            assert result == validated(StorageBoxResponse, STORAGE_BOX_RESPONSE)
            assert hash(result) == hash(validated(StorageBoxResponse, STORAGE_BOX_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_storage_boxes_delete_storage_box() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.storage_boxes.delete_storage_box(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42"


def test_async_storage_boxes_delete_storage_box() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_boxes.delete_storage_box(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42"


def test_storage_boxes_list_storage_box_folders() -> None:
    recorder = Recorder(200, LIST_STORAGE_BOX_FOLDERS_RESPONSE)
    with sync_client(recorder) as client:
        result = client.storage_boxes.list_storage_box_folders(42)
        assert result == validated(ListStorageBoxFoldersResponse, LIST_STORAGE_BOX_FOLDERS_RESPONSE)
        assert hash(result) == hash(
            validated(ListStorageBoxFoldersResponse, LIST_STORAGE_BOX_FOLDERS_RESPONSE)
        )
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/folders"


def test_async_storage_boxes_list_storage_box_folders() -> None:
    recorder = Recorder(200, LIST_STORAGE_BOX_FOLDERS_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_boxes.list_storage_box_folders(42)
            assert result == validated(
                ListStorageBoxFoldersResponse, LIST_STORAGE_BOX_FOLDERS_RESPONSE
            )
            assert hash(result) == hash(
                validated(ListStorageBoxFoldersResponse, LIST_STORAGE_BOX_FOLDERS_RESPONSE)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/folders"

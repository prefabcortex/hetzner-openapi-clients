"""Generated tests for ``storage_box_subaccounts``."""

import asyncio

from hetzner_api.models import (
    ActionResponse,
    CreateStorageBoxSubaccountResponse,
    ListStorageBoxSubaccountsResponse,
    SubaccountResponse,
)
from tests.payloads import (
    ACTION_RESPONSE,
    CREATE_STORAGE_BOX_SUBACCOUNT_RESPONSE,
    LIST_STORAGE_BOX_SUBACCOUNTS_RESPONSE,
    SUBACCOUNT_RESPONSE,
)
from tests.support import Recorder, async_client, json_of, sync_client, to_jsonable, validated


def test_storage_box_subaccounts_list_storage_box_subaccounts() -> None:
    recorder = Recorder(200, LIST_STORAGE_BOX_SUBACCOUNTS_RESPONSE)
    with sync_client(recorder) as client:
        result = client.storage_box_subaccounts.list_storage_box_subaccounts(42)
        assert result == validated(
            ListStorageBoxSubaccountsResponse, LIST_STORAGE_BOX_SUBACCOUNTS_RESPONSE
        )
        assert hash(result) == hash(
            validated(ListStorageBoxSubaccountsResponse, LIST_STORAGE_BOX_SUBACCOUNTS_RESPONSE)
        )
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/subaccounts"


def test_async_storage_box_subaccounts_list_storage_box_subaccounts() -> None:
    recorder = Recorder(200, LIST_STORAGE_BOX_SUBACCOUNTS_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_box_subaccounts.list_storage_box_subaccounts(42)
            assert result == validated(
                ListStorageBoxSubaccountsResponse, LIST_STORAGE_BOX_SUBACCOUNTS_RESPONSE
            )
            assert hash(result) == hash(
                validated(ListStorageBoxSubaccountsResponse, LIST_STORAGE_BOX_SUBACCOUNTS_RESPONSE)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/subaccounts"


def test_storage_box_subaccounts_create_storage_box_subaccount() -> None:
    recorder = Recorder(200, CREATE_STORAGE_BOX_SUBACCOUNT_RESPONSE)
    with sync_client(recorder) as client:
        result = client.storage_box_subaccounts.create_storage_box_subaccount(
            42, home_directory="my-backup/server01", password="example"
        )
        assert result == validated(
            CreateStorageBoxSubaccountResponse, CREATE_STORAGE_BOX_SUBACCOUNT_RESPONSE
        )
        assert hash(result) == hash(
            validated(CreateStorageBoxSubaccountResponse, CREATE_STORAGE_BOX_SUBACCOUNT_RESPONSE)
        )
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/subaccounts"
    assert json_of(request) == to_jsonable(
        {"home_directory": "my-backup/server01", "password": "example"}
    )


def test_async_storage_box_subaccounts_create_storage_box_subaccount() -> None:
    recorder = Recorder(200, CREATE_STORAGE_BOX_SUBACCOUNT_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_box_subaccounts.create_storage_box_subaccount(
                42, home_directory="my-backup/server01", password="example"
            )
            assert result == validated(
                CreateStorageBoxSubaccountResponse, CREATE_STORAGE_BOX_SUBACCOUNT_RESPONSE
            )
            assert hash(result) == hash(
                validated(
                    CreateStorageBoxSubaccountResponse, CREATE_STORAGE_BOX_SUBACCOUNT_RESPONSE
                )
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/subaccounts"
    assert json_of(request) == to_jsonable(
        {"home_directory": "my-backup/server01", "password": "example"}
    )


def test_storage_box_subaccounts_get_storage_box_subaccount() -> None:
    recorder = Recorder(200, SUBACCOUNT_RESPONSE)
    with sync_client(recorder) as client:
        result = client.storage_box_subaccounts.get_storage_box_subaccount(42, 42)
        assert result == validated(SubaccountResponse, SUBACCOUNT_RESPONSE)
        assert hash(result) == hash(validated(SubaccountResponse, SUBACCOUNT_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/subaccounts/42"


def test_async_storage_box_subaccounts_get_storage_box_subaccount() -> None:
    recorder = Recorder(200, SUBACCOUNT_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_box_subaccounts.get_storage_box_subaccount(42, 42)
            assert result == validated(SubaccountResponse, SUBACCOUNT_RESPONSE)
            assert hash(result) == hash(validated(SubaccountResponse, SUBACCOUNT_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/subaccounts/42"


def test_storage_box_subaccounts_update_storage_box_subaccount() -> None:
    recorder = Recorder(200, SUBACCOUNT_RESPONSE)
    with sync_client(recorder) as client:
        result = client.storage_box_subaccounts.update_storage_box_subaccount(42, 42)
        assert result == validated(SubaccountResponse, SUBACCOUNT_RESPONSE)
        assert hash(result) == hash(validated(SubaccountResponse, SUBACCOUNT_RESPONSE))
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/subaccounts/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_async_storage_box_subaccounts_update_storage_box_subaccount() -> None:
    recorder = Recorder(200, SUBACCOUNT_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_box_subaccounts.update_storage_box_subaccount(42, 42)
            assert result == validated(SubaccountResponse, SUBACCOUNT_RESPONSE)
            assert hash(result) == hash(validated(SubaccountResponse, SUBACCOUNT_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/subaccounts/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_storage_box_subaccounts_delete_storage_box_subaccount() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.storage_box_subaccounts.delete_storage_box_subaccount(42, 42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/subaccounts/42"


def test_async_storage_box_subaccounts_delete_storage_box_subaccount() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_box_subaccounts.delete_storage_box_subaccount(42, 42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/subaccounts/42"

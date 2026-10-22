"""Generated tests for ``storage_box_subaccount_actions``."""

import asyncio

from hetzner_api.models import ActionResponse
from tests.payloads import ACTION_RESPONSE
from tests.support import Recorder, async_client, json_of, sync_client, to_jsonable, validated


def test_storage_box_subaccount_actions_change_storage_box_subaccount_h_97b567b6() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        resource = client.storage_box_subaccount_actions
        result = resource.change_storage_box_subaccount_home_directory(
            42, 42, home_directory="my-backup/server01"
        )
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.com"
    assert (
        request.url.raw_path.split(b"?")[0]
        == b"/v1/storage_boxes/42/subaccounts/42/actions/change_home_directory"
    )
    assert json_of(request) == to_jsonable({"home_directory": "my-backup/server01"})


def test_async_storage_box_subaccount_actions_change_storage_box_subaccount_h_97b567b6() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            resource = client.storage_box_subaccount_actions
            result = await resource.change_storage_box_subaccount_home_directory(
                42, 42, home_directory="my-backup/server01"
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.com"
    assert (
        request.url.raw_path.split(b"?")[0]
        == b"/v1/storage_boxes/42/subaccounts/42/actions/change_home_directory"
    )
    assert json_of(request) == to_jsonable({"home_directory": "my-backup/server01"})


def test_storage_box_subaccount_actions_reset_storage_box_subaccount_password() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        resource = client.storage_box_subaccount_actions
        result = resource.reset_storage_box_subaccount_password(42, 42, password="example")
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.com"
    assert (
        request.url.raw_path.split(b"?")[0]
        == b"/v1/storage_boxes/42/subaccounts/42/actions/reset_subaccount_password"
    )
    assert json_of(request) == to_jsonable({"password": "example"})


def test_async_storage_box_subaccount_actions_reset_storage_box_subaccount_password() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            resource = client.storage_box_subaccount_actions
            result = await resource.reset_storage_box_subaccount_password(
                42, 42, password="example"
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.com"
    assert (
        request.url.raw_path.split(b"?")[0]
        == b"/v1/storage_boxes/42/subaccounts/42/actions/reset_subaccount_password"
    )
    assert json_of(request) == to_jsonable({"password": "example"})


def test_storage_box_subaccount_actions_update_storage_box_subaccount_a_1dc3d20e() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        resource = client.storage_box_subaccount_actions
        result = resource.update_storage_box_subaccount_access_settings(42, 42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.com"
    assert (
        request.url.raw_path.split(b"?")[0]
        == b"/v1/storage_boxes/42/subaccounts/42/actions/update_access_settings"
    )
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_async_storage_box_subaccount_actions_update_storage_box_subaccount_a_1dc3d20e() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            resource = client.storage_box_subaccount_actions
            result = await resource.update_storage_box_subaccount_access_settings(42, 42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.com"
    assert (
        request.url.raw_path.split(b"?")[0]
        == b"/v1/storage_boxes/42/subaccounts/42/actions/update_access_settings"
    )
    assert json_of(request) == to_jsonable(dict[str, object]())

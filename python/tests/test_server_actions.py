"""Generated tests for ``server_actions``."""

import asyncio

import pytest

from hetzner_api.models import (
    ActionListResponseWithMeta,
    ActionResponse,
    CreateServerImageResponse,
    RebuildServerResponse,
    RequestServerConsoleResponse,
    RootPasswordResponse,
)
from tests.payloads import (
    ACTION_LIST_RESPONSE_WITH_META,
    ACTION_RESPONSE,
    CREATE_SERVER_IMAGE_RESPONSE,
    REBUILD_SERVER_RESPONSE,
    REQUEST_SERVER_CONSOLE_RESPONSE,
    ROOT_PASSWORD_RESPONSE,
)
from tests.support import Recorder, async_client, json_of, sync_client, to_jsonable, validated


def test_server_actions_list_servers_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        result = client.server_actions.list_servers_actions()
        assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        assert hash(result) == hash(
            validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        )
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/actions"


def test_async_server_actions_list_servers_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_actions.list_servers_actions()
            assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            assert hash(result) == hash(
                validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/actions"


def test_server_actions_get_servers_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.server_actions.get_servers_action(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/actions/42"


def test_async_server_actions_get_servers_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_actions.get_servers_action(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/actions/42"


def test_server_actions_list_server_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        result = client.server_actions.list_server_actions(42)
        assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        assert hash(result) == hash(
            validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        )
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions"


def test_async_server_actions_list_server_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_actions.list_server_actions(42)
            assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            assert hash(result) == hash(
                validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions"


def test_server_actions_add_server_to_placement_group() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.server_actions.add_server_to_placement_group(42, placement_group=1)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/add_to_placement_group"
    assert json_of(request) == to_jsonable({"placement_group": 1})


def test_async_server_actions_add_server_to_placement_group() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_actions.add_server_to_placement_group(
                42, placement_group=1
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/add_to_placement_group"
    assert json_of(request) == to_jsonable({"placement_group": 1})


def test_server_actions_attach_server_iso() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.server_actions.attach_server_iso(42, iso="FreeBSD-11.0-RELEASE-amd64-dvd1")
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/attach_iso"
    assert json_of(request) == to_jsonable({"iso": "FreeBSD-11.0-RELEASE-amd64-dvd1"})


def test_async_server_actions_attach_server_iso() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_actions.attach_server_iso(
                42, iso="FreeBSD-11.0-RELEASE-amd64-dvd1"
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/attach_iso"
    assert json_of(request) == to_jsonable({"iso": "FreeBSD-11.0-RELEASE-amd64-dvd1"})


def test_server_actions_attach_server_to_network() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.server_actions.attach_server_to_network(42, network=4711)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/attach_to_network"
    assert json_of(request) == to_jsonable({"network": 4711})


def test_async_server_actions_attach_server_to_network() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_actions.attach_server_to_network(42, network=4711)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/attach_to_network"
    assert json_of(request) == to_jsonable({"network": 4711})


def test_server_actions_change_server_alias_ips() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.server_actions.change_server_alias_ips(
            42, network=4711, alias_ips=["10.0.1.2"]
        )
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/change_alias_ips"
    assert json_of(request) == to_jsonable({"network": 4711, "alias_ips": ["10.0.1.2"]})


def test_async_server_actions_change_server_alias_ips() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_actions.change_server_alias_ips(
                42, network=4711, alias_ips=["10.0.1.2"]
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/change_alias_ips"
    assert json_of(request) == to_jsonable({"network": 4711, "alias_ips": ["10.0.1.2"]})


def test_server_actions_change_server_dns_ptr() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.server_actions.change_server_dns_ptr(
            42, ip="2001:db8::1", dns_ptr="server.example.com"
        )
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/change_dns_ptr"
    assert json_of(request) == to_jsonable({"ip": "2001:db8::1", "dns_ptr": "server.example.com"})


def test_async_server_actions_change_server_dns_ptr() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_actions.change_server_dns_ptr(
                42, ip="2001:db8::1", dns_ptr="server.example.com"
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/change_dns_ptr"
    assert json_of(request) == to_jsonable({"ip": "2001:db8::1", "dns_ptr": "server.example.com"})


def test_server_actions_change_server_protection() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.server_actions.change_server_protection(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/change_protection"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_async_server_actions_change_server_protection() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_actions.change_server_protection(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/change_protection"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_server_actions_change_server_type() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.server_actions.change_server_type(
            42, upgrade_disk=True, server_type="cpx22"
        )
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/change_type"
    assert json_of(request) == to_jsonable({"upgrade_disk": True, "server_type": "cpx22"})


def test_async_server_actions_change_server_type() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_actions.change_server_type(
                42, upgrade_disk=True, server_type="cpx22"
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/change_type"
    assert json_of(request) == to_jsonable({"upgrade_disk": True, "server_type": "cpx22"})


def test_server_actions_create_server_image() -> None:
    recorder = Recorder(200, CREATE_SERVER_IMAGE_RESPONSE)
    with sync_client(recorder) as client:
        result = client.server_actions.create_server_image(42)
        assert result == validated(CreateServerImageResponse, CREATE_SERVER_IMAGE_RESPONSE)
        assert hash(result) == hash(
            validated(CreateServerImageResponse, CREATE_SERVER_IMAGE_RESPONSE)
        )
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/create_image"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_async_server_actions_create_server_image() -> None:
    recorder = Recorder(200, CREATE_SERVER_IMAGE_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_actions.create_server_image(42)
            assert result == validated(CreateServerImageResponse, CREATE_SERVER_IMAGE_RESPONSE)
            assert hash(result) == hash(
                validated(CreateServerImageResponse, CREATE_SERVER_IMAGE_RESPONSE)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/create_image"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_server_actions_detach_server_from_network() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.server_actions.detach_server_from_network(42, network=4711)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/detach_from_network"
    assert json_of(request) == to_jsonable({"network": 4711})


def test_async_server_actions_detach_server_from_network() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_actions.detach_server_from_network(42, network=4711)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/detach_from_network"
    assert json_of(request) == to_jsonable({"network": 4711})


def test_server_actions_detach_server_iso() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.server_actions.detach_server_iso(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/detach_iso"


def test_async_server_actions_detach_server_iso() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_actions.detach_server_iso(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/detach_iso"


def test_server_actions_disable_server_backup() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.server_actions.disable_server_backup(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/disable_backup"


def test_async_server_actions_disable_server_backup() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_actions.disable_server_backup(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/disable_backup"


def test_server_actions_disable_server_rescue() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.server_actions.disable_server_rescue(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/disable_rescue"


def test_async_server_actions_disable_server_rescue() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_actions.disable_server_rescue(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/disable_rescue"


def test_server_actions_enable_server_backup() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.server_actions.enable_server_backup(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/enable_backup"


def test_async_server_actions_enable_server_backup() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_actions.enable_server_backup(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/enable_backup"


def test_server_actions_enable_server_rescue() -> None:
    recorder = Recorder(200, ROOT_PASSWORD_RESPONSE)
    with sync_client(recorder) as client:
        result = client.server_actions.enable_server_rescue(42)
        assert result == validated(RootPasswordResponse, ROOT_PASSWORD_RESPONSE)
        assert hash(result) == hash(validated(RootPasswordResponse, ROOT_PASSWORD_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/enable_rescue"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_async_server_actions_enable_server_rescue() -> None:
    recorder = Recorder(200, ROOT_PASSWORD_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_actions.enable_server_rescue(42)
            assert result == validated(RootPasswordResponse, ROOT_PASSWORD_RESPONSE)
            assert hash(result) == hash(validated(RootPasswordResponse, ROOT_PASSWORD_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/enable_rescue"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_server_actions_poweroff_server() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.server_actions.poweroff_server(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/poweroff"


def test_async_server_actions_poweroff_server() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_actions.poweroff_server(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/poweroff"


def test_server_actions_poweron_server() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.server_actions.poweron_server(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/poweron"


def test_async_server_actions_poweron_server() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_actions.poweron_server(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/poweron"


def test_server_actions_reboot_server() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.server_actions.reboot_server(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/reboot"


def test_async_server_actions_reboot_server() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_actions.reboot_server(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/reboot"


def test_server_actions_rebuild_server() -> None:
    recorder = Recorder(200, REBUILD_SERVER_RESPONSE)
    with sync_client(recorder) as client:
        result = client.server_actions.rebuild_server(42, image="ubuntu-24.04")
        assert result == validated(RebuildServerResponse, REBUILD_SERVER_RESPONSE)
        assert hash(result) == hash(validated(RebuildServerResponse, REBUILD_SERVER_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/rebuild"
    assert json_of(request) == to_jsonable({"image": "ubuntu-24.04"})


def test_async_server_actions_rebuild_server() -> None:
    recorder = Recorder(200, REBUILD_SERVER_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_actions.rebuild_server(42, image="ubuntu-24.04")
            assert result == validated(RebuildServerResponse, REBUILD_SERVER_RESPONSE)
            assert hash(result) == hash(validated(RebuildServerResponse, REBUILD_SERVER_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/rebuild"
    assert json_of(request) == to_jsonable({"image": "ubuntu-24.04"})


def test_server_actions_remove_server_from_placement_group() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.server_actions.remove_server_from_placement_group(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert (
        request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/remove_from_placement_group"
    )


def test_async_server_actions_remove_server_from_placement_group() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_actions.remove_server_from_placement_group(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert (
        request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/remove_from_placement_group"
    )


def test_server_actions_request_server_console() -> None:
    recorder = Recorder(200, REQUEST_SERVER_CONSOLE_RESPONSE)
    with sync_client(recorder) as client:
        result = client.server_actions.request_server_console(42)
        assert result == validated(RequestServerConsoleResponse, REQUEST_SERVER_CONSOLE_RESPONSE)
        assert hash(result) == hash(
            validated(RequestServerConsoleResponse, REQUEST_SERVER_CONSOLE_RESPONSE)
        )
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/request_console"


def test_async_server_actions_request_server_console() -> None:
    recorder = Recorder(200, REQUEST_SERVER_CONSOLE_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_actions.request_server_console(42)
            assert result == validated(
                RequestServerConsoleResponse, REQUEST_SERVER_CONSOLE_RESPONSE
            )
            assert hash(result) == hash(
                validated(RequestServerConsoleResponse, REQUEST_SERVER_CONSOLE_RESPONSE)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/request_console"


def test_server_actions_reset_server() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.server_actions.reset_server(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/reset"


def test_async_server_actions_reset_server() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_actions.reset_server(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/reset"


def test_server_actions_reset_server_password() -> None:
    recorder = Recorder(200, ROOT_PASSWORD_RESPONSE)
    with sync_client(recorder) as client:
        result = client.server_actions.reset_server_password(42)
        assert result == validated(RootPasswordResponse, ROOT_PASSWORD_RESPONSE)
        assert hash(result) == hash(validated(RootPasswordResponse, ROOT_PASSWORD_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/reset_password"


def test_async_server_actions_reset_server_password() -> None:
    recorder = Recorder(200, ROOT_PASSWORD_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_actions.reset_server_password(42)
            assert result == validated(RootPasswordResponse, ROOT_PASSWORD_RESPONSE)
            assert hash(result) == hash(validated(RootPasswordResponse, ROOT_PASSWORD_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/reset_password"


def test_server_actions_shutdown_server() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.server_actions.shutdown_server(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/shutdown"


def test_async_server_actions_shutdown_server() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.server_actions.shutdown_server(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/shutdown"


def test_server_actions_get_server_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        deprecated_method = client.server_actions.get_server_action  # type: ignore[deprecated]  # pyright: ignore[reportDeprecated]
        with pytest.deprecated_call():
            result = deprecated_method(42, 42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/42"


def test_async_server_actions_get_server_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            deprecated_method = client.server_actions.get_server_action  # type: ignore[deprecated]  # pyright: ignore[reportDeprecated]
            with pytest.deprecated_call():
                result = await deprecated_method(42, 42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/actions/42"

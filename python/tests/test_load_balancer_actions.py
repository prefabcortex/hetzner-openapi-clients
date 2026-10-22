"""Generated tests for ``load_balancer_actions``."""

import asyncio

import pytest

from hetzner_api.models import ActionListResponseWithMeta, ActionResponse
from tests.payloads import ACTION_LIST_RESPONSE_WITH_META, ACTION_RESPONSE
from tests.support import Recorder, async_client, json_of, sync_client, to_jsonable, validated


def test_load_balancer_actions_list_load_balancers_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        result = client.load_balancer_actions.list_load_balancers_actions()
        assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        assert hash(result) == hash(
            validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        )
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/actions"


def test_async_load_balancer_actions_list_load_balancers_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.load_balancer_actions.list_load_balancers_actions()
            assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            assert hash(result) == hash(
                validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/actions"


def test_load_balancer_actions_get_load_balancers_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.load_balancer_actions.get_load_balancers_action(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/actions/42"


def test_async_load_balancer_actions_get_load_balancers_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.load_balancer_actions.get_load_balancers_action(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/actions/42"


def test_load_balancer_actions_list_load_balancer_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        result = client.load_balancer_actions.list_load_balancer_actions(42)
        assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        assert hash(result) == hash(
            validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        )
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/actions"


def test_async_load_balancer_actions_list_load_balancer_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.load_balancer_actions.list_load_balancer_actions(42)
            assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            assert hash(result) == hash(
                validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/actions"


def test_load_balancer_actions_add_load_balancer_service() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.load_balancer_actions.add_load_balancer_service(
            42,
            protocol="https",
            listen_port=443,
            destination_port=80,
            proxyprotocol=False,
            health_check={
                "protocol": "http",
                "port": 4711,
                "interval": 15,
                "timeout": 10,
                "retries": 3,
            },
        )
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/actions/add_service"
    assert json_of(request) == to_jsonable(
        {
            "protocol": "https",
            "listen_port": 443,
            "destination_port": 80,
            "proxyprotocol": False,
            "health_check": {
                "protocol": "http",
                "port": 4711,
                "interval": 15,
                "timeout": 10,
                "retries": 3,
            },
        }
    )


def test_async_load_balancer_actions_add_load_balancer_service() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.load_balancer_actions.add_load_balancer_service(
                42,
                protocol="https",
                listen_port=443,
                destination_port=80,
                proxyprotocol=False,
                health_check={
                    "protocol": "http",
                    "port": 4711,
                    "interval": 15,
                    "timeout": 10,
                    "retries": 3,
                },
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/actions/add_service"
    assert json_of(request) == to_jsonable(
        {
            "protocol": "https",
            "listen_port": 443,
            "destination_port": 80,
            "proxyprotocol": False,
            "health_check": {
                "protocol": "http",
                "port": 4711,
                "interval": 15,
                "timeout": 10,
                "retries": 3,
            },
        }
    )


def test_load_balancer_actions_add_load_balancer_target() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.load_balancer_actions.add_load_balancer_target(42, type="server")
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/actions/add_target"
    assert json_of(request) == to_jsonable({"type": "server"})


def test_async_load_balancer_actions_add_load_balancer_target() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.load_balancer_actions.add_load_balancer_target(42, type="server")
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/actions/add_target"
    assert json_of(request) == to_jsonable({"type": "server"})


def test_load_balancer_actions_attach_load_balancer_to_network() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.load_balancer_actions.attach_load_balancer_to_network(42, network=123)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/actions/attach_to_network"
    assert json_of(request) == to_jsonable({"network": 123})


def test_async_load_balancer_actions_attach_load_balancer_to_network() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.load_balancer_actions.attach_load_balancer_to_network(
                42, network=123
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/actions/attach_to_network"
    assert json_of(request) == to_jsonable({"network": 123})


def test_load_balancer_actions_change_load_balancer_algorithm() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.load_balancer_actions.change_load_balancer_algorithm(42, type="round_robin")
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/actions/change_algorithm"
    assert json_of(request) == to_jsonable({"type": "round_robin"})


def test_async_load_balancer_actions_change_load_balancer_algorithm() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.load_balancer_actions.change_load_balancer_algorithm(
                42, type="round_robin"
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/actions/change_algorithm"
    assert json_of(request) == to_jsonable({"type": "round_robin"})


def test_load_balancer_actions_change_load_balancer_dns_ptr() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.load_balancer_actions.change_load_balancer_dns_ptr(
            42, ip="2001:db8::1", dns_ptr="server.example.com"
        )
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/actions/change_dns_ptr"
    assert json_of(request) == to_jsonable({"ip": "2001:db8::1", "dns_ptr": "server.example.com"})


def test_async_load_balancer_actions_change_load_balancer_dns_ptr() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.load_balancer_actions.change_load_balancer_dns_ptr(
                42, ip="2001:db8::1", dns_ptr="server.example.com"
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/actions/change_dns_ptr"
    assert json_of(request) == to_jsonable({"ip": "2001:db8::1", "dns_ptr": "server.example.com"})


def test_load_balancer_actions_change_load_balancer_protection() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.load_balancer_actions.change_load_balancer_protection(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/actions/change_protection"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_async_load_balancer_actions_change_load_balancer_protection() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.load_balancer_actions.change_load_balancer_protection(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/actions/change_protection"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_load_balancer_actions_change_load_balancer_type() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.load_balancer_actions.change_load_balancer_type(
            42, load_balancer_type="lb11"
        )
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/actions/change_type"
    assert json_of(request) == to_jsonable({"load_balancer_type": "lb11"})


def test_async_load_balancer_actions_change_load_balancer_type() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.load_balancer_actions.change_load_balancer_type(
                42, load_balancer_type="lb11"
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/actions/change_type"
    assert json_of(request) == to_jsonable({"load_balancer_type": "lb11"})


def test_load_balancer_actions_delete_load_balancer_service() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.load_balancer_actions.delete_load_balancer_service(42, listen_port=443)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/actions/delete_service"
    assert json_of(request) == to_jsonable({"listen_port": 443})


def test_async_load_balancer_actions_delete_load_balancer_service() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.load_balancer_actions.delete_load_balancer_service(
                42, listen_port=443
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/actions/delete_service"
    assert json_of(request) == to_jsonable({"listen_port": 443})


def test_load_balancer_actions_detach_load_balancer_from_network() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.load_balancer_actions.detach_load_balancer_from_network(42, network=4711)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert (
        request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/actions/detach_from_network"
    )
    assert json_of(request) == to_jsonable({"network": 4711})


def test_async_load_balancer_actions_detach_load_balancer_from_network() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.load_balancer_actions.detach_load_balancer_from_network(
                42, network=4711
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert (
        request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/actions/detach_from_network"
    )
    assert json_of(request) == to_jsonable({"network": 4711})


def test_load_balancer_actions_disable_load_balancer_public_interface() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.load_balancer_actions.disable_load_balancer_public_interface(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert (
        request.url.raw_path.split(b"?")[0]
        == b"/v1/load_balancers/42/actions/disable_public_interface"
    )


def test_async_load_balancer_actions_disable_load_balancer_public_interface() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.load_balancer_actions.disable_load_balancer_public_interface(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert (
        request.url.raw_path.split(b"?")[0]
        == b"/v1/load_balancers/42/actions/disable_public_interface"
    )


def test_load_balancer_actions_enable_load_balancer_public_interface() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.load_balancer_actions.enable_load_balancer_public_interface(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert (
        request.url.raw_path.split(b"?")[0]
        == b"/v1/load_balancers/42/actions/enable_public_interface"
    )


def test_async_load_balancer_actions_enable_load_balancer_public_interface() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.load_balancer_actions.enable_load_balancer_public_interface(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert (
        request.url.raw_path.split(b"?")[0]
        == b"/v1/load_balancers/42/actions/enable_public_interface"
    )


def test_load_balancer_actions_remove_load_balancer_target() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.load_balancer_actions.remove_load_balancer_target(42, type="server")
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/actions/remove_target"
    assert json_of(request) == to_jsonable({"type": "server"})


def test_async_load_balancer_actions_remove_load_balancer_target() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.load_balancer_actions.remove_load_balancer_target(
                42, type="server"
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/actions/remove_target"
    assert json_of(request) == to_jsonable({"type": "server"})


def test_load_balancer_actions_update_load_balancer_service() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.load_balancer_actions.update_load_balancer_service(42, listen_port=443)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/actions/update_service"
    assert json_of(request) == to_jsonable({"listen_port": 443})


def test_async_load_balancer_actions_update_load_balancer_service() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.load_balancer_actions.update_load_balancer_service(
                42, listen_port=443
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/actions/update_service"
    assert json_of(request) == to_jsonable({"listen_port": 443})


def test_load_balancer_actions_get_load_balancer_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        deprecated_method = client.load_balancer_actions.get_load_balancer_action  # type: ignore[deprecated]  # pyright: ignore[reportDeprecated]
        with pytest.deprecated_call():
            result = deprecated_method(42, 42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/actions/42"


def test_async_load_balancer_actions_get_load_balancer_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            deprecated_method = client.load_balancer_actions.get_load_balancer_action  # type: ignore[deprecated]  # pyright: ignore[reportDeprecated]
            with pytest.deprecated_call():
                result = await deprecated_method(42, 42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/actions/42"

"""Generated tests for ``firewalls``."""

import asyncio

from hetzner_api.models import CreateFirewallResponse, FirewallResponse, FirewallsResponse
from tests.payloads import CREATE_FIREWALL_RESPONSE, FIREWALL_RESPONSE, FIREWALLS_RESPONSE
from tests.support import Recorder, async_client, json_of, sync_client, to_jsonable, validated


def test_firewalls_list_firewalls() -> None:
    recorder = Recorder(200, FIREWALLS_RESPONSE)
    with sync_client(recorder) as client:
        result = client.firewalls.list_firewalls()
        assert result == validated(FirewallsResponse, FIREWALLS_RESPONSE)
        assert hash(result) == hash(validated(FirewallsResponse, FIREWALLS_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/firewalls"


def test_async_firewalls_list_firewalls() -> None:
    recorder = Recorder(200, FIREWALLS_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.firewalls.list_firewalls()
            assert result == validated(FirewallsResponse, FIREWALLS_RESPONSE)
            assert hash(result) == hash(validated(FirewallsResponse, FIREWALLS_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/firewalls"


def test_firewalls_create_firewall() -> None:
    recorder = Recorder(200, CREATE_FIREWALL_RESPONSE)
    with sync_client(recorder) as client:
        result = client.firewalls.create_firewall(name="new-name")
        assert result == validated(CreateFirewallResponse, CREATE_FIREWALL_RESPONSE)
        assert hash(result) == hash(validated(CreateFirewallResponse, CREATE_FIREWALL_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/firewalls"
    assert json_of(request) == to_jsonable({"name": "new-name"})


def test_async_firewalls_create_firewall() -> None:
    recorder = Recorder(200, CREATE_FIREWALL_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.firewalls.create_firewall(name="new-name")
            assert result == validated(CreateFirewallResponse, CREATE_FIREWALL_RESPONSE)
            assert hash(result) == hash(validated(CreateFirewallResponse, CREATE_FIREWALL_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/firewalls"
    assert json_of(request) == to_jsonable({"name": "new-name"})


def test_firewalls_get_firewall() -> None:
    recorder = Recorder(200, FIREWALL_RESPONSE)
    with sync_client(recorder) as client:
        result = client.firewalls.get_firewall(42)
        assert result == validated(FirewallResponse, FIREWALL_RESPONSE)
        assert hash(result) == hash(validated(FirewallResponse, FIREWALL_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/firewalls/42"


def test_async_firewalls_get_firewall() -> None:
    recorder = Recorder(200, FIREWALL_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.firewalls.get_firewall(42)
            assert result == validated(FirewallResponse, FIREWALL_RESPONSE)
            assert hash(result) == hash(validated(FirewallResponse, FIREWALL_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/firewalls/42"


def test_firewalls_update_firewall() -> None:
    recorder = Recorder(200, FIREWALL_RESPONSE)
    with sync_client(recorder) as client:
        result = client.firewalls.update_firewall(42)
        assert result == validated(FirewallResponse, FIREWALL_RESPONSE)
        assert hash(result) == hash(validated(FirewallResponse, FIREWALL_RESPONSE))
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/firewalls/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_async_firewalls_update_firewall() -> None:
    recorder = Recorder(200, FIREWALL_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.firewalls.update_firewall(42)
            assert result == validated(FirewallResponse, FIREWALL_RESPONSE)
            assert hash(result) == hash(validated(FirewallResponse, FIREWALL_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/firewalls/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_firewalls_delete_firewall() -> None:
    recorder = Recorder(204, None)
    with sync_client(recorder) as client:
        client.firewalls.delete_firewall(42)
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/firewalls/42"


def test_async_firewalls_delete_firewall() -> None:
    recorder = Recorder(204, None)

    async def run() -> None:
        async with async_client(recorder) as client:
            await client.firewalls.delete_firewall(42)

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/firewalls/42"

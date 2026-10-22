"""Generated tests for ``floating_ips``."""

import asyncio

from hetzner_api.models import CreateFloatingIpResponse, FloatingIpResponse, ListFloatingIpsResponse
from tests.payloads import (
    CREATE_FLOATING_IP_RESPONSE,
    FLOATING_IP_RESPONSE,
    LIST_FLOATING_IPS_RESPONSE,
)
from tests.support import Recorder, async_client, json_of, sync_client, to_jsonable, validated


def test_floating_ips_list_floating_ips() -> None:
    recorder = Recorder(200, LIST_FLOATING_IPS_RESPONSE)
    with sync_client(recorder) as client:
        result = client.floating_ips.list_floating_ips()
        assert result == validated(ListFloatingIpsResponse, LIST_FLOATING_IPS_RESPONSE)
        assert hash(result) == hash(validated(ListFloatingIpsResponse, LIST_FLOATING_IPS_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/floating_ips"


def test_async_floating_ips_list_floating_ips() -> None:
    recorder = Recorder(200, LIST_FLOATING_IPS_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.floating_ips.list_floating_ips()
            assert result == validated(ListFloatingIpsResponse, LIST_FLOATING_IPS_RESPONSE)
            assert hash(result) == hash(
                validated(ListFloatingIpsResponse, LIST_FLOATING_IPS_RESPONSE)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/floating_ips"


def test_floating_ips_create_floating_ip() -> None:
    recorder = Recorder(200, CREATE_FLOATING_IP_RESPONSE)
    with sync_client(recorder) as client:
        result = client.floating_ips.create_floating_ip(type="ipv6")
        assert result == validated(CreateFloatingIpResponse, CREATE_FLOATING_IP_RESPONSE)
        assert hash(result) == hash(
            validated(CreateFloatingIpResponse, CREATE_FLOATING_IP_RESPONSE)
        )
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/floating_ips"
    assert json_of(request) == to_jsonable({"type": "ipv6"})


def test_async_floating_ips_create_floating_ip() -> None:
    recorder = Recorder(200, CREATE_FLOATING_IP_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.floating_ips.create_floating_ip(type="ipv6")
            assert result == validated(CreateFloatingIpResponse, CREATE_FLOATING_IP_RESPONSE)
            assert hash(result) == hash(
                validated(CreateFloatingIpResponse, CREATE_FLOATING_IP_RESPONSE)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/floating_ips"
    assert json_of(request) == to_jsonable({"type": "ipv6"})


def test_floating_ips_get_floating_ip() -> None:
    recorder = Recorder(200, FLOATING_IP_RESPONSE)
    with sync_client(recorder) as client:
        result = client.floating_ips.get_floating_ip(42)
        assert result == validated(FloatingIpResponse, FLOATING_IP_RESPONSE)
        assert hash(result) == hash(validated(FloatingIpResponse, FLOATING_IP_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/floating_ips/42"


def test_async_floating_ips_get_floating_ip() -> None:
    recorder = Recorder(200, FLOATING_IP_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.floating_ips.get_floating_ip(42)
            assert result == validated(FloatingIpResponse, FLOATING_IP_RESPONSE)
            assert hash(result) == hash(validated(FloatingIpResponse, FLOATING_IP_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/floating_ips/42"


def test_floating_ips_update_floating_ip() -> None:
    recorder = Recorder(200, FLOATING_IP_RESPONSE)
    with sync_client(recorder) as client:
        result = client.floating_ips.update_floating_ip(42)
        assert result == validated(FloatingIpResponse, FLOATING_IP_RESPONSE)
        assert hash(result) == hash(validated(FloatingIpResponse, FLOATING_IP_RESPONSE))
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/floating_ips/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_async_floating_ips_update_floating_ip() -> None:
    recorder = Recorder(200, FLOATING_IP_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.floating_ips.update_floating_ip(42)
            assert result == validated(FloatingIpResponse, FLOATING_IP_RESPONSE)
            assert hash(result) == hash(validated(FloatingIpResponse, FLOATING_IP_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/floating_ips/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_floating_ips_delete_floating_ip() -> None:
    recorder = Recorder(204, None)
    with sync_client(recorder) as client:
        client.floating_ips.delete_floating_ip(42)
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/floating_ips/42"


def test_async_floating_ips_delete_floating_ip() -> None:
    recorder = Recorder(204, None)

    async def run() -> None:
        async with async_client(recorder) as client:
            await client.floating_ips.delete_floating_ip(42)

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/floating_ips/42"

"""Generated tests for ``primary_ips``."""

import asyncio

from hetzner_api.models import CreatePrimaryIPResponse, PrimaryIPResponse, PrimaryIPsResponse
from tests.payloads import CREATE_PRIMARY_IP_RESPONSE, PRIMARY_I_PS_RESPONSE, PRIMARY_IP_RESPONSE
from tests.support import Recorder, async_client, json_of, sync_client, to_jsonable, validated


def test_primary_ips_list_primary_ips() -> None:
    recorder = Recorder(200, PRIMARY_I_PS_RESPONSE)
    with sync_client(recorder) as client:
        result = client.primary_ips.list_primary_ips()
        assert result == validated(PrimaryIPsResponse, PRIMARY_I_PS_RESPONSE)
        assert hash(result) == hash(validated(PrimaryIPsResponse, PRIMARY_I_PS_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/primary_ips"


def test_async_primary_ips_list_primary_ips() -> None:
    recorder = Recorder(200, PRIMARY_I_PS_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.primary_ips.list_primary_ips()
            assert result == validated(PrimaryIPsResponse, PRIMARY_I_PS_RESPONSE)
            assert hash(result) == hash(validated(PrimaryIPsResponse, PRIMARY_I_PS_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/primary_ips"


def test_primary_ips_create_primary_ip() -> None:
    recorder = Recorder(200, CREATE_PRIMARY_IP_RESPONSE)
    with sync_client(recorder) as client:
        result = client.primary_ips.create_primary_ip(name="my-resource", type="ipv6")
        assert result == validated(CreatePrimaryIPResponse, CREATE_PRIMARY_IP_RESPONSE)
        assert hash(result) == hash(validated(CreatePrimaryIPResponse, CREATE_PRIMARY_IP_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/primary_ips"
    assert json_of(request) == to_jsonable({"name": "my-resource", "type": "ipv6"})


def test_async_primary_ips_create_primary_ip() -> None:
    recorder = Recorder(200, CREATE_PRIMARY_IP_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.primary_ips.create_primary_ip(name="my-resource", type="ipv6")
            assert result == validated(CreatePrimaryIPResponse, CREATE_PRIMARY_IP_RESPONSE)
            assert hash(result) == hash(
                validated(CreatePrimaryIPResponse, CREATE_PRIMARY_IP_RESPONSE)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/primary_ips"
    assert json_of(request) == to_jsonable({"name": "my-resource", "type": "ipv6"})


def test_primary_ips_get_primary_ip() -> None:
    recorder = Recorder(200, PRIMARY_IP_RESPONSE)
    with sync_client(recorder) as client:
        result = client.primary_ips.get_primary_ip(42)
        assert result == validated(PrimaryIPResponse, PRIMARY_IP_RESPONSE)
        assert hash(result) == hash(validated(PrimaryIPResponse, PRIMARY_IP_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/primary_ips/42"


def test_async_primary_ips_get_primary_ip() -> None:
    recorder = Recorder(200, PRIMARY_IP_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.primary_ips.get_primary_ip(42)
            assert result == validated(PrimaryIPResponse, PRIMARY_IP_RESPONSE)
            assert hash(result) == hash(validated(PrimaryIPResponse, PRIMARY_IP_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/primary_ips/42"


def test_primary_ips_update_primary_ip() -> None:
    recorder = Recorder(200, PRIMARY_IP_RESPONSE)
    with sync_client(recorder) as client:
        result = client.primary_ips.update_primary_ip(42)
        assert result == validated(PrimaryIPResponse, PRIMARY_IP_RESPONSE)
        assert hash(result) == hash(validated(PrimaryIPResponse, PRIMARY_IP_RESPONSE))
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/primary_ips/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_async_primary_ips_update_primary_ip() -> None:
    recorder = Recorder(200, PRIMARY_IP_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.primary_ips.update_primary_ip(42)
            assert result == validated(PrimaryIPResponse, PRIMARY_IP_RESPONSE)
            assert hash(result) == hash(validated(PrimaryIPResponse, PRIMARY_IP_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/primary_ips/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_primary_ips_delete_primary_ip() -> None:
    recorder = Recorder(204, None)
    with sync_client(recorder) as client:
        client.primary_ips.delete_primary_ip(42)
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/primary_ips/42"


def test_async_primary_ips_delete_primary_ip() -> None:
    recorder = Recorder(204, None)

    async def run() -> None:
        async with async_client(recorder) as client:
            await client.primary_ips.delete_primary_ip(42)

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/primary_ips/42"

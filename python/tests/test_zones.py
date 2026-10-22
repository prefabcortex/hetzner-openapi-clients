"""Generated tests for ``zones``."""

import asyncio

from hetzner_api.models import (
    ActionResponse,
    CreateZoneResponse,
    ListZonesResponse,
    Zonefile,
    ZoneResponse,
)
from tests.payloads import (
    ACTION_RESPONSE,
    CREATE_ZONE_RESPONSE,
    LIST_ZONES_RESPONSE,
    ZONE_RESPONSE,
    ZONEFILE,
)
from tests.support import Recorder, async_client, json_of, sync_client, to_jsonable, validated


def test_zones_list_zones() -> None:
    recorder = Recorder(200, LIST_ZONES_RESPONSE)
    with sync_client(recorder) as client:
        result = client.zones.list_zones()
        assert result == validated(ListZonesResponse, LIST_ZONES_RESPONSE)
        assert hash(result) == hash(validated(ListZonesResponse, LIST_ZONES_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/zones"


def test_async_zones_list_zones() -> None:
    recorder = Recorder(200, LIST_ZONES_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.zones.list_zones()
            assert result == validated(ListZonesResponse, LIST_ZONES_RESPONSE)
            assert hash(result) == hash(validated(ListZonesResponse, LIST_ZONES_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/zones"


def test_zones_create_zone() -> None:
    recorder = Recorder(200, CREATE_ZONE_RESPONSE)
    with sync_client(recorder) as client:
        result = client.zones.create_zone(name="example.com", mode="primary")
        assert result == validated(CreateZoneResponse, CREATE_ZONE_RESPONSE)
        assert hash(result) == hash(validated(CreateZoneResponse, CREATE_ZONE_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/zones"
    assert json_of(request) == to_jsonable({"name": "example.com", "mode": "primary"})


def test_async_zones_create_zone() -> None:
    recorder = Recorder(200, CREATE_ZONE_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.zones.create_zone(name="example.com", mode="primary")
            assert result == validated(CreateZoneResponse, CREATE_ZONE_RESPONSE)
            assert hash(result) == hash(validated(CreateZoneResponse, CREATE_ZONE_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/zones"
    assert json_of(request) == to_jsonable({"name": "example.com", "mode": "primary"})


def test_zones_get_zone() -> None:
    recorder = Recorder(200, ZONE_RESPONSE)
    with sync_client(recorder) as client:
        result = client.zones.get_zone("example")
        assert result == validated(ZoneResponse, ZONE_RESPONSE)
        assert hash(result) == hash(validated(ZoneResponse, ZONE_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/zones/example"


def test_async_zones_get_zone() -> None:
    recorder = Recorder(200, ZONE_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.zones.get_zone("example")
            assert result == validated(ZoneResponse, ZONE_RESPONSE)
            assert hash(result) == hash(validated(ZoneResponse, ZONE_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/zones/example"


def test_zones_update_zone() -> None:
    recorder = Recorder(200, ZONE_RESPONSE)
    with sync_client(recorder) as client:
        result = client.zones.update_zone("example")
        assert result == validated(ZoneResponse, ZONE_RESPONSE)
        assert hash(result) == hash(validated(ZoneResponse, ZONE_RESPONSE))
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/zones/example"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_async_zones_update_zone() -> None:
    recorder = Recorder(200, ZONE_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.zones.update_zone("example")
            assert result == validated(ZoneResponse, ZONE_RESPONSE)
            assert hash(result) == hash(validated(ZoneResponse, ZONE_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/zones/example"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_zones_delete_zone() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.zones.delete_zone("example")
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/zones/example"


def test_async_zones_delete_zone() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.zones.delete_zone("example")
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/zones/example"


def test_zones_get_zone_zonefile() -> None:
    recorder = Recorder(200, ZONEFILE)
    with sync_client(recorder) as client:
        result = client.zones.get_zone_zonefile("example")
        assert result == validated(Zonefile, ZONEFILE)
        assert hash(result) == hash(validated(Zonefile, ZONEFILE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/zones/example/zonefile"


def test_async_zones_get_zone_zonefile() -> None:
    recorder = Recorder(200, ZONEFILE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.zones.get_zone_zonefile("example")
            assert result == validated(Zonefile, ZONEFILE)
            assert hash(result) == hash(validated(Zonefile, ZONEFILE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/zones/example/zonefile"

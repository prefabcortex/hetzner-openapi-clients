"""Generated tests for ``zone_rrsets``."""

import asyncio

from hetzner_api.models import (
    ActionResponse,
    CreateZoneRrsetResponse,
    ListZoneRrsetsResponse,
    RrsetResponse,
)
from tests.payloads import (
    ACTION_RESPONSE,
    CREATE_ZONE_RRSET_RESPONSE,
    LIST_ZONE_RRSETS_RESPONSE,
    RRSET_RESPONSE,
)
from tests.support import Recorder, async_client, json_of, sync_client, to_jsonable, validated


def test_zone_rrsets_list_zone_rrsets() -> None:
    recorder = Recorder(200, LIST_ZONE_RRSETS_RESPONSE)
    with sync_client(recorder) as client:
        result = client.zone_rrsets.list_zone_rrsets("example")
        assert result == validated(ListZoneRrsetsResponse, LIST_ZONE_RRSETS_RESPONSE)
        assert hash(result) == hash(validated(ListZoneRrsetsResponse, LIST_ZONE_RRSETS_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/zones/example/rrsets"


def test_async_zone_rrsets_list_zone_rrsets() -> None:
    recorder = Recorder(200, LIST_ZONE_RRSETS_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.zone_rrsets.list_zone_rrsets("example")
            assert result == validated(ListZoneRrsetsResponse, LIST_ZONE_RRSETS_RESPONSE)
            assert hash(result) == hash(
                validated(ListZoneRrsetsResponse, LIST_ZONE_RRSETS_RESPONSE)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/zones/example/rrsets"


def test_zone_rrsets_create_zone_rrset() -> None:
    recorder = Recorder(200, CREATE_ZONE_RRSET_RESPONSE)
    with sync_client(recorder) as client:
        result = client.zone_rrsets.create_zone_rrset(
            "example", name="www", type="A", records=[{"value": "198.51.100.1"}]
        )
        assert result == validated(CreateZoneRrsetResponse, CREATE_ZONE_RRSET_RESPONSE)
        assert hash(result) == hash(validated(CreateZoneRrsetResponse, CREATE_ZONE_RRSET_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/zones/example/rrsets"
    assert json_of(request) == to_jsonable(
        {"name": "www", "type": "A", "records": [{"value": "198.51.100.1"}]}
    )


def test_async_zone_rrsets_create_zone_rrset() -> None:
    recorder = Recorder(200, CREATE_ZONE_RRSET_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.zone_rrsets.create_zone_rrset(
                "example", name="www", type="A", records=[{"value": "198.51.100.1"}]
            )
            assert result == validated(CreateZoneRrsetResponse, CREATE_ZONE_RRSET_RESPONSE)
            assert hash(result) == hash(
                validated(CreateZoneRrsetResponse, CREATE_ZONE_RRSET_RESPONSE)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/zones/example/rrsets"
    assert json_of(request) == to_jsonable(
        {"name": "www", "type": "A", "records": [{"value": "198.51.100.1"}]}
    )


def test_zone_rrsets_get_zone_rrset() -> None:
    recorder = Recorder(200, RRSET_RESPONSE)
    with sync_client(recorder) as client:
        result = client.zone_rrsets.get_zone_rrset("example", "www", "A")
        assert result == validated(RrsetResponse, RRSET_RESPONSE)
        assert hash(result) == hash(validated(RrsetResponse, RRSET_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/zones/example/rrsets/www/A"


def test_async_zone_rrsets_get_zone_rrset() -> None:
    recorder = Recorder(200, RRSET_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.zone_rrsets.get_zone_rrset("example", "www", "A")
            assert result == validated(RrsetResponse, RRSET_RESPONSE)
            assert hash(result) == hash(validated(RrsetResponse, RRSET_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/zones/example/rrsets/www/A"


def test_zone_rrsets_update_zone_rrset() -> None:
    recorder = Recorder(200, RRSET_RESPONSE)
    with sync_client(recorder) as client:
        result = client.zone_rrsets.update_zone_rrset("example", "www", "A")
        assert result == validated(RrsetResponse, RRSET_RESPONSE)
        assert hash(result) == hash(validated(RrsetResponse, RRSET_RESPONSE))
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/zones/example/rrsets/www/A"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_async_zone_rrsets_update_zone_rrset() -> None:
    recorder = Recorder(200, RRSET_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.zone_rrsets.update_zone_rrset("example", "www", "A")
            assert result == validated(RrsetResponse, RRSET_RESPONSE)
            assert hash(result) == hash(validated(RrsetResponse, RRSET_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/zones/example/rrsets/www/A"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_zone_rrsets_delete_zone_rrset() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.zone_rrsets.delete_zone_rrset("example", "www", "A")
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/zones/example/rrsets/www/A"


def test_async_zone_rrsets_delete_zone_rrset() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.zone_rrsets.delete_zone_rrset("example", "www", "A")
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/zones/example/rrsets/www/A"

"""Generated tests for ``locations``."""

import asyncio

from hetzner_api.models import GetLocationResponse, ListLocationsResponse
from tests.payloads import GET_LOCATION_RESPONSE, LIST_LOCATIONS_RESPONSE
from tests.support import Recorder, async_client, sync_client, validated


def test_locations_list_locations() -> None:
    recorder = Recorder(200, LIST_LOCATIONS_RESPONSE)
    with sync_client(recorder) as client:
        result = client.locations.list_locations()
        assert result == validated(ListLocationsResponse, LIST_LOCATIONS_RESPONSE)
        assert hash(result) == hash(validated(ListLocationsResponse, LIST_LOCATIONS_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/locations"


def test_async_locations_list_locations() -> None:
    recorder = Recorder(200, LIST_LOCATIONS_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.locations.list_locations()
            assert result == validated(ListLocationsResponse, LIST_LOCATIONS_RESPONSE)
            assert hash(result) == hash(validated(ListLocationsResponse, LIST_LOCATIONS_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/locations"


def test_locations_get_location() -> None:
    recorder = Recorder(200, GET_LOCATION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.locations.get_location(42)
        assert result == validated(GetLocationResponse, GET_LOCATION_RESPONSE)
        assert hash(result) == hash(validated(GetLocationResponse, GET_LOCATION_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/locations/42"


def test_async_locations_get_location() -> None:
    recorder = Recorder(200, GET_LOCATION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.locations.get_location(42)
            assert result == validated(GetLocationResponse, GET_LOCATION_RESPONSE)
            assert hash(result) == hash(validated(GetLocationResponse, GET_LOCATION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/locations/42"

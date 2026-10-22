"""Generated tests for ``zone_rrset_actions``."""

import asyncio

from hetzner_api.models import ActionResponse
from tests.payloads import ACTION_RESPONSE
from tests.support import Recorder, async_client, json_of, sync_client, to_jsonable, validated


def test_zone_rrset_actions_change_zone_rrset_protection() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.zone_rrset_actions.change_zone_rrset_protection(
            "example", "www", "A", change=False
        )
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert (
        request.url.raw_path.split(b"?")[0]
        == b"/v1/zones/example/rrsets/www/A/actions/change_protection"
    )
    assert json_of(request) == to_jsonable({"change": False})


def test_async_zone_rrset_actions_change_zone_rrset_protection() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.zone_rrset_actions.change_zone_rrset_protection(
                "example", "www", "A", change=False
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert (
        request.url.raw_path.split(b"?")[0]
        == b"/v1/zones/example/rrsets/www/A/actions/change_protection"
    )
    assert json_of(request) == to_jsonable({"change": False})


def test_zone_rrset_actions_change_zone_rrset_ttl() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.zone_rrset_actions.change_zone_rrset_ttl("example", "www", "A", ttl=3600)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert (
        request.url.raw_path.split(b"?")[0] == b"/v1/zones/example/rrsets/www/A/actions/change_ttl"
    )
    assert json_of(request) == to_jsonable({"ttl": 3600})


def test_async_zone_rrset_actions_change_zone_rrset_ttl() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.zone_rrset_actions.change_zone_rrset_ttl(
                "example", "www", "A", ttl=3600
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert (
        request.url.raw_path.split(b"?")[0] == b"/v1/zones/example/rrsets/www/A/actions/change_ttl"
    )
    assert json_of(request) == to_jsonable({"ttl": 3600})


def test_zone_rrset_actions_set_zone_rrset_records() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.zone_rrset_actions.set_zone_rrset_records(
            "example", "www", "A", records=[{"value": "198.51.100.1"}]
        )
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert (
        request.url.raw_path.split(b"?")[0] == b"/v1/zones/example/rrsets/www/A/actions/set_records"
    )
    assert json_of(request) == to_jsonable({"records": [{"value": "198.51.100.1"}]})


def test_async_zone_rrset_actions_set_zone_rrset_records() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.zone_rrset_actions.set_zone_rrset_records(
                "example", "www", "A", records=[{"value": "198.51.100.1"}]
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert (
        request.url.raw_path.split(b"?")[0] == b"/v1/zones/example/rrsets/www/A/actions/set_records"
    )
    assert json_of(request) == to_jsonable({"records": [{"value": "198.51.100.1"}]})


def test_zone_rrset_actions_add_zone_rrset_records() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.zone_rrset_actions.add_zone_rrset_records(
            "example", "www", "A", records=[{"value": "198.51.100.1"}]
        )
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert (
        request.url.raw_path.split(b"?")[0] == b"/v1/zones/example/rrsets/www/A/actions/add_records"
    )
    assert json_of(request) == to_jsonable({"records": [{"value": "198.51.100.1"}]})


def test_async_zone_rrset_actions_add_zone_rrset_records() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.zone_rrset_actions.add_zone_rrset_records(
                "example", "www", "A", records=[{"value": "198.51.100.1"}]
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert (
        request.url.raw_path.split(b"?")[0] == b"/v1/zones/example/rrsets/www/A/actions/add_records"
    )
    assert json_of(request) == to_jsonable({"records": [{"value": "198.51.100.1"}]})


def test_zone_rrset_actions_remove_zone_rrset_records() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.zone_rrset_actions.remove_zone_rrset_records(
            "example", "www", "A", records=[{"value": "198.51.100.1"}]
        )
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert (
        request.url.raw_path.split(b"?")[0]
        == b"/v1/zones/example/rrsets/www/A/actions/remove_records"
    )
    assert json_of(request) == to_jsonable({"records": [{"value": "198.51.100.1"}]})


def test_async_zone_rrset_actions_remove_zone_rrset_records() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.zone_rrset_actions.remove_zone_rrset_records(
                "example", "www", "A", records=[{"value": "198.51.100.1"}]
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert (
        request.url.raw_path.split(b"?")[0]
        == b"/v1/zones/example/rrsets/www/A/actions/remove_records"
    )
    assert json_of(request) == to_jsonable({"records": [{"value": "198.51.100.1"}]})


def test_zone_rrset_actions_update_zone_rrset_records() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.zone_rrset_actions.update_zone_rrset_records(
            "example",
            "www",
            "A",
            records=[{"value": "198.51.100.1", "comment": "My web server at Hetzner Cloud."}],
        )
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert (
        request.url.raw_path.split(b"?")[0]
        == b"/v1/zones/example/rrsets/www/A/actions/update_records"
    )
    assert json_of(request) == to_jsonable(
        {"records": [{"value": "198.51.100.1", "comment": "My web server at Hetzner Cloud."}]}
    )


def test_async_zone_rrset_actions_update_zone_rrset_records() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.zone_rrset_actions.update_zone_rrset_records(
                "example",
                "www",
                "A",
                records=[{"value": "198.51.100.1", "comment": "My web server at Hetzner Cloud."}],
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert (
        request.url.raw_path.split(b"?")[0]
        == b"/v1/zones/example/rrsets/www/A/actions/update_records"
    )
    assert json_of(request) == to_jsonable(
        {"records": [{"value": "198.51.100.1", "comment": "My web server at Hetzner Cloud."}]}
    )

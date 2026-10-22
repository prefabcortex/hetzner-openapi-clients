"""Generated tests for ``placement_groups``."""

import asyncio

from hetzner_api.models import (
    CreatePlacementGroupResponse,
    PlacementGroupResponse,
    PlacementGroupsResponse,
)
from tests.payloads import (
    CREATE_PLACEMENT_GROUP_RESPONSE,
    PLACEMENT_GROUP_RESPONSE,
    PLACEMENT_GROUPS_RESPONSE,
)
from tests.support import Recorder, async_client, json_of, sync_client, to_jsonable, validated


def test_placement_groups_list_placement_groups() -> None:
    recorder = Recorder(200, PLACEMENT_GROUPS_RESPONSE)
    with sync_client(recorder) as client:
        result = client.placement_groups.list_placement_groups()
        assert result == validated(PlacementGroupsResponse, PLACEMENT_GROUPS_RESPONSE)
        assert hash(result) == hash(validated(PlacementGroupsResponse, PLACEMENT_GROUPS_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/placement_groups"


def test_async_placement_groups_list_placement_groups() -> None:
    recorder = Recorder(200, PLACEMENT_GROUPS_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.placement_groups.list_placement_groups()
            assert result == validated(PlacementGroupsResponse, PLACEMENT_GROUPS_RESPONSE)
            assert hash(result) == hash(
                validated(PlacementGroupsResponse, PLACEMENT_GROUPS_RESPONSE)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/placement_groups"


def test_placement_groups_create_placement_group() -> None:
    recorder = Recorder(200, CREATE_PLACEMENT_GROUP_RESPONSE)
    with sync_client(recorder) as client:
        result = client.placement_groups.create_placement_group(
            name="my Placement Group", type="spread"
        )
        assert result == validated(CreatePlacementGroupResponse, CREATE_PLACEMENT_GROUP_RESPONSE)
        assert hash(result) == hash(
            validated(CreatePlacementGroupResponse, CREATE_PLACEMENT_GROUP_RESPONSE)
        )
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/placement_groups"
    assert json_of(request) == to_jsonable({"name": "my Placement Group", "type": "spread"})


def test_async_placement_groups_create_placement_group() -> None:
    recorder = Recorder(200, CREATE_PLACEMENT_GROUP_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.placement_groups.create_placement_group(
                name="my Placement Group", type="spread"
            )
            assert result == validated(
                CreatePlacementGroupResponse, CREATE_PLACEMENT_GROUP_RESPONSE
            )
            assert hash(result) == hash(
                validated(CreatePlacementGroupResponse, CREATE_PLACEMENT_GROUP_RESPONSE)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/placement_groups"
    assert json_of(request) == to_jsonable({"name": "my Placement Group", "type": "spread"})


def test_placement_groups_get_placement_group() -> None:
    recorder = Recorder(200, PLACEMENT_GROUP_RESPONSE)
    with sync_client(recorder) as client:
        result = client.placement_groups.get_placement_group(42)
        assert result == validated(PlacementGroupResponse, PLACEMENT_GROUP_RESPONSE)
        assert hash(result) == hash(validated(PlacementGroupResponse, PLACEMENT_GROUP_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/placement_groups/42"


def test_async_placement_groups_get_placement_group() -> None:
    recorder = Recorder(200, PLACEMENT_GROUP_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.placement_groups.get_placement_group(42)
            assert result == validated(PlacementGroupResponse, PLACEMENT_GROUP_RESPONSE)
            assert hash(result) == hash(validated(PlacementGroupResponse, PLACEMENT_GROUP_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/placement_groups/42"


def test_placement_groups_update_placement_group() -> None:
    recorder = Recorder(200, PLACEMENT_GROUP_RESPONSE)
    with sync_client(recorder) as client:
        result = client.placement_groups.update_placement_group(42)
        assert result == validated(PlacementGroupResponse, PLACEMENT_GROUP_RESPONSE)
        assert hash(result) == hash(validated(PlacementGroupResponse, PLACEMENT_GROUP_RESPONSE))
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/placement_groups/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_async_placement_groups_update_placement_group() -> None:
    recorder = Recorder(200, PLACEMENT_GROUP_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.placement_groups.update_placement_group(42)
            assert result == validated(PlacementGroupResponse, PLACEMENT_GROUP_RESPONSE)
            assert hash(result) == hash(validated(PlacementGroupResponse, PLACEMENT_GROUP_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/placement_groups/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_placement_groups_delete_placement_group() -> None:
    recorder = Recorder(204, None)
    with sync_client(recorder) as client:
        client.placement_groups.delete_placement_group(42)
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/placement_groups/42"


def test_async_placement_groups_delete_placement_group() -> None:
    recorder = Recorder(204, None)

    async def run() -> None:
        async with async_client(recorder) as client:
            await client.placement_groups.delete_placement_group(42)

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/placement_groups/42"

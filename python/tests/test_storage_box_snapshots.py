"""Generated tests for ``storage_box_snapshots``."""

import asyncio

from hetzner_api.models import (
    ActionResponse,
    CreateStorageBoxSnapshotResponse,
    ListStorageBoxSnapshotsResponse,
    SnapshotResponse,
)
from tests.payloads import (
    ACTION_RESPONSE,
    CREATE_STORAGE_BOX_SNAPSHOT_RESPONSE,
    LIST_STORAGE_BOX_SNAPSHOTS_RESPONSE,
    SNAPSHOT_RESPONSE,
)
from tests.support import Recorder, async_client, json_of, sync_client, to_jsonable, validated


def test_storage_box_snapshots_list_storage_box_snapshots() -> None:
    recorder = Recorder(200, LIST_STORAGE_BOX_SNAPSHOTS_RESPONSE)
    with sync_client(recorder) as client:
        result = client.storage_box_snapshots.list_storage_box_snapshots(42)
        assert result == validated(
            ListStorageBoxSnapshotsResponse, LIST_STORAGE_BOX_SNAPSHOTS_RESPONSE
        )
        assert hash(result) == hash(
            validated(ListStorageBoxSnapshotsResponse, LIST_STORAGE_BOX_SNAPSHOTS_RESPONSE)
        )
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/snapshots"


def test_async_storage_box_snapshots_list_storage_box_snapshots() -> None:
    recorder = Recorder(200, LIST_STORAGE_BOX_SNAPSHOTS_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_box_snapshots.list_storage_box_snapshots(42)
            assert result == validated(
                ListStorageBoxSnapshotsResponse, LIST_STORAGE_BOX_SNAPSHOTS_RESPONSE
            )
            assert hash(result) == hash(
                validated(ListStorageBoxSnapshotsResponse, LIST_STORAGE_BOX_SNAPSHOTS_RESPONSE)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/snapshots"


def test_storage_box_snapshots_create_storage_box_snapshot() -> None:
    recorder = Recorder(200, CREATE_STORAGE_BOX_SNAPSHOT_RESPONSE)
    with sync_client(recorder) as client:
        result = client.storage_box_snapshots.create_storage_box_snapshot(42)
        assert result == validated(
            CreateStorageBoxSnapshotResponse, CREATE_STORAGE_BOX_SNAPSHOT_RESPONSE
        )
        assert hash(result) == hash(
            validated(CreateStorageBoxSnapshotResponse, CREATE_STORAGE_BOX_SNAPSHOT_RESPONSE)
        )
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/snapshots"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_async_storage_box_snapshots_create_storage_box_snapshot() -> None:
    recorder = Recorder(200, CREATE_STORAGE_BOX_SNAPSHOT_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_box_snapshots.create_storage_box_snapshot(42)
            assert result == validated(
                CreateStorageBoxSnapshotResponse, CREATE_STORAGE_BOX_SNAPSHOT_RESPONSE
            )
            assert hash(result) == hash(
                validated(CreateStorageBoxSnapshotResponse, CREATE_STORAGE_BOX_SNAPSHOT_RESPONSE)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/snapshots"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_storage_box_snapshots_get_storage_box_snapshot() -> None:
    recorder = Recorder(200, SNAPSHOT_RESPONSE)
    with sync_client(recorder) as client:
        result = client.storage_box_snapshots.get_storage_box_snapshot(42, 42)
        assert result == validated(SnapshotResponse, SNAPSHOT_RESPONSE)
        assert hash(result) == hash(validated(SnapshotResponse, SNAPSHOT_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/snapshots/42"


def test_async_storage_box_snapshots_get_storage_box_snapshot() -> None:
    recorder = Recorder(200, SNAPSHOT_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_box_snapshots.get_storage_box_snapshot(42, 42)
            assert result == validated(SnapshotResponse, SNAPSHOT_RESPONSE)
            assert hash(result) == hash(validated(SnapshotResponse, SNAPSHOT_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/snapshots/42"


def test_storage_box_snapshots_update_storage_box_snapshot() -> None:
    recorder = Recorder(200, SNAPSHOT_RESPONSE)
    with sync_client(recorder) as client:
        result = client.storage_box_snapshots.update_storage_box_snapshot(42, 42)
        assert result == validated(SnapshotResponse, SNAPSHOT_RESPONSE)
        assert hash(result) == hash(validated(SnapshotResponse, SNAPSHOT_RESPONSE))
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/snapshots/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_async_storage_box_snapshots_update_storage_box_snapshot() -> None:
    recorder = Recorder(200, SNAPSHOT_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_box_snapshots.update_storage_box_snapshot(42, 42)
            assert result == validated(SnapshotResponse, SNAPSHOT_RESPONSE)
            assert hash(result) == hash(validated(SnapshotResponse, SNAPSHOT_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/snapshots/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_storage_box_snapshots_delete_storage_box_snapshot() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.storage_box_snapshots.delete_storage_box_snapshot(42, 42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/snapshots/42"


def test_async_storage_box_snapshots_delete_storage_box_snapshot() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_box_snapshots.delete_storage_box_snapshot(42, 42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/snapshots/42"

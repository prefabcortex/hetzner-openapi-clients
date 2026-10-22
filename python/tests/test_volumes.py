"""Generated tests for ``volumes``."""

import asyncio

from hetzner_api.models import CreateVolumeResponse, ListVolumesResponse, VolumeResponse
from tests.payloads import CREATE_VOLUME_RESPONSE, LIST_VOLUMES_RESPONSE, VOLUME_RESPONSE
from tests.support import Recorder, async_client, json_of, sync_client, to_jsonable, validated


def test_volumes_list_volumes() -> None:
    recorder = Recorder(200, LIST_VOLUMES_RESPONSE)
    with sync_client(recorder) as client:
        result = client.volumes.list_volumes()
        assert result == validated(ListVolumesResponse, LIST_VOLUMES_RESPONSE)
        assert hash(result) == hash(validated(ListVolumesResponse, LIST_VOLUMES_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/volumes"


def test_async_volumes_list_volumes() -> None:
    recorder = Recorder(200, LIST_VOLUMES_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.volumes.list_volumes()
            assert result == validated(ListVolumesResponse, LIST_VOLUMES_RESPONSE)
            assert hash(result) == hash(validated(ListVolumesResponse, LIST_VOLUMES_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/volumes"


def test_volumes_create_volume() -> None:
    recorder = Recorder(200, CREATE_VOLUME_RESPONSE)
    with sync_client(recorder) as client:
        result = client.volumes.create_volume(size=42, name="databases-storage")
        assert result == validated(CreateVolumeResponse, CREATE_VOLUME_RESPONSE)
        assert hash(result) == hash(validated(CreateVolumeResponse, CREATE_VOLUME_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/volumes"
    assert json_of(request) == to_jsonable({"size": 42, "name": "databases-storage"})


def test_async_volumes_create_volume() -> None:
    recorder = Recorder(200, CREATE_VOLUME_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.volumes.create_volume(size=42, name="databases-storage")
            assert result == validated(CreateVolumeResponse, CREATE_VOLUME_RESPONSE)
            assert hash(result) == hash(validated(CreateVolumeResponse, CREATE_VOLUME_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/volumes"
    assert json_of(request) == to_jsonable({"size": 42, "name": "databases-storage"})


def test_volumes_get_volume() -> None:
    recorder = Recorder(200, VOLUME_RESPONSE)
    with sync_client(recorder) as client:
        result = client.volumes.get_volume(42)
        assert result == validated(VolumeResponse, VOLUME_RESPONSE)
        assert hash(result) == hash(validated(VolumeResponse, VOLUME_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/volumes/42"


def test_async_volumes_get_volume() -> None:
    recorder = Recorder(200, VOLUME_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.volumes.get_volume(42)
            assert result == validated(VolumeResponse, VOLUME_RESPONSE)
            assert hash(result) == hash(validated(VolumeResponse, VOLUME_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/volumes/42"


def test_volumes_update_volume() -> None:
    recorder = Recorder(200, VOLUME_RESPONSE)
    with sync_client(recorder) as client:
        result = client.volumes.update_volume(42)
        assert result == validated(VolumeResponse, VOLUME_RESPONSE)
        assert hash(result) == hash(validated(VolumeResponse, VOLUME_RESPONSE))
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/volumes/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_async_volumes_update_volume() -> None:
    recorder = Recorder(200, VOLUME_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.volumes.update_volume(42)
            assert result == validated(VolumeResponse, VOLUME_RESPONSE)
            assert hash(result) == hash(validated(VolumeResponse, VOLUME_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/volumes/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_volumes_delete_volume() -> None:
    recorder = Recorder(204, None)
    with sync_client(recorder) as client:
        client.volumes.delete_volume(42)
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/volumes/42"


def test_async_volumes_delete_volume() -> None:
    recorder = Recorder(204, None)

    async def run() -> None:
        async with async_client(recorder) as client:
            await client.volumes.delete_volume(42)

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/volumes/42"

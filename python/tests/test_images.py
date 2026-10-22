"""Generated tests for ``images``."""

import asyncio

from hetzner_api.models import ImageResponse, ListImagesResponse
from tests.payloads import IMAGE_RESPONSE, LIST_IMAGES_RESPONSE
from tests.support import Recorder, async_client, json_of, sync_client, to_jsonable, validated


def test_images_list_images() -> None:
    recorder = Recorder(200, LIST_IMAGES_RESPONSE)
    with sync_client(recorder) as client:
        result = client.images.list_images()
        assert result == validated(ListImagesResponse, LIST_IMAGES_RESPONSE)
        assert hash(result) == hash(validated(ListImagesResponse, LIST_IMAGES_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/images"


def test_async_images_list_images() -> None:
    recorder = Recorder(200, LIST_IMAGES_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.images.list_images()
            assert result == validated(ListImagesResponse, LIST_IMAGES_RESPONSE)
            assert hash(result) == hash(validated(ListImagesResponse, LIST_IMAGES_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/images"


def test_images_get_image() -> None:
    recorder = Recorder(200, IMAGE_RESPONSE)
    with sync_client(recorder) as client:
        result = client.images.get_image(42)
        assert result == validated(ImageResponse, IMAGE_RESPONSE)
        assert hash(result) == hash(validated(ImageResponse, IMAGE_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/images/42"


def test_async_images_get_image() -> None:
    recorder = Recorder(200, IMAGE_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.images.get_image(42)
            assert result == validated(ImageResponse, IMAGE_RESPONSE)
            assert hash(result) == hash(validated(ImageResponse, IMAGE_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/images/42"


def test_images_update_image() -> None:
    recorder = Recorder(200, IMAGE_RESPONSE)
    with sync_client(recorder) as client:
        result = client.images.update_image(42)
        assert result == validated(ImageResponse, IMAGE_RESPONSE)
        assert hash(result) == hash(validated(ImageResponse, IMAGE_RESPONSE))
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/images/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_async_images_update_image() -> None:
    recorder = Recorder(200, IMAGE_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.images.update_image(42)
            assert result == validated(ImageResponse, IMAGE_RESPONSE)
            assert hash(result) == hash(validated(ImageResponse, IMAGE_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/images/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_images_delete_image() -> None:
    recorder = Recorder(204, None)
    with sync_client(recorder) as client:
        client.images.delete_image(42)
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/images/42"


def test_async_images_delete_image() -> None:
    recorder = Recorder(204, None)

    async def run() -> None:
        async with async_client(recorder) as client:
            await client.images.delete_image(42)

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/images/42"

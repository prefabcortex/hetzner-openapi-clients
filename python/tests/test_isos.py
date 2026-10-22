"""Generated tests for ``isos``."""

import asyncio

from hetzner_api.models import GetIsoResponse, ListIsosResponse
from tests.payloads import GET_ISO_RESPONSE, LIST_ISOS_RESPONSE
from tests.support import Recorder, async_client, sync_client, validated


def test_isos_list_isos() -> None:
    recorder = Recorder(200, LIST_ISOS_RESPONSE)
    with sync_client(recorder) as client:
        result = client.isos.list_isos()
        assert result == validated(ListIsosResponse, LIST_ISOS_RESPONSE)
        assert hash(result) == hash(validated(ListIsosResponse, LIST_ISOS_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/isos"


def test_async_isos_list_isos() -> None:
    recorder = Recorder(200, LIST_ISOS_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.isos.list_isos()
            assert result == validated(ListIsosResponse, LIST_ISOS_RESPONSE)
            assert hash(result) == hash(validated(ListIsosResponse, LIST_ISOS_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/isos"


def test_isos_get_iso() -> None:
    recorder = Recorder(200, GET_ISO_RESPONSE)
    with sync_client(recorder) as client:
        result = client.isos.get_iso(42)
        assert result == validated(GetIsoResponse, GET_ISO_RESPONSE)
        assert hash(result) == hash(validated(GetIsoResponse, GET_ISO_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/isos/42"


def test_async_isos_get_iso() -> None:
    recorder = Recorder(200, GET_ISO_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.isos.get_iso(42)
            assert result == validated(GetIsoResponse, GET_ISO_RESPONSE)
            assert hash(result) == hash(validated(GetIsoResponse, GET_ISO_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/isos/42"

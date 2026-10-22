"""Generated tests for ``data_centers``."""

import asyncio

import pytest

from hetzner_api.models import GetDatacenterResponse, ListDatacentersResponse
from tests.payloads import GET_DATACENTER_RESPONSE, LIST_DATACENTERS_RESPONSE
from tests.support import Recorder, async_client, sync_client, validated


def test_data_centers_list_datacenters() -> None:
    recorder = Recorder(200, LIST_DATACENTERS_RESPONSE)
    with sync_client(recorder) as client:
        deprecated_method = client.data_centers.list_datacenters  # type: ignore[deprecated]  # pyright: ignore[reportDeprecated]
        with pytest.deprecated_call():
            result = deprecated_method()
        assert result == validated(ListDatacentersResponse, LIST_DATACENTERS_RESPONSE)
        assert hash(result) == hash(validated(ListDatacentersResponse, LIST_DATACENTERS_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/datacenters"


def test_async_data_centers_list_datacenters() -> None:
    recorder = Recorder(200, LIST_DATACENTERS_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            deprecated_method = client.data_centers.list_datacenters  # type: ignore[deprecated]  # pyright: ignore[reportDeprecated]
            with pytest.deprecated_call():
                result = await deprecated_method()
            assert result == validated(ListDatacentersResponse, LIST_DATACENTERS_RESPONSE)
            assert hash(result) == hash(
                validated(ListDatacentersResponse, LIST_DATACENTERS_RESPONSE)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/datacenters"


def test_data_centers_get_datacenter() -> None:
    recorder = Recorder(200, GET_DATACENTER_RESPONSE)
    with sync_client(recorder) as client:
        deprecated_method = client.data_centers.get_datacenter  # type: ignore[deprecated]  # pyright: ignore[reportDeprecated]
        with pytest.deprecated_call():
            result = deprecated_method(42)
        assert result == validated(GetDatacenterResponse, GET_DATACENTER_RESPONSE)
        assert hash(result) == hash(validated(GetDatacenterResponse, GET_DATACENTER_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/datacenters/42"


def test_async_data_centers_get_datacenter() -> None:
    recorder = Recorder(200, GET_DATACENTER_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            deprecated_method = client.data_centers.get_datacenter  # type: ignore[deprecated]  # pyright: ignore[reportDeprecated]
            with pytest.deprecated_call():
                result = await deprecated_method(42)
            assert result == validated(GetDatacenterResponse, GET_DATACENTER_RESPONSE)
            assert hash(result) == hash(validated(GetDatacenterResponse, GET_DATACENTER_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/datacenters/42"

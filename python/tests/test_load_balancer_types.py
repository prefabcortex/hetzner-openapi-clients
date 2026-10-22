"""Generated tests for ``load_balancer_types``."""

import asyncio

from hetzner_api.models import GetLoadBalancerTypeResponse, ListLoadBalancerTypesResponse
from tests.payloads import GET_LOAD_BALANCER_TYPE_RESPONSE, LIST_LOAD_BALANCER_TYPES_RESPONSE
from tests.support import Recorder, async_client, sync_client, validated


def test_load_balancer_types_list_load_balancer_types() -> None:
    recorder = Recorder(200, LIST_LOAD_BALANCER_TYPES_RESPONSE)
    with sync_client(recorder) as client:
        result = client.load_balancer_types.list_load_balancer_types()
        assert result == validated(ListLoadBalancerTypesResponse, LIST_LOAD_BALANCER_TYPES_RESPONSE)
        assert hash(result) == hash(
            validated(ListLoadBalancerTypesResponse, LIST_LOAD_BALANCER_TYPES_RESPONSE)
        )
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancer_types"


def test_async_load_balancer_types_list_load_balancer_types() -> None:
    recorder = Recorder(200, LIST_LOAD_BALANCER_TYPES_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.load_balancer_types.list_load_balancer_types()
            assert result == validated(
                ListLoadBalancerTypesResponse, LIST_LOAD_BALANCER_TYPES_RESPONSE
            )
            assert hash(result) == hash(
                validated(ListLoadBalancerTypesResponse, LIST_LOAD_BALANCER_TYPES_RESPONSE)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancer_types"


def test_load_balancer_types_get_load_balancer_type() -> None:
    recorder = Recorder(200, GET_LOAD_BALANCER_TYPE_RESPONSE)
    with sync_client(recorder) as client:
        result = client.load_balancer_types.get_load_balancer_type(42)
        assert result == validated(GetLoadBalancerTypeResponse, GET_LOAD_BALANCER_TYPE_RESPONSE)
        assert hash(result) == hash(
            validated(GetLoadBalancerTypeResponse, GET_LOAD_BALANCER_TYPE_RESPONSE)
        )
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancer_types/42"


def test_async_load_balancer_types_get_load_balancer_type() -> None:
    recorder = Recorder(200, GET_LOAD_BALANCER_TYPE_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.load_balancer_types.get_load_balancer_type(42)
            assert result == validated(GetLoadBalancerTypeResponse, GET_LOAD_BALANCER_TYPE_RESPONSE)
            assert hash(result) == hash(
                validated(GetLoadBalancerTypeResponse, GET_LOAD_BALANCER_TYPE_RESPONSE)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancer_types/42"

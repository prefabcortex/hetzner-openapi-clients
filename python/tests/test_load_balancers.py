"""Generated tests for ``load_balancers``."""

import asyncio

from hetzner_api.models import (
    ActionResponse,
    CreateLoadBalancerResponse,
    ListLoadBalancersResponse,
    LoadBalancerResponse,
    MetricsResponse,
)
from tests.payloads import (
    ACTION_RESPONSE,
    CREATE_LOAD_BALANCER_RESPONSE,
    LIST_LOAD_BALANCERS_RESPONSE,
    LOAD_BALANCER_RESPONSE,
    METRICS_RESPONSE,
)
from tests.support import Recorder, async_client, json_of, sync_client, to_jsonable, validated


def test_load_balancers_list_load_balancers() -> None:
    recorder = Recorder(200, LIST_LOAD_BALANCERS_RESPONSE)
    with sync_client(recorder) as client:
        result = client.load_balancers.list_load_balancers()
        assert result == validated(ListLoadBalancersResponse, LIST_LOAD_BALANCERS_RESPONSE)
        assert hash(result) == hash(
            validated(ListLoadBalancersResponse, LIST_LOAD_BALANCERS_RESPONSE)
        )
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers"


def test_async_load_balancers_list_load_balancers() -> None:
    recorder = Recorder(200, LIST_LOAD_BALANCERS_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.load_balancers.list_load_balancers()
            assert result == validated(ListLoadBalancersResponse, LIST_LOAD_BALANCERS_RESPONSE)
            assert hash(result) == hash(
                validated(ListLoadBalancersResponse, LIST_LOAD_BALANCERS_RESPONSE)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers"


def test_load_balancers_create_load_balancer() -> None:
    recorder = Recorder(200, CREATE_LOAD_BALANCER_RESPONSE)
    with sync_client(recorder) as client:
        result = client.load_balancers.create_load_balancer(
            name="Web Frontend", load_balancer_type="lb11"
        )
        assert result == validated(CreateLoadBalancerResponse, CREATE_LOAD_BALANCER_RESPONSE)
        assert hash(result) == hash(
            validated(CreateLoadBalancerResponse, CREATE_LOAD_BALANCER_RESPONSE)
        )
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers"
    assert json_of(request) == to_jsonable({"name": "Web Frontend", "load_balancer_type": "lb11"})


def test_async_load_balancers_create_load_balancer() -> None:
    recorder = Recorder(200, CREATE_LOAD_BALANCER_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.load_balancers.create_load_balancer(
                name="Web Frontend", load_balancer_type="lb11"
            )
            assert result == validated(CreateLoadBalancerResponse, CREATE_LOAD_BALANCER_RESPONSE)
            assert hash(result) == hash(
                validated(CreateLoadBalancerResponse, CREATE_LOAD_BALANCER_RESPONSE)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers"
    assert json_of(request) == to_jsonable({"name": "Web Frontend", "load_balancer_type": "lb11"})


def test_load_balancers_get_load_balancer() -> None:
    recorder = Recorder(200, LOAD_BALANCER_RESPONSE)
    with sync_client(recorder) as client:
        result = client.load_balancers.get_load_balancer(42)
        assert result == validated(LoadBalancerResponse, LOAD_BALANCER_RESPONSE)
        assert hash(result) == hash(validated(LoadBalancerResponse, LOAD_BALANCER_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42"


def test_async_load_balancers_get_load_balancer() -> None:
    recorder = Recorder(200, LOAD_BALANCER_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.load_balancers.get_load_balancer(42)
            assert result == validated(LoadBalancerResponse, LOAD_BALANCER_RESPONSE)
            assert hash(result) == hash(validated(LoadBalancerResponse, LOAD_BALANCER_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42"


def test_load_balancers_update_load_balancer() -> None:
    recorder = Recorder(200, LOAD_BALANCER_RESPONSE)
    with sync_client(recorder) as client:
        result = client.load_balancers.update_load_balancer(42)
        assert result == validated(LoadBalancerResponse, LOAD_BALANCER_RESPONSE)
        assert hash(result) == hash(validated(LoadBalancerResponse, LOAD_BALANCER_RESPONSE))
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_async_load_balancers_update_load_balancer() -> None:
    recorder = Recorder(200, LOAD_BALANCER_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.load_balancers.update_load_balancer(42)
            assert result == validated(LoadBalancerResponse, LOAD_BALANCER_RESPONSE)
            assert hash(result) == hash(validated(LoadBalancerResponse, LOAD_BALANCER_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_load_balancers_delete_load_balancer() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.load_balancers.delete_load_balancer(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42"


def test_async_load_balancers_delete_load_balancer() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.load_balancers.delete_load_balancer(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42"


def test_load_balancers_get_load_balancer_metrics() -> None:
    recorder = Recorder(200, METRICS_RESPONSE)
    with sync_client(recorder) as client:
        result = client.load_balancers.get_load_balancer_metrics(
            42, type=["open_connections"], start="example", end="example"
        )
        assert result == validated(MetricsResponse, METRICS_RESPONSE)
        assert hash(result) == hash(validated(MetricsResponse, METRICS_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/metrics"


def test_async_load_balancers_get_load_balancer_metrics() -> None:
    recorder = Recorder(200, METRICS_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.load_balancers.get_load_balancer_metrics(
                42, type=["open_connections"], start="example", end="example"
            )
            assert result == validated(MetricsResponse, METRICS_RESPONSE)
            assert hash(result) == hash(validated(MetricsResponse, METRICS_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/load_balancers/42/metrics"

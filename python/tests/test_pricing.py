"""Generated tests for ``pricing``."""

import asyncio

from hetzner_api.models import GetPricingResponse
from tests.payloads import GET_PRICING_RESPONSE
from tests.support import Recorder, async_client, sync_client, validated


def test_pricing_get_pricing() -> None:
    recorder = Recorder(200, GET_PRICING_RESPONSE)
    with sync_client(recorder) as client:
        result = client.pricing.get_pricing()
        assert result == validated(GetPricingResponse, GET_PRICING_RESPONSE)
        assert hash(result) == hash(validated(GetPricingResponse, GET_PRICING_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/pricing"


def test_async_pricing_get_pricing() -> None:
    recorder = Recorder(200, GET_PRICING_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.pricing.get_pricing()
            assert result == validated(GetPricingResponse, GET_PRICING_RESPONSE)
            assert hash(result) == hash(validated(GetPricingResponse, GET_PRICING_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/pricing"

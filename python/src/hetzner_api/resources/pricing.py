"""Resource ``pricing`` (generated - do not edit by hand)."""

from typing import Final

from hetzner_api._auth import Security
from hetzner_api._base_client import AsyncTransport, SyncTransport
from hetzner_api.errors import ErrorModels
from hetzner_api.models import ErrorResponse, GetPricingResponse

__all__ = [
    "AsyncPricingResource",
    "PricingResource",
]

_SECURITY_1: Final[Security] = (("APIToken",),)

_ERRORS_1: Final[ErrorModels] = {
    "4XX": ErrorResponse,
    "5XX": ErrorResponse,
}


class PricingResource:
    """Operations on ``pricing`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def get_pricing(self) -> GetPricingResponse:
        """Get all prices.

        Returns prices for all resources available on the platform. VAT and currency of the Project
        owner are used for calculations.

        Both net and gross prices are included in the response.

        ``GET /pricing``

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        response = self._transport.request(
            "GET",
            "/pricing",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(GetPricingResponse, response)


class AsyncPricingResource:
    """Operations on ``pricing`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def get_pricing(self) -> GetPricingResponse:
        """Get all prices.

        Returns prices for all resources available on the platform. VAT and currency of the Project
        owner are used for calculations.

        Both net and gross prices are included in the response.

        ``GET /pricing``

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        response = await self._transport.request(
            "GET",
            "/pricing",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(GetPricingResponse, response)

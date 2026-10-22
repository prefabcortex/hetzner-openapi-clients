"""Examples for ``pricing`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import GetPricingResponse


def pricing_get_pricing(client: Hetzner) -> GetPricingResponse:
    """Get all prices.

    ``GET /pricing``
    """
    return client.pricing.get_pricing()

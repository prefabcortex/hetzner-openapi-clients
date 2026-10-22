"""Examples for ``load_balancer_types`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import GetLoadBalancerTypeResponse, ListLoadBalancerTypesResponse


def load_balancer_types_list_load_balancer_types(client: Hetzner) -> ListLoadBalancerTypesResponse:
    """List Load Balancer Types.

    ``GET /load_balancer_types``

    Optional arguments: name, page, per_page.
    """
    return client.load_balancer_types.list_load_balancer_types()


def load_balancer_types_get_load_balancer_type(client: Hetzner) -> GetLoadBalancerTypeResponse:
    """Get a Load Balancer Type.

    ``GET /load_balancer_types/{id}``
    """
    return client.load_balancer_types.get_load_balancer_type(42)

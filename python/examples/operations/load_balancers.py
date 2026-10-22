"""Examples for ``load_balancers`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import (
    ActionResponse,
    CreateLoadBalancerResponse,
    ListLoadBalancersResponse,
    LoadBalancerResponse,
    MetricsResponse,
)


def load_balancers_list_load_balancers(client: Hetzner) -> ListLoadBalancersResponse:
    """List Load Balancers.

    ``GET /load_balancers``

    Optional arguments: sort, name, label_selector, page, per_page.
    """
    return client.load_balancers.list_load_balancers()


def load_balancers_create_load_balancer(client: Hetzner) -> CreateLoadBalancerResponse:
    """Create a Load Balancer.

    ``POST /load_balancers``

    Optional arguments: algorithm, services, targets, labels, public_interface, public_net, network,
    network_zone, location.
    """
    return client.load_balancers.create_load_balancer(
        name="Web Frontend", load_balancer_type="lb11"
    )


def load_balancers_get_load_balancer(client: Hetzner) -> LoadBalancerResponse:
    """Get a Load Balancer.

    ``GET /load_balancers/{id}``
    """
    return client.load_balancers.get_load_balancer(42)


def load_balancers_update_load_balancer(client: Hetzner) -> LoadBalancerResponse:
    """Update a Load Balancer.

    ``PUT /load_balancers/{id}``

    Optional arguments: name, labels.
    """
    return client.load_balancers.update_load_balancer(42)


def load_balancers_delete_load_balancer(client: Hetzner) -> ActionResponse:
    """Delete a Load Balancer.

    ``DELETE /load_balancers/{id}``
    """
    return client.load_balancers.delete_load_balancer(42)


def load_balancers_get_load_balancer_metrics(client: Hetzner) -> MetricsResponse:
    """Get Metrics for a LoadBalancer.

    ``GET /load_balancers/{id}/metrics``

    Optional arguments: step.
    """
    return client.load_balancers.get_load_balancer_metrics(
        42, type=["open_connections"], start="example", end="example"
    )

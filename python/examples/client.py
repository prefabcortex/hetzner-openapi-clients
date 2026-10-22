"""Creating and configuring the client (generated example - copy what you need)."""

import logging

import httpx2

from hetzner_api import Hetzner, HetznerError, NotFoundError, RetryPolicy


def basic() -> None:
    """The token comes from ``$HCLOUD_TOKEN``; ``with`` closes the connections at the end."""
    with Hetzner() as client:
        print(client.server_actions.get_servers_action(42))


def configured() -> Hetzner:
    """Timeouts, retries and additional headers for every request."""
    return Hetzner(
        timeout=10.0,  # seconds per request; None disables the timeout
        retry=RetryPolicy(max_retries=3, max_delay=30.0),
        headers={"X-Request-Source": "example"},
    )


def own_http_client() -> Hetzner:
    """Your own ``httpx2.Client`` - e.g. for a proxy or your own TLS settings."""
    http_client = httpx2.Client(proxy="http://proxy.example:3128", timeout=20.0)
    return Hetzner(http_client=http_client)


def with_logging() -> None:
    """Requests on ``DEBUG``, retries on ``INFO``, responses off the spec on ``WARNING``."""
    logging.basicConfig(format="%(asctime)s %(name)s %(levelname)s %(message)s")
    logging.getLogger("hetzner_api").setLevel(logging.DEBUG)
    with Hetzner() as client:
        client.server_actions.get_servers_action(42)


def handling_errors() -> None:
    """One exception per HTTP status; ``HetznerError`` catches everything the client raises."""
    with Hetzner() as client:
        try:
            print(client.server_actions.get_servers_action(42))
        except NotFoundError as error:
            print("not found:", error.status_code, error.error)
        except HetznerError as error:
            print("failed:", error)


if __name__ == "__main__":
    handling_errors()

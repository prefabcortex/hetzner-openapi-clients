"""Lax or strict: how closely the API is held to its spec (generated example).

Lax (the default) gets along with what the API sends: rules of the spec (``maxLength``,
``pattern`` …) are not checked, and a response that does not match the spec is still returned -
with a warning on the ``hetzner_api`` logger. Strict raises instead: use it to test an API
against its spec.
"""

from hetzner_api import Hetzner, RequestValidationError, ResponseValidationError


def strict() -> None:
    """Arguments are checked before sending, responses when they arrive."""
    with Hetzner(validation="strict") as client:
        try:
            print(client.server_actions.get_servers_action(42))
        except RequestValidationError as error:
            print("not sent:", error.problems)
        except ResponseValidationError as error:
            print("the response does not match the spec:", error.errors)


if __name__ == "__main__":
    strict()

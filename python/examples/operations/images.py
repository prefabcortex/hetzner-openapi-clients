"""Examples for ``images`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import ImageResponse, ListImagesResponse


def images_list_images(client: Hetzner) -> ListImagesResponse:
    """List Images.

    ``GET /images``

    Optional arguments: sort, type, status, bound_to, include_deprecated, name, label_selector,
    architecture, page, per_page.
    """
    return client.images.list_images()


def images_get_image(client: Hetzner) -> ImageResponse:
    """Get an Image.

    ``GET /images/{id}``
    """
    return client.images.get_image(42)


def images_update_image(client: Hetzner) -> ImageResponse:
    """Update an Image.

    ``PUT /images/{id}``

    Optional arguments: description, type, labels.
    """
    return client.images.update_image(42)


def images_delete_image(client: Hetzner) -> None:
    """Delete an Image.

    ``DELETE /images/{id}``
    """
    client.images.delete_image(42)

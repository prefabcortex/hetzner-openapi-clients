"""Examples for ``certificates`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import CertificateResponse, CertificatesResponse, CreateCertificateResponse


def certificates_list_certificates(client: Hetzner) -> CertificatesResponse:
    """List Certificates.

    ``GET /certificates``

    Optional arguments: sort, name, label_selector, type, page, per_page.
    """
    return client.certificates.list_certificates()


def certificates_create_certificate(client: Hetzner) -> CreateCertificateResponse:
    """Create a Certificate.

    ``POST /certificates``

    Optional arguments: labels, type, certificate, private_key, domain_names.
    """
    return client.certificates.create_certificate(name="my website cert")


def certificates_get_certificate(client: Hetzner) -> CertificateResponse:
    """Get a Certificate.

    ``GET /certificates/{id}``
    """
    return client.certificates.get_certificate(42)


def certificates_update_certificate(client: Hetzner) -> CertificateResponse:
    """Update a Certificate.

    ``PUT /certificates/{id}``

    Optional arguments: name, labels.
    """
    return client.certificates.update_certificate(42)


def certificates_delete_certificate(client: Hetzner) -> None:
    """Delete a Certificate.

    ``DELETE /certificates/{id}``
    """
    client.certificates.delete_certificate(42)

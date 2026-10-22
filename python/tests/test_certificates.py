"""Generated tests for ``certificates``."""

import asyncio

from hetzner_api.models import CertificateResponse, CertificatesResponse, CreateCertificateResponse
from tests.payloads import CERTIFICATE_RESPONSE, CERTIFICATES_RESPONSE, CREATE_CERTIFICATE_RESPONSE
from tests.support import Recorder, async_client, json_of, sync_client, to_jsonable, validated


def test_certificates_list_certificates() -> None:
    recorder = Recorder(200, CERTIFICATES_RESPONSE)
    with sync_client(recorder) as client:
        result = client.certificates.list_certificates()
        assert result == validated(CertificatesResponse, CERTIFICATES_RESPONSE)
        assert hash(result) == hash(validated(CertificatesResponse, CERTIFICATES_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/certificates"


def test_async_certificates_list_certificates() -> None:
    recorder = Recorder(200, CERTIFICATES_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.certificates.list_certificates()
            assert result == validated(CertificatesResponse, CERTIFICATES_RESPONSE)
            assert hash(result) == hash(validated(CertificatesResponse, CERTIFICATES_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/certificates"


def test_certificates_create_certificate() -> None:
    recorder = Recorder(200, CREATE_CERTIFICATE_RESPONSE)
    with sync_client(recorder) as client:
        result = client.certificates.create_certificate(name="my website cert")
        assert result == validated(CreateCertificateResponse, CREATE_CERTIFICATE_RESPONSE)
        assert hash(result) == hash(
            validated(CreateCertificateResponse, CREATE_CERTIFICATE_RESPONSE)
        )
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/certificates"
    assert json_of(request) == to_jsonable({"name": "my website cert"})


def test_async_certificates_create_certificate() -> None:
    recorder = Recorder(200, CREATE_CERTIFICATE_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.certificates.create_certificate(name="my website cert")
            assert result == validated(CreateCertificateResponse, CREATE_CERTIFICATE_RESPONSE)
            assert hash(result) == hash(
                validated(CreateCertificateResponse, CREATE_CERTIFICATE_RESPONSE)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/certificates"
    assert json_of(request) == to_jsonable({"name": "my website cert"})


def test_certificates_get_certificate() -> None:
    recorder = Recorder(200, CERTIFICATE_RESPONSE)
    with sync_client(recorder) as client:
        result = client.certificates.get_certificate(42)
        assert result == validated(CertificateResponse, CERTIFICATE_RESPONSE)
        assert hash(result) == hash(validated(CertificateResponse, CERTIFICATE_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/certificates/42"


def test_async_certificates_get_certificate() -> None:
    recorder = Recorder(200, CERTIFICATE_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.certificates.get_certificate(42)
            assert result == validated(CertificateResponse, CERTIFICATE_RESPONSE)
            assert hash(result) == hash(validated(CertificateResponse, CERTIFICATE_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/certificates/42"


def test_certificates_update_certificate() -> None:
    recorder = Recorder(200, CERTIFICATE_RESPONSE)
    with sync_client(recorder) as client:
        result = client.certificates.update_certificate(42)
        assert result == validated(CertificateResponse, CERTIFICATE_RESPONSE)
        assert hash(result) == hash(validated(CertificateResponse, CERTIFICATE_RESPONSE))
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/certificates/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_async_certificates_update_certificate() -> None:
    recorder = Recorder(200, CERTIFICATE_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.certificates.update_certificate(42)
            assert result == validated(CertificateResponse, CERTIFICATE_RESPONSE)
            assert hash(result) == hash(validated(CertificateResponse, CERTIFICATE_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/certificates/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_certificates_delete_certificate() -> None:
    recorder = Recorder(204, None)
    with sync_client(recorder) as client:
        client.certificates.delete_certificate(42)
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/certificates/42"


def test_async_certificates_delete_certificate() -> None:
    recorder = Recorder(204, None)

    async def run() -> None:
        async with async_client(recorder) as client:
            await client.certificates.delete_certificate(42)

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/certificates/42"

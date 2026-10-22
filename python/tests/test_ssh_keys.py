"""Generated tests for ``ssh_keys``."""

import asyncio

from hetzner_api.models import ListSshKeysResponse, SshKeyResponse
from tests.payloads import LIST_SSH_KEYS_RESPONSE, SSH_KEY_RESPONSE
from tests.support import Recorder, async_client, json_of, sync_client, to_jsonable, validated


def test_ssh_keys_list_ssh_keys() -> None:
    recorder = Recorder(200, LIST_SSH_KEYS_RESPONSE)
    with sync_client(recorder) as client:
        result = client.ssh_keys.list_ssh_keys()
        assert result == validated(ListSshKeysResponse, LIST_SSH_KEYS_RESPONSE)
        assert hash(result) == hash(validated(ListSshKeysResponse, LIST_SSH_KEYS_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/ssh_keys"


def test_async_ssh_keys_list_ssh_keys() -> None:
    recorder = Recorder(200, LIST_SSH_KEYS_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.ssh_keys.list_ssh_keys()
            assert result == validated(ListSshKeysResponse, LIST_SSH_KEYS_RESPONSE)
            assert hash(result) == hash(validated(ListSshKeysResponse, LIST_SSH_KEYS_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/ssh_keys"


def test_ssh_keys_create_ssh_key() -> None:
    recorder = Recorder(200, SSH_KEY_RESPONSE)
    with sync_client(recorder) as client:
        result = client.ssh_keys.create_ssh_key(
            name="My ssh key", public_key="ssh-rsa AAAjjk76kgf...Xt"
        )
        assert result == validated(SshKeyResponse, SSH_KEY_RESPONSE)
        assert hash(result) == hash(validated(SshKeyResponse, SSH_KEY_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/ssh_keys"
    assert json_of(request) == to_jsonable(
        {"name": "My ssh key", "public_key": "ssh-rsa AAAjjk76kgf...Xt"}
    )


def test_async_ssh_keys_create_ssh_key() -> None:
    recorder = Recorder(200, SSH_KEY_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.ssh_keys.create_ssh_key(
                name="My ssh key", public_key="ssh-rsa AAAjjk76kgf...Xt"
            )
            assert result == validated(SshKeyResponse, SSH_KEY_RESPONSE)
            assert hash(result) == hash(validated(SshKeyResponse, SSH_KEY_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/ssh_keys"
    assert json_of(request) == to_jsonable(
        {"name": "My ssh key", "public_key": "ssh-rsa AAAjjk76kgf...Xt"}
    )


def test_ssh_keys_get_ssh_key() -> None:
    recorder = Recorder(200, SSH_KEY_RESPONSE)
    with sync_client(recorder) as client:
        result = client.ssh_keys.get_ssh_key(42)
        assert result == validated(SshKeyResponse, SSH_KEY_RESPONSE)
        assert hash(result) == hash(validated(SshKeyResponse, SSH_KEY_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/ssh_keys/42"


def test_async_ssh_keys_get_ssh_key() -> None:
    recorder = Recorder(200, SSH_KEY_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.ssh_keys.get_ssh_key(42)
            assert result == validated(SshKeyResponse, SSH_KEY_RESPONSE)
            assert hash(result) == hash(validated(SshKeyResponse, SSH_KEY_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/ssh_keys/42"


def test_ssh_keys_update_ssh_key() -> None:
    recorder = Recorder(200, SSH_KEY_RESPONSE)
    with sync_client(recorder) as client:
        result = client.ssh_keys.update_ssh_key(42)
        assert result == validated(SshKeyResponse, SSH_KEY_RESPONSE)
        assert hash(result) == hash(validated(SshKeyResponse, SSH_KEY_RESPONSE))
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/ssh_keys/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_async_ssh_keys_update_ssh_key() -> None:
    recorder = Recorder(200, SSH_KEY_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.ssh_keys.update_ssh_key(42)
            assert result == validated(SshKeyResponse, SSH_KEY_RESPONSE)
            assert hash(result) == hash(validated(SshKeyResponse, SSH_KEY_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/ssh_keys/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_ssh_keys_delete_ssh_key() -> None:
    recorder = Recorder(204, None)
    with sync_client(recorder) as client:
        client.ssh_keys.delete_ssh_key(42)
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/ssh_keys/42"


def test_async_ssh_keys_delete_ssh_key() -> None:
    recorder = Recorder(204, None)

    async def run() -> None:
        async with async_client(recorder) as client:
            await client.ssh_keys.delete_ssh_key(42)

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/ssh_keys/42"

"""The async client: the same API with ``async``/``await`` (generated example)."""

import asyncio

from hetzner_api import AsyncHetzner


async def main() -> None:
    """Every method is awaited."""
    async with AsyncHetzner() as client:
        print(await client.server_actions.get_servers_action(42))


async def concurrently(ids: list[int]) -> None:
    """Several requests at once with ``asyncio.gather``."""
    async with AsyncHetzner() as client:
        for found in await asyncio.gather(
            *(client.server_actions.get_servers_action(each) for each in ids)
        ):
            print(found)


if __name__ == "__main__":
    asyncio.run(main())

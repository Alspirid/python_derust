import asyncio


async def greet(name: str) -> str:
    await asyncio.sleep(1)
    return f"greeting {name}"


async def main() -> list[str]:
    return list(await asyncio.gather(greet("Sam"), greet("John"), greet("Alex")))


asyncio.run(main())
# → ["Hello, a", "Hello, b", "Hello, c"]   in ~1 second total, not 3

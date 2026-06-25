import asyncio


async def fetch(item: int) -> int:
    await asyncio.sleep(0.1)  # pretend I/O
    return item * 2


async def process_all(items: list[int], limit: int):
    sem = asyncio.Semaphore(limit)

    async def process_with_limit(item: int) -> int:
        async with sem:
            return await fetch(item)

    return await asyncio.gather(*(process_with_limit(item) for item in items))


result = asyncio.run(process_all([1, 2, 3, 4, 5], limit=2))
print(result)
# → [2, 4, 6, 8, 10]   — at most 2 fetches running at any instant

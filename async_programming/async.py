import asyncio

async def task(name):
    print(f"{name}: step 1")
    await asyncio.sleep(1)
    print(f"{name}: step 2")
    await asyncio.sleep(1)
    print(f"{name}: step 3")

async def main():
    await asyncio.gather(
        task("A"),
        task("B")
    )

asyncio.run(main())

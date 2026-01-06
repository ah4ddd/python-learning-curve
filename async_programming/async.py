import asyncio

async def task():
    await asyncio.sleep(2)
    print("done")

async def main():
    await asyncio.gather(task(), task())

asyncio.run(main())

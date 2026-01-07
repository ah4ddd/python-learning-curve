import asyncio

async def handle_request(user_id):
    print(f"Handling user {user_id}")
    await asyncio.sleep(3)   # simulates DB / network wait
    print(f"Finished user {user_id}")

async def main():
    print("Server started")

    await asyncio.gather(
        handle_request(1),
        handle_request(2),
        handle_request(3),
    )

    print("Server shutting down")

asyncio.run(main())

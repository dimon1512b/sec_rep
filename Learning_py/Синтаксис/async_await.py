import asyncio

async def async_task():
    print("Start of async_task")
    await asyncio.sleep(5)
    print("End of async_task")

async def main():
    print("Start of main")
    await asyncio.gather(
        async_task(),
        other_async_task()
    )
    print("End of main")

async def other_async_task():
    print("Start of other_async_task")
    await asyncio.sleep(2)
    print("End of other_async_task")

asyncio.run(main())

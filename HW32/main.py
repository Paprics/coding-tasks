import asyncio
import aiohttp


async def make_request(session, name):
    await session.get("https://httpbin.org/delay/2")
    print(f"{name}: запрос завершён")


async def future_waiter(name, fut):
    result = await fut
    print(f"{name}: получил future: {result}")


async def future_setter(fut, value):
    fut.set_result(value)
    print(f"Future установлено: {value}")


async def main():
    fut1 = asyncio.Future()
    fut2 = asyncio.Future()

    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            make_request(session, "Корутина 1"),
            make_request(session, "Корутина 2"),
            future_waiter("Корутина 3", fut1),
            future_waiter("Корутина 4", fut2),
            future_setter(fut1, "готово 1"),
            future_setter(fut2, "готово 2"),
        )

if __name__ == "__main__":
    asyncio.run(main())

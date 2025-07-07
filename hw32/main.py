import asyncio
import aiohttp

async def coroutine_1(session):
    async with session.get("https://httpbin.org/delay/1") as resp:
        await resp.text()
    print("Корутина 1: запит завершено")
    return "Результат coroutine_1"

async def coroutine_2(session):
    async with session.get("https://httpbin.org/delay/2") as resp:
        await resp.text()
    print("Корутина 2: запит завершено")
    return "Результат coroutine_2"

async def coroutine_3(session):
    async with session.get("https://httpbin.org/delay/3") as resp:
        await resp.text()
    print("Корутина 3: запит завершено")
    return "Результат coroutine_3"

async def coroutine_4(session):
    async with session.get("https://httpbin.org/delay/4") as resp:
        await resp.text()
    print("Корутина 4: запит завершено")
    return "Результат coroutine_4"

async def coroutine_5(session):
    async with session.get("https://httpbin.org/delay/5") as resp:
        await resp.text()
    print("Корутина 5: запит завершено")
    return "Результат coroutine_5"

async def coroutine_6(session):
    async with session.get("https://httpbin.org/delay/6") as resp:
        await resp.text()
    print("Корутина 6: запит завершено")
    return "Результат coroutine_6"

async def waiter_1(tasks):
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    done2, _ = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
    done.update(done2)
    results = [await task for task in done]
    print(f"Корутина 7: отримала результати: {results}")

async def waiter_2(tasks):
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    done2, _ = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
    done.update(done2)
    results = [await task for task in done]
    print(f"Корутина 8: отримала результати: {results}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(coroutine_1(session)),
            asyncio.create_task(coroutine_2(session)),
            asyncio.create_task(coroutine_3(session)),
            asyncio.create_task(coroutine_4(session)),
            asyncio.create_task(coroutine_5(session)),
            asyncio.create_task(coroutine_6(session)),
        ]

        await asyncio.gather(
            *tasks,
            waiter_1(tasks),
            waiter_2(tasks),
        )

if __name__ == "__main__":
    asyncio.run(main())

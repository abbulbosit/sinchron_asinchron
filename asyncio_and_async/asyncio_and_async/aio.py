import asyncio
from datetime import datetime

async def task1():
    await asyncio.sleep(2)
    print("Task 1 completed")

async def task2():
    await asyncio.sleep(2)
    print("Task 2 completed")

async def task3():
    await asyncio.sleep(2)
    print("Task 3 completed")

async def task4():
    await asyncio.sleep(2)
    print("Task 4 completed")

async def task5():
    await asyncio.sleep(2)
    print("Task 5 completed")

async def task6():
    await asyncio.sleep(2)
    print("Task 6 completed")

async def task7():
    await asyncio.sleep(2)
    print("Task 7 completed")

async def task8():
    await asyncio.sleep(2)
    print("Task 8 completed")

async def tasks():
    print(datetime.now())
    await asyncio.gather(task1(), task2(), task3(), task4(), task5(), task6(), task7(), task8())
    print(datetime.now())


if __name__ == "__main__":
    asyncio.run(tasks())
# -*- coding: utf-8 -*-
import asyncio


'''
    Python 3.4     |     Python 3.5     |     Python 3.6     |     Python 3.7

@asyncio.coroutine |                            async

    yield from     |                            await

                        ensure_future()                      |    create_task()

                loop = asyncio.get_event_loop()              |
                loop.run_until_complete(main())              |    asyncio.run()
                loop.close()                                 |
'''
async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(0.1)


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print('{} seconds have passed'.format(count))
        count += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())

    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()
    asyncio.run(main())
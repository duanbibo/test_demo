import asyncio
import time
import requests
import aiohttp
from concurrent.futures import ThreadPoolExecutor


NUMBERS = range(12)
URL = 'http://httpbin.org/get?a={}'

async def fetch(a):
    async with aiohttp.request('GET', URL.format(a)) as r:
        data = await r.json()
    return data['args']['a']

async def run_scraper_tasks(executor):
    loop = asyncio.get_event_loop()

    blocking_tasks = []
    for num in NUMBERS:
        task = loop.run_in_executor(executor, fetch, num)
        task.__num = num
        blocking_tasks.append(task)

    completed, pending = await asyncio.wait(blocking_tasks)

    results = {t.__num: t.result() for t in completed}
    for num, result in sorted(results.items(), key=lambda x: x[0]):
        print('fetch({}) = {}'.format(num, result))

start = time.time()
executor = ThreadPoolExecutor(3)
event_loop = asyncio.get_event_loop()

event_loop.run_until_complete(
    run_scraper_tasks(executor)
)

print('Use asyncio+requests+ThreadPoolExecutor cost: {}'.format(time.time() - start))


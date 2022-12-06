import os.path
import time
import asyncio
import aiohttp
import aiofiles

"""
Event loop object it is thread
"""

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

amount_images = 10

size = {
    'width': 1920,
    'height': 1080
}
size_to_str = f'{size["width"]}/{size["height"]}'
url = f'https://loremflickr.com/{size_to_str}'

if not os.path.exists('images'):
    os.mkdir('images')


async def download_image(link, session, num):
    async with session.get(link) as resp:
        if resp.status == 200:
            file_name = f'{size_to_str.replace("/", "x")}_{num}.jpg'
            folder = os.path.join('images', file_name)
            f = await aiofiles.open(folder, mode='wb')
            await f.write(await resp.read())
            await f.close()
            print(f'{file_name} ready')


async def main(link, amount):
    print('START DOWNLOADING')
    start = time.monotonic()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(amount):
            task = asyncio.create_task(download_image(link, session, i + 1))
            tasks.append(task)
        await asyncio.gather(*tasks)
        print(f'FINISH DOWNLOADING - {time.monotonic() - start} sec')


async def a_def_1():
    pass


async def a_def_2():
    pass


async def a_def_3():
    pass


def run_as_imported():
    asyncio.run(main(url, amount_images))


if __name__ == '__main__':
    asyncio.run(main(url, amount_images))

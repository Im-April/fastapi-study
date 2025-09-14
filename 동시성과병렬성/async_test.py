# 간단한 비동기 함수

import asyncio

async def hello():
    print('인녕하세요')
    await asyncio.sleep(1)
    print('잘 가세요')

asyncio.run(hello())
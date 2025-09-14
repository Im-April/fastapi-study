import asyncio
import time

# 동기 방식 - 순차적 실행
def sync_task(name, delay):
    print(f"{name} 시작")
    time.sleep(delay)
    print(f"{name} 완료")

def run_sync():
    start = time.time()
    sync_task("작업1", 2)
    sync_task("작업2", 1)
    sync_task("작업3", 1)
    print(f"동기 실행 시간: {time.time() - start:.2f}초")

# 비동기 방식 - 동시 실행
async def async_task(name, delay):
    print(f"{name} 시작")
    await asyncio.sleep(delay)
    print(f"{name} 완료")

async def run_async():
    start = time.time()
    await asyncio.gather(
        async_task("작업1", 2),
        async_task("작업2", 1),
        async_task("작업3", 1)
    )
    print(f"비동기 실행 시간: {time.time() - start:.2f}초")

# 실행
run_sync() 
asyncio.run(run_async())  
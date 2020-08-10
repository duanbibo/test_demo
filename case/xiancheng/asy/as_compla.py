import asyncio
import time


async def foo(n):
      print('Waiting: ', n)
      await asyncio.sleep(n)
      return n
def call(task):
      ''' 单个任务的回调'''
      return ("协程回调完毕{}".format(task))

def endcall(loop):
      print("所有任务执行完毕")
      loop.stop()


async def main():
      coroutine1 = foo(1)
      coroutine2 = foo(2)
      coroutine3 = foo(4)

      tasks = [
            asyncio.ensure_future(coroutine1),
            asyncio.ensure_future(coroutine2),
            asyncio.ensure_future(coroutine3)
      ]
      for task in asyncio.as_completed(tasks):
            result = await task
            huidiao    = call(result)
            print('Task ret: {}'.format(result),"huidiao:{}".format(huidiao))


now = lambda: time.time()
start = now()

loop = asyncio.get_event_loop()
done = loop.run_until_complete(main())


loop.call_soon(endcall(loop))
print(now() - start)
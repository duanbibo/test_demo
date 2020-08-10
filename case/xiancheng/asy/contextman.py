import asyncio




#声明异步的上下文
class Sync():

      async def __aenter__(self):
            print("开始了")
            return self

      async def __aexit__(self, exc_type, exc_val, exc_tb):
            # 退出async with的时候，任务列表中的任务进行并发操作。
            #self.finished = await asyncio.gather(*self.pending, return_exceptions=True)
            print("退出了")
'''
使用异步的上下文管理器
'''

async def contextm():
      print("1")
      #使用异步的上下文管理器
      async with Sync() as s:
            print("内部")

loop=asyncio.get_event_loop()
loop.run_until_complete(contextm())
loop.close()
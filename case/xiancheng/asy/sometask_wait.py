import asyncio
import time

async def other():
      print("other：其他协程内执行")
      return "other"


async def task1():
      print("task1")
      print(time.time(),"before1 sleep4秒准备")
      await asyncio.sleep(2)
      print(time.time(),"sleep2秒after1")
      print("task1 over")

async def task2():
      print("task2  start2调用其他协程")
      c=asyncio.ensure_future(other())
      await asyncio.sleep(4)
      print("task2  after4秒")
      return "task2 获取其他协程结果 %s"%c

loop=asyncio.get_event_loop()
tasks=[task1(),task2()]
print(time.time())
tasksult=loop.run_until_complete(asyncio.wait(tasks))
print(tasksult[0],"批量执行task结束")
loop.close()


#执行结果  ：先按照加入的task队列进行执行，在执行task1的时候，遇见await/yiled from 语句 进入协程内部执行
           #同时，将执行权交给主线程，线程开始执行其他的异步函数。在
# task1
# task2
# task2 after
# task1 after

import asyncio


async def  do(a):
      print("执行异步任务,计算参数的平方")
      await asyncio.sleep(3)
      return a**2


def  call(a):
      #print("task 执行over",a)
      return "计算结果为{}".format(a)

async def a(r):
      response=await  do(r)
      huidiao=call(response)
      return  huidiao


#pars=[1,2,3,4,5,6,7]
loop=asyncio.get_event_loop()
task=loop.run_until_complete(a(4))
print(task)
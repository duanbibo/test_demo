import asyncio
from asyncio import  FIRST_COMPLETED

class  A:
      '''协程内多个task，不影响变量'''

      def __init__(self):
            self.total=0

      async def add(self):
            for i in range(10**7):
                  self.total+=1
a=A()

task=[a.add(),a.add()]
loop=asyncio.get_event_loop()

#使用asyncio.wait(task-list) 返回值为2个set集合，第一个为完成的，第二个为未完成的
f1,f2=loop.run_until_complete(asyncio.wait(task))
#ga=loop.run_until_complete(asyncio.gather(a.add(),a.add()))
loop.close()

print(a.total)#多个协程任务，每个协程执行10**7 次
#print(ga)


#print(f1,f2)
#遍历已完成的集合
# a=1
# for i in f1:
#       print("协程{}执行结果:".format(a),i.result())
#       a+=1
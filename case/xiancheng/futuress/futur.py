

from concurrent.futures import ThreadPoolExecutor,as_completed

import requests
import time

from  case.xiancheng.futuress.task import huidiao
''' 单个函数和单个迭代对象：submit
    利用concurren.funtures模块的线程池/进程池执行器，传入最大的数，控制并发的数量，进行实例化对象。
    实例化对象调用内部的方法 submit (需要执行的函数，函数对应的参数)进行并发请求，返回一个实例化future对象。
    
    

'''
def load_url(url):
      time.sleep(5)
      return requests.get(url)
url="http://httpbin.org"

excecutor=ThreadPoolExecutor(max_workers=1)
future=excecutor.submit(load_url,url)

def  over(xx):
      print(xx,"success")

#根据future对象，调用回调函数，执行完毕后调用其他函数。future.add_done_callback(func)
future.add_done_callback(over)  #回调函数，将futuer当做参数值，传入某个函数中

future.done()  #返回布尔值类型，任务是否结束,这个是非阻塞的。直接会输出值。

print("任务是否结束：",future.done())  #

print( "执行结果；",future.result())        #阻塞的，任务执行完毕后才有返回值。

print(future.result().status_code)




print("---------------单个函数，多个参数，map执行：zip(迭代参数，map(函数，迭代参数))")

urs=["http://www.baidu.com","http://www.qq.com","http://www.sina.com.cn"]
with ThreadPoolExecutor(max_workers=3) as excecutor:
   for url ,data in zip(urs,excecutor.map(load_url,urs)):

     print( "执行结果；",(url,data.status_code))



print("---------------单个函数，多个参数，"
      "借助future实例的submit方法和as_completed函数执行，"
      "先将列表中的多个任务依次进行submit,然后返回个可迭代对象，"
      "将这个可迭代对象放入as_completed函数中依次执行，他的future实例的result方法是不阻塞的")

import os
print(os.cpu_count()),

with ThreadPoolExecutor(max_workers=3) as excecutor:
      tasks=[excecutor.submit(load_url,u)for u in urs]
      for future_as in as_completed(tasks):
            print("查看是否结束:",future_as.done())
            print("查看任务执行结果:",future_as.result(),"查看回调情况：",future_as.add_done_callback(huidiao))




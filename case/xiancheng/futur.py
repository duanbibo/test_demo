

from concurrent.futures import ThreadPoolExecutor,as_completed
import requests
''' 单个函数和单个迭代对象：submit'''
def load_url(url):
      return requests.get(url)
url="http://httpbin.org"

excecutor=ThreadPoolExecutor(max_workers=1)
future=excecutor.submit(load_url,url)

def  over(xx):
      print(xx,"success")

future.add_done_callback(over)  #回调函数，将futuer当做参数值，传入某个函数中

print( "执行结果；",future.result(),"任务是否成功",future.done(),future.result().status_code)

print("---------------单个函数，多个参数map执行：zip(迭代参数，map(函数，迭代参数))")
urs=["http://www.baidu.com","http://www.qq.com","http://www.sina.com.cn"]
with ThreadPoolExecutor(max_workers=3) as excecutor:
   for url ,data in zip(urs,excecutor.map(load_url,urs)):
     print( "执行结果；",(url,data.status_code))

print("---------------单个函数，多个参数as_completed执行，实际"
      "先将列表中的多个任务依次进行submit,然后返回个可迭代对象，"
      "将这个可迭代对象放入as_completed函数中依次执行")


with ThreadPoolExecutor(max_workers=3) as excecutor:
      tasks=[excecutor.submit(load_url,u)for u in urs]
      for future_as in as_completed(tasks):
            print(future_as.result())



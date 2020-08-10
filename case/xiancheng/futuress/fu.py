from concurrent import futures
import time
from concurrent.futures import as_completed

from  case.xiancheng.futuress.task import func1,func2,huidiao

litask=[func1,func2]

times=[1,2,3,4,5,6,7]

#单个函数单次运行
def work_future():
         exec= futures.ThreadPoolExecutor(max_workers=3)
         future=exec.submit(func1,5)
         print("result:", future.result(timeout=18))
         #print(future.done())#
         future.add_done_callback(huidiao)




#每个函数里面都有个sleep语句，如果不进行并发的时候，那么执行10次，将耗时 1+2，，+10秒
#使用map有弊端，返回的结果会按照调用顺序返回，执行快的会被阻塞。加入第一个执行未完毕，后面的执行结束了就必须等到第一个才有有result
def work_future_somemap():
   with futures.ThreadPoolExecutor(max_workers=4)as exec:
     for num,result in zip(times,exec.map(func1,times,chunksize=len(times))):
           print( "参数：",num ,";返回结果：",result,"现在时间：",time.time())




#使用submit方法和as_completed函数
def work_future_completed():
     with futures.ThreadPoolExecutor(max_workers=4) as executor:
           task=[executor.submit(func1,one) for one in times]
           for future in as_completed(task):

                 print("resulf():",future.result,";done():",future.done())



if __name__ == '__main__':
    print(time.time(), "首次执行4个线程时间")
    #单个函数运行一次
    #work_future()


    #使用map批量并发,这个是阻塞的
    work_future_somemap()

    #使用exec的submit提交单个和future的as_complated函数
    #work_future_completed()



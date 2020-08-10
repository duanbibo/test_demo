from concurrent.futures import ThreadPoolExecutor,as_completed
from collections import ChainMap
from itertools import chain

from case.xiancheng.futuress.task import func1,func2 ,huidiao

r=range(1,4)
daoxu=(4,3,1)




def  future_sumbit_completed():

      with ThreadPoolExecutor(max_workers=3) as executor:
            #创建一个字典用来接收多个函数和他们的参数
            #
            # future_num={executor.submit(func1,num):num for num in daoxu}
            # funture2_num={executor.submit(func2,num):num for num in r}

            #不能直接用list将不同的迭代对象放入里面，可以使用chainmap或者chain ,将生成器对象连接

            future_num=[executor.submit(func1,num) for num in daoxu]
            funture2_num=[executor.submit(func2,num) for num in r]
            chainmap=chain(future_num,funture2_num)

            #chainmap=ChainMap(future_num,funture2_num)

            for future in as_completed(chainmap):
                  print("查看是否结束:", future.done())
                  print("查看任务执行结果:", future.result(),
                        "查看回调情况：", future.add_done_callback(huidiao))


if __name__ == '__main__':
    future_sumbit_completed()
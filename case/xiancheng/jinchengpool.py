from multiprocessing import Pool
from multiprocessing import Process
import time
def run():
      while True:
            for i in range (1,3):
                 start=time.time()
                 print("子线程%s出来了"%(i))
                 time.sleep(i)
                 end=time.time()
                 zhixing=end-start
                 print("子进程%s关闭了%f"%(i,zhixing))


if __name__ == '__main__':
      '''
       创建容量为2的进程池，每次启动3个进程。
       预期结果：前2个线程并行执行，
      '''
      print("父进程启动---不参与计数")
      pp=Pool(2)
      for i in range(3):
            pp.apply_async(run)
      pp.close()
      pp.join()

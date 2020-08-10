import multiprocessing
import threading
import  os
import time

''' 使用多进程
    获取进程ID ，利用OS模块的 os.getpid 
       父进程ID   os.getppid
'''


def run(i):
      ''' 创建进程的函数'''
      print("进程%s"%i)
      time.sleep(1)
      for n in range(2):
            t=threading.Thread(target=thred_run,args=(i,n))
            t.start()

def thred_run(i,n):
      ''' 线程实体运行的值，在内部调用进程的传参数'''
      print("在进程%s 的线程%s，进程ID是%s"%(i,n,os.getpid()))


if __name__ == '__main__':
    for i in range(4):
          p=multiprocessing.Process(target=run,args=(i,))

          p.start()
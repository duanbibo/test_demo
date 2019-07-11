from multiprocessing import Process
import time
import os

number=8
def run():
      while True:
            print("子线程2出来了,%s,%s"%(os.getpid(),os.getppid()))

            time.sleep(1)

if __name__ == '__main__':

      print("我先启动的，我线程是,%s," %(os.getpid()))
      print(number)
      p = Process(target=run)

      p.start()

      while True:
            print("母线程1出来了,%s,%s"%(os.getpid(),os.getppid()))
            print(number)
            time.sleep(3)
            run()



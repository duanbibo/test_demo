
import threading
import time

class myThread(threading.Thread):


      def __init__(self,name,counter):
            threading.Thread.__init__(self)
            self.name=name
            self.counter=counter



      def run(self):
            global n
            threadLock.acquire()

            threadLock.release()

threads=[]
threadLock = threading.Lock()
#
m = myThread("线程1", 1)
m2 = myThread("线程2", 2)
m.start()
m2.start()
threads.append(m)
threads.append(m2)
for t in threads:
      t.join()
print("结束运行")
print(threads)






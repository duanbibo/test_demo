from threading import Thread,Lock
import threading,time
class MyThread(Thread):
    def run(self):
        if mylock.acquire():
            try:
              print("第一个线程的锁已经开动，并且我已经进入%s"%threading.current_thread().name)
              time.sleep(1)
            finally:
               mylock.release()
               try:
                 if mylock2.acquire(2):
                     print("等待第二个的锁开开")
               finally:
                  mylock2.release()

class MyThread2(Thread):

    def run(self):
        if mylock2.acquire():
            try:
               print("第2个线程的锁已经开动，并且我已经进入%s"%threading.current_thread().name)
               time.sleep(1)
            finally:
                  mylock2.release()
                  try:
                    if mylock.acquire(2):
                       print("等待第一个的锁开开")
                  finally:
                     mylock.release()

mylock = Lock()
mylock2 = Lock()
p1=MyThread()
p2=MyThread2()
p1.start()
p2.start()

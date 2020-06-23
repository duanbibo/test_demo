

import threading,time
from random import randint
class Producer(threading.Thread):
    def run(self):
        global L
        while True:
            val=randint(0,100)
            # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            print('生产者',self.name,' Append'+str(val),L)
            if lock_con.acquire():
                if len(L)>5:   #当这个队列数量超过10时，就挂起
                    lock_con.wait()
                L.append(val)
                lock_con.notify() #唤醒其他线程
                lock_con.release() #释放锁
            time.sleep(3)
class Consumer(threading.Thread):
    def run(self):
        global L
        while True:
            lock_con.acquire()
            if len(L)==0:
                lock_con.wait()  #当队列没有资源时，进行挂起。
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            print('消费者',self.name,'Delete'+str(L[0]),L)
            del L[0]
            lock_con.notify()
            lock_con.release()
            time.sleep(0.5)
if __name__=='__main__':
    L=[]
    lock_con=threading.Condition()
    threads=[]
    for i in range(5):
        threads.append(Producer())
    threads.append(Consumer())
    for t in threads:
        t.start()
    for t in threads:
        t.join()

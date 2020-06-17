import threading ,time

num=0
#进行锁对象
lock=threading.Lock()
loca=threading.local()
def run(n):
      time.sleep(0.1)
      global num
      for i in range(10):
            # lock.acquire()   #第一种方式
            # try:
            #   num = num + n
            #   #num = num - n
            # finally:
            #  lock.release()
            # print(num)
            with lock:             #第二种方式
                  num= num +n
                  #num= num -n
                  print(num)
            loca.x=num




if __name__ == '__main__':

    t1=threading.Thread(target=run,args=(6,))
    t2=threading.Thread(target=run,args=(-6,))
    t1.start()
    t2.start()
    t1.join()
    # t2.join()
    print("num=",num,threading.current_thread().name)

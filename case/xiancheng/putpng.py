import  threading


lock=threading.Lock()

def  p(x):
    global  zer
    zer=1000
    while zer>0:
      #lock.acquire()  # 第一种方式
      try:
          zer=zer-x
          print(zer,threading.current_thread())
      finally:
            #lock.release()
            if zer< 0:
                  print("over",threading.current_thread())


if __name__ == '__main__':
    t=threading.Thread(target=p,args=(2,))
    t2=threading.Thread(target=p,args=(3,))
    t.start()
    t2.start()
    t.join()
    t2.join()
    print("num=",  threading.current_thread().name)
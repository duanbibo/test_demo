import threading



class A(threading.Thread):

     def __init__(self):
           threading.Thread.__init__(self)
           self.total=0

     def  add(self):

           for i in range(10**7):
                 with lock:
                   self.total+=1

#在外部声明个锁对象，内部可以使用lock.的加锁和释放锁的方法，或者使用with语句
lock = threading.Lock()

a=A()

t1=threading.Thread(target=a.add)
t2=threading.Thread(target=a.add)
t1.start()
t2.start()
t1.join()
t2.join()
print(a.total)

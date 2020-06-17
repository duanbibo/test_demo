import threading,time
class mythreading(threading.Thread):
    def run(self):
            semaphore.acquire()
            print(self.name+'\n')
            time.sleep(3)
            semaphore.release()
if __name__=='__main__':
    semaphore=threading.Semaphore(5)
    lst=[]
    for i in range(23):
        lst.append(mythreading())
    for i in lst:
        i.start()   #start方法执行父类的run方法

#存在输出的时候有时不会换行的现象没解决！
from multiprocessing import Process ,Queue
import random

'''
进程间数据交互通过队列，将含有队列的函数传给进程当执行体
'''
def f(qq,i):
      print("当前进程%s，消费的数据是 %s"%(i,qq.get()))


if __name__ == '__main__':
    ''' 利用队列将随机数放进队列内，然后各个子进程进行消费'''
    q=Queue()
    for i in range(1,4):
          n = random.randint(1,10)
          q.put(n)

    for i in range(1,4):
          p=Process(target=f,args=(q,i))    #这里创建的都是子进程
          p.start()

                          #子进程分别消费数据
          p.join()



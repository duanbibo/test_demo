import threading,time ,queue,random

#生产者
def product(i,q):
      while True:
            num=random.randint(0,1000)
            q.put(num)  #将生产者的数据，放入队列
            print("生产者%d生产了%d放入了队列"%(i,num))
            time.sleep(3)
      #任务完成
      q.task_done



   #消费者
def customer(i,q):
      while True:
            item=q.get()
            if item is None:
                  break
            print("消费者%d消费了%d数据"%(i,item))
            time.sleep(2)
      q.task_done()








if __name__ == '__main__':
      #消息队列
      q=queue.Queue


      #启动生产者
      for i in range(4):
          threading.Thread(target=product,args=(i,q)).start()
          #创建线程，线程的名称，线程的参数(i.q)
            # 这里面 i和q只是形参，只要数量对上就像。
            #i指的是 线程组号， q指的是 函数内的实际random值


     #启动消费者
      for i in range(4):
          threading.Thread(target=customer, args=(i, q)).start()

'''
打印结果;  生产者0-4 生产了1342数据放入了队列 
          消费者0-4 消费了 1234数据
                
'''
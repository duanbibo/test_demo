import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor
from  apscheduler.events import  EVENT_JOB_EXECUTED , EVENT_JOB_ERROR ,EVENT_JOB_REMOVED,EVENT_EXECUTOR_REMOVED


def timedTask(x):
       f=open('aps.txt','a')
       f.write(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]+x+'\n')
       print("first")
       f.close()

def my_listener(event):
    if event.code==EVENT_JOB_EXECUTED:
       print("任务已经执行完成")
    elif event.code==EVENT_EXECUTOR_REMOVED:
          print("作业已经被移除")






if __name__ == '__main__':

      #执行的间隔可以是变量，可以是某个函数的返回值。也可以是输入的值
      def jiange():
            return  5
      a=jiange()

      #使用执行器：线程池设置20个，将执行器当做调度器的参数传入进行实例化
      executors = {
            'default': ThreadPoolExecutor(1),
      }
      # 创建后台执行的 schedulers
      scheduler = BackgroundScheduler(executors=executors)

      # 添加调度任务 ，可以使用
      # 调度方法为 timedTask，触发器选择 interval(间隔性)，间隔时长为 2 秒
      scheduler.add_job(timedTask, 'interval',seconds=a,args=["你好"],id="first",max_instances=1)


       #方式二：通过为方法上添加装饰器来实现，确定是无法动态的控制job的行为
      #利用cron表达式进行执行。每天的19:23进行执行
      @scheduler.scheduled_job("cron",hour=15,minute=32,id="zhujie")
      def zhujierenwu():
            print("注解执行")


      # 当任务执行完或任务出错时，调用my_listener
      scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)


      # 启动调度任务
      scheduler.start()
      #scheduler.pause_job("first") #停止job
      #scheduler.remove_job("first") #移除job
      #scheduler.resume_job("first") #恢复job
      v=scheduler.get_jobs()   #获取所有job ,返回是一个列表，包括信息有job的id和function
      #scheduler.shutdown() 强制关闭所有调度任务
      print(v)

      while True:
            pass
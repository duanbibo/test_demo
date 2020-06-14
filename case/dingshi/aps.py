import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor


def timedTask(x):
       f=open('aps.txt','a')
       f.write(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]+x+'\n')
       print("first")
       f.close()





if __name__ == '__main__':

      #使用执行器：线程池设置20个，将执行器当做调度器的参数传入进行实例化
      executors = {
            'default': ThreadPoolExecutor(20),
      }
      # 创建后台执行的 schedulers
      scheduler = BackgroundScheduler(executors=executors)

      # 添加调度任务 ，可以使用
      # 调度方法为 timedTask，触发器选择 interval(间隔性)，间隔时长为 2 秒
      scheduler.add_job(timedTask, 'interval',seconds=2,args=["你好"],id="first")


       #方式二：通过为方法上添加装饰器来实现，确定是无法动态的控制job的行为
      @scheduler.scheduled_job('interval',seconds=2,id="secod")
      def zhujierenwu():
            print("注解执行")




      # 启动调度任务
      scheduler.start()
      scheduler.pause_job("first") #停止job
      #scheduler.remove_job("first") #移除job
      #scheduler.resume_job("first") #恢复job
      v=scheduler.get_jobs()   #获取所有job ,返回是一个列表，包括信息有job的id和function
      print(v)

      while True:
            print(time.time())
            time.sleep(5)
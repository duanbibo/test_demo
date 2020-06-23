import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler
import pymysql
from apscheduler.executors.pool import ThreadPoolExecutor
import redis
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
import logging
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR,EVENT_JOB_ADDED




# r=redis.Redis(host='localhost',port=6379,decode_responses=True,password='duanbibo')
value = 1

def write():
      global  value
      #r.set('aps_name', value)
      #print(r.get('aps_name'))
      print(value)
      value += 1


logging.basicConfig(level=logging.INFO,
                  format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
datefmt = '%Y-%m-%d %H:%M:%S',
filename = 'log1.txt',
filemode = 'a')


#每次执行完毕一个job后进行监听
def my_listen(event):
      if event.code==EVENT_JOB_ADDED:
            print("作业添加成功")
            logging.info("日志作业添加成功")
      elif event.code==EVENT_JOB_EXECUTED:
            print("作业执行成功")
            logging.info("日志作业执行成")







# 定义executor 使用asyncio是的调度执行规则
first_executor = ThreadPoolExecutor(10)

# 初始化scheduler时，可以直接指定jobstore和executor
init_scheduler_options = {
    "jobstores": {
        # first 为 jobstore的名字，在创建Job时直接直接此名字即可
       'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite'),
        "redis" : RedisJobStore(db=1,host="localhost",port=6379,password="duanbibo")
    },
    "executors": {
        # first 为 executor 的名字，在创建Job时直接直接此名字，执行时则会使用此executor执行
        "first": first_executor
    },
    # 创建job时的默认参数
    "job_defaults": {
        'coalesce': False,  # 是否合并执行，当需要执行的定时任务终止后，再次启动服务后继续执行依次执行而非合并
        'max_instances': 5  # 最大实例数
    }
}
# 创建scheduler
scheduler = BackgroundScheduler(**init_scheduler_options)
#配置监听，需要制定监听的事件，不同的事件对应着调度器在执行任务中不同的事件
#制定这个监听是对job任务执行后的监听
scheduler.add_listener(my_listen, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR|EVENT_JOB_ADDED)
#清除之前的任务，否则添加新的任务不成功
scheduler._jobstores.clear()
scheduler.add_job(write,'interval',seconds=2,id="redis_aps")

# 启动调度
scheduler.start()
while True:
            print(time.time())
            time.sleep(5)




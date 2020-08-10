from tqdm import tqdm
import time


#进度条，显示百分比，进度条，当前执行第X批次 ，当前执行时间，剩余时间 ，每秒字节数
i=0
for i in tqdm(range(10**5)):
     i+=1
     if i%20000==0:
           time.sleep(0.1)




from retry import retry
#执行失败后，尝试进行5次，每2秒发起一次
@retry(tries=5,delay=2)
def do_somethding():
      print("1")
      assert  2>5

do_somethding()

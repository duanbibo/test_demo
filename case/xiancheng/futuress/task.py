import  time

def func1(c):
      print(time.time())
      time.sleep(c)
      print("func1休息了{}秒".format(c))
      return c

def func2(c):
      time.sleep(c)
      print("func2休息了{}秒".format(c))
      return " success"

def  huidiao(future):
      r=future.result()
      print(r,"回调函数执行中")
      return r

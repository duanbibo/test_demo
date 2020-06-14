import threading




def  p():
      # global timer
      timer = threading.Timer(2.0, p)
      timer.start()

p()
# if __name__ == "__main__":
#
#     timer = threading.Timer(2.0, p, ["Hawk"])   ##每隔两秒调用函数hello
#
#     timer.start()
#     #timer.cancel()

def fun_timer():
      print("hello timer!")
      # 定义全局变量
      global timer
      # 10秒调用函数一次
      timer = threading.Timer(3, fun_timer)

      print('当前线程数为{}'.format(threading.activeCount()))

      # 启用定时器
      timer.start()

fun_timer()
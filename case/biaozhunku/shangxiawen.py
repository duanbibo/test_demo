
''' '''
'''
python的上下文管理器 ：
   with和上下文管理器：with出现的原因是简化 try ..finally 模式 
                        用于保证代码在执行某项操作时由于异常而中止。
   上下文管理协议包含 enter 和exit 方法，enter是个无参方法，执行后返回当前对象的引用，
                    exit 方法，是一个包含3个非必填参数exc_type异常类型，exc_value异常值，traceback回溯信息                  
                        
   
'''
class OpenContext(object):

    def __init__(self, filename, mode):  # 调用 open(filename, mode) 返回一个实例
        self.fp = open(filename, mode)

    def __enter__(self):  # 用 with 管理 __init__ 返回的实例时，with 会自动调用这个方法
        print("enter")
        return self.fp

    # 退出 with 代码块时，会自动调用这个方法。
    def __exit__(self, exc_type, exc_value, traceback):
        self.fp.close()
        print("exit")
        return False

# 这里先构造了 OpenContext 实例，然后用 with 管理该实例
with OpenContext('./geshihua.py','r') as f:
      print("ing")
      pass






import contextlib
from contextlib import suppress ,closing,redirect_stdout,contextmanager
from urllib.request import urlopen

with closing(urlopen('http://www.baidu.com'))as page:
      for line in page:
            print(line)

with suppress(ZeroDivisionError):
      a=0/0
      print("已经抑制指定异常了")
      print(a)
with open('source.txt','a',encoding='utf-8')as f:
      with redirect_stdout(f):
            help(callable)


'''   自定义一个上下文的装饰器，利用yield关键字前后调用 进入和退出方法'''
@contextmanager
def  con():
      print("开始")
      msg=" finally部分"
      try:
            yield  5
      except ZeroDivisionError:
            msg="0不能当除数"
      finally:
            print(msg)


with con() as c:
      print("执行中")
      print(c)


'''
else从句 不仅能和if 结合，也可以与 while，for except 进行一起使用
'''





l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in l1:
      print(i)
else:
      print("over")

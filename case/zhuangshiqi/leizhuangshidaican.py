from functools import wraps
import inspect
import requests

class reques():

      def __init__(self,url='',method='get',**kwargs):
            self.url=url
            self.method=None
            self.head=None
            print(url,method)

      def  __call__(self, func):
            print(func,"原方法")
            #self.func=func
            #第一种方式
            # def info(*args):
            #   print("参数列表",*args)
            #   return func(*args)
            #
            # return info
            @wraps(func)
            def  func_warp(*args):
                  print("参数列表",*args,inspect.getfullargspec(func),inspect.getsource(func))
                  return func(*args)
            return  func_warp





@reques(url="url1",method="get")
def  t(a,b):
      print(a,b)

t("ttt","xxx")

print(t.__name__)


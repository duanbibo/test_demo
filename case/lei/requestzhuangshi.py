
from functools import wraps
import requests
import inspect

class request():
      def __init__(self,method,url,**kwargs):
            self.method=method
            self.url=url


      def __call__(self,func):
          @wraps(func)
          def wrapper():
               print(inspect.getfullargspec(func),self.url,self.method)
               print(func.__name__,func.__doc__)
               res=requests.request(method=self.method,url=self.url)
               print(res.content)
               return res
          return wrapper


@request(url="http://www.baidu.com",method="get")
def login():
      ''' 登录接口'''
      pass

# l=login()
# a=l.content
# print(a)

if __name__ == '__main__':
      def test_():
            a = login()
            print(a)
            assert 200 in a


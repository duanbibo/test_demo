import time
from functools import wraps
def log_i(func):
      def inner(*args,**kwargs):
            print("start time",time.strftime("%Y-%m-%d   %H:%M:%S"))
            func(*args,**kwargs)
            print("over time", time.strftime("%Y-%m-%d   %H:%M:%S"))
      return inner

@log_i
def neirong(a):
      print(a)

neirong("zhuang")

print("--------------")
import time

def out(par):
       def mid(func):
             def inner(*args,**kwargs):
                   if par =="pingfang":
                     print("pass，先执行装饰器内部的东西")
                     #通过装饰器内部实现将函数中提供的参数进行处理
                     jieguo=[ i*i for i in args ]

                    # print(jieguo)
                     return func(jieguo[0],jieguo[1],**kwargs)

                   else:
                         print("erro，先执行装饰器内部的东西")
                         func(*args,**kwargs)

                         print("over","继续执行装饰器内东西",par)

             return  inner


       return mid

@out("pingfang")
def te_(a,b):
      print(a,b,"执行函数内操作")

#te_(4,5)


def log(func):
      def warpper(*args,**kwargs):
            print("执行了",func.__name__,"方法")
            return  func(*args,**kwargs)

      return  warpper
@log
def p(pp):
      print(pp)


p(1)
print("--------")
def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(
                level=level,
                func=func.__name__))
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper

@logging(level='INFO')
def say(something):
    print("say {}!".format(something))

say( "你好")

#当打印函数的名字时，由于函数被装饰器修饰，所以打印的结果是处理函数参数的闭包内的实际函数，而非原函数
print(say.__name__)
print("=============")
def logging2(level):

    def wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(
                level=level,
                func=func.__name__))
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper

@logging2(level='INFO')
def say2(something):
    '''你好呀'''
    print("say {}!".format(something))

say( "你好")

#当装饰器内部使用了系统提供的wraps时，系统就会获取
print(say2.__name__,say2.__doc__)
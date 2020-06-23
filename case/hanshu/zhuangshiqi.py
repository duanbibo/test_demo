
import time


# def runtime(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         f = func(*args, **kwargs)     # 原函数
#         end = time.time()
#         print("运行时长：%.4f 秒" % (end-start))
#         return f
#     return wrapper
'''
装饰器就是一个闭包：   
        1>  外函数的参数：接收被装饰器修饰的函数名；
            内函数的参数：接受被装饰器修饰函数内的参数。
        2>  外函数不处理逻辑，直接return 内函数的方法
            内函数处理完逻辑后，直接调用   原函数名（参数）
        3>   用法，主要是对原函数进行解耦，将原函数的参数值进行判断。   

              anno(A)；
                 def nei(a):
                 
                    A(a)
                 return nei
                 
                    
                    

'''
def score(func_s):
      print("装饰器定义后直接执行")
      sc=[]
      def wrapper(b):
            nonlocal sc
            if b<0:
                  sc.append("输入错误")
                 # print(sc)
            elif b <60:
                  sc.append(b)
                  print("您的成绩是{}分，不及格".format(sc[0]))
            elif b<=80:
                  sc.append(b)
                  print("您的成绩是 %d 分，及格"%b)
            else:
                  sc.append(b)
                  print("您的成绩是 %d 分，恭喜你"%b)
            func_s(b)  #在内函数通过  函数（参数），退出返回到被装饰的函数中，去执行剩余部分。
            print("继续执行装饰器操作")
      return wrapper


@score
def func_y(b):
      print("回到原函数内部执行",b)

b = int(input("请输入你的成绩："))
#func_y(b)

print("----------------------")
''' ----- --------------------'''
def func(a, b):
    def line(x):
        return x*a  - b


    return line


print(func(2, 3)(4))  #5
'''-------- --------------- ---------'''

def zhuangshiqi(hanshu):
      def neibu(canshu):
            if canshu>100:
                  print("erro")
            else:
                  print("good")
            return hanshu(canshu)

      return neibu

@zhuangshiqi
def a(wang):
      print("xxx")
      pass

#a(100)


import time
def zhuang(c):
      def f(func):
            def inner(*args,**kwargs):
                  time.sleep(c)
                  print('可以调用装饰器的参数,暂停%s秒执行'%c)
                  return func(*args,**kwargs)
            return inner
      return f

@zhuang(8)
def daicanshu(cs):
      pass
#调用
daicanshu('xx')


def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print ("[{level}]: enter function {func}()".format(
                level=level,
                func=func.__name__))
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper

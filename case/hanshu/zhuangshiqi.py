
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
      def wrapper(b):
            if b<0:
                  print("您输入的成绩错误")
            elif b <60:
                  print("您的成绩是 %d 分，不及格"%b)
            elif b<=80:
                  print("您的成绩是 %d 分，及格"%b)
            else:
                  print("您的成绩是 %d 分，恭喜你"%b)
            func_s(b)
      return wrapper


@score
def func_y(b):
      pass
''' ----- --------------------'''
def func(a, b):
    def line(x):
        return x*a  - b


    return line


print(func(2, 3)(4))
'''-------- --------------- ---------'''

def zhuangshiqi(hanshu):
      def neibu(canshu):
            if canshu>100:
                  print("erro")
            else:
                  print("good")
            hanshu(canshu)

      return neibu

@zhuangshiqi
def a(wang):
      wang+4

      pass


def get_x(z, b):
    return lambda x:z+b
z = get_x(1, 3)

print(z('x'))      #5,4



if __name__ == '__main__':
      b = int(input("请输入你的成绩："))
      func_y(b)
      a(101)




# @runtime
# def func_a(a):
#     print("hello"+a)
#     time.sleep(0.5)


# if __name__ == '__main__':
#     #func_a("a")
#     func_s()

# def test(func1):
#     def test_in():
#         print("testing")
#         func1()
#     return test_in
#
# def f1():
#     print("---f1----")
#
# f1=test(f1)
# f1()
#
# b=2
# b+=3
# del b
# print(b)
# 解析如下：
#
# 1.  test(f1)  有两层关系 1. f1 代表是 f1函数名的指针当作参数传入 test()  , 2. test(f1) 代表 返回test_in 函数指针
# 2. f1=test（f1） 把test_in 函数指针赋值给 f1  ,f1 的函数指针 有 指向 print（“----f1----"）变成了test_in里的函数体
# 3. f1() 执行test_in 里的函数体
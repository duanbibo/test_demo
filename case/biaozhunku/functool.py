import  functools
'''
functools库主要有哪些东西：比如常用的map reduce ,fillter 中reduce函数
       def wraps(wrapped: _AnyCallable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> 
        系统提供的包装类，可以通过此装饰器能够获取被修饰的函数的一些签名信息。
       lru.cache( maxsize=128,typed=False) 装饰器：备忘功能，主要用于优化递归是修饰函数, 每次结果执行记录，缓存不会无限增长，
         参数指定了存储多少个调用的结果，存满之后，旧的结果是否会被扔掉，腾出空间。调试起来方便
         
        
        
'''
'''   partial :主要是冻结参数，固定将原函数以及提供额外的参数，组合成一个新的func,
       每次调用这个组合后的func时，默认先执行原函数和冻结的参数
        语法    partial(func  , parameter)
 '''
from operator import mul
from functools import partial

dongjiesum=partial(mul,4)
jieguo=dongjiesum(5)
print(jieguo)


'''   单重派发 函数的装饰器 ：根据函数的第一个参数的类型，决定调用哪一个同名函数
      与java中的方法重载类似，在一个类中方法名一样的话，要求参数列表不同。
      python以另一种方式进行实现了，根据第一个参数类型来选择具体实现的策略。
'''
from functools import singledispatch

@singledispatch
def parse(arg):
      print('没有合适的类型被调用')

@parse.register(str)
def _(arg):
      print('选择策略：出现str了')

@parse.register(int)
def _(arg):
      print('选择策略：这次输入的是整数')

@parse.register
def _(arg: list):
      ''' 从python3.7开始可以用注解来进行标注第一个参数的类型'''
      print('选择策略：这次使用的是通过注解的list类型')

parse(3)
parse('4')
parse([4,5,6])
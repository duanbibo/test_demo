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

'''  propertry  :使用这个装饰器将函数伪装成类实例的属性
     这个是类，内部有setter, getter,deleter 方法


'''

class Student(object):
    #__slots__ = ('get_score', 'set_score','_score')

    # def get_score(self):
    #      return self._score
    #
    # def set_score(self, value):
    #     if not isinstance(value, int):
    #         raise ValueError('score must be an integer!')
    #     elif value < 0 or value > 100:
    #         raise ValueError('score must between 0 ~ 100!')
    #     else:
    #           self._score = value
    def p(self,xx):
          print(xx)
    @property
    def score(self):
          return self._score

    @score.setter
    def score(self, value):
          if not isinstance(value, int):
                raise ValueError('score must be an integer!')
          elif value < 0 or value > 100:
                raise ValueError('score must between 0 ~ 100!')
          else:
                self._score = value


s=Student()

s.score=89    #调用@property修饰的方法，调用时类似于参数的调用，给这个属性赋值
print(s.score)    #调用源get方法。’
s.p(90)

'''
warps  :装饰器，他的函数中的参数 指定了，用来获取被装饰函数的一些信息。
WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__', '__doc__',
                       '__annotations__')
WRAPPER_UPDATES = ('__dict__',)    #当被修饰的函数是类，可以通过 dict 获取实例下的属性返回一个字典 {'_score': 89},
                                     通过类名调用的dict获取的信息更全。
def update_wrapper(wrapper,
                   wrapped,
                   assigned = WRAPPER_ASSIGNMENTS,
                   updated = WRAPPER_UPDATES):
                   
'''
def  func(tt):
      '''测试描述doc'''
      print(tt)
a=func('ttt')
print(func.__doc__)
print("对象的dict信息",s.__dict__)
print("类实例的dict信息",Student.__dict__)

''' 用于比较的装饰器'''

from functools import  total_ordering

'''给定一个声明一个或多个全比较排序方法的类，这个类装饰器实现剩余的方法。这减轻了指定所有可能的全比较操作的工作。
此类必须包含以下方法之一：__lt__() 、__le__()、__gt__() 或 __ge__()。另外，此类必须支持 __eq__() 方法。
用在类上面，让类重写这些方法，
'''

''' functools.cmp_to_key(func)   将旧的比较换成新的比较。参数为比较函数，是一个可调用对象。该对象接受两个参数并比较他们。
 结果为小于则返回一个负数，相等则返回零，大于则返回一个正数。key function则是一个接受一个参数，并返回另一个用以排序的值的可调用对象。
 类似于 sorted() ， min() ， max() ， heapq.nlargest() ， heapq.nsmallest() ， itertools.groupby() 等函数的 key 参数中使用
 '''

# sorted(iterable, key=cmp_to_key(locale.strcoll))  # locale-aware sort order

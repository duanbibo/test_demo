import wrapt
import inspect

@wrapt.decorator
def log(wrapped, instance, args, kwargs):
      if  len(args) ==1:
       print(wrapped.__name__,wrapped.__doc__)
      return wrapped(*args,**kwargs)


@log
def say(something):
      '''原函数的注释'''
      pass


say("hello")
print("========需要带参数的装饰器")

import wrapt

def logging(level):
    @wrapt.decorator
    def wrapper(wrapped, instance, *args, **kwargs):
        print(level,instance,wrapped.__name__,wrapped.__doc__,inspect.getfullargspec(wrapped),inspect.getsource(wrapped))
        return wrapped(*args, **kwargs)
    return wrapper

@logging(level="INFO")
def do(work):
      '''我是文档注释'''
      pass

do("every")

class Person():

      def __init__(self, name, age):
            self.name = name
            self.age = age

      @logging(level='INFO')
      def say(self):
            print("i'm  %s ,i had  %d" % (self.name, self.age))

      def __str__(self):
            return  '[Person: name:%s ,age: %d]'%(self.name,self.age)


p=Person('测试第三方模块',38)
p.say()





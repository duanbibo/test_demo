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


def logging(level):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        print(level,wrapped.__name__,wrapped.__doc__,inspect.getfullargspec(wrapped),inspect.getsource(wrapped))
        return wrapped(*args, **kwargs)
    return wrapper

@logging(level="INFO")
def do(work):
      '''我是文档注释'''
      pass


do("every")



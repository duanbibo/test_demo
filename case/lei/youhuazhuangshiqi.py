from decorator import decorate


def wrapper(func,*args,**kwargs):
      return  func(*args,**kwargs)


def log(func):
      return  decorate(func,wrapper) #用wrapper装饰 func

print("=======第二种方式")



from decorator import decorator

@decorator
def log2(func,*args,**kwargs):
      print(func.__name__,func.__doc__)
      return func(*args,**kwargs)


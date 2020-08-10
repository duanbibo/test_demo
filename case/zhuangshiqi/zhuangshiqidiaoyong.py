
class  tracer:
      '''类装饰器：通过实例属性共享信息'''

      def __init__(self,func):
            self.calls=0
            self.func=func
            print("执行init %s"% (self.func))

      def __call__(self, *args,**keargs):
            self.calls+=1
            print('call %s to%s' %(self.calls,self.func.__name__))
            return self.func(*args,**keargs)



def  ftracer(func):
      ''' 函数装修饰单个函数的实例保存：调用同一个函数共享实例nonlocal'''
      call=0
      def inner(*args):
            nonlocal  call
            call+=1
            print("这是第 %s 次调用"% call)
            func(*args)
      return inner


gcall=0

def fatarcer(func):
      '''基于修饰多个函数的状态信息保存'''
      def inner(*args):
            global  gcall
            gcall+=1
            print("这是第 %s 次调用,被修饰的函数时 %s"%(gcall,func.__name__))
            func(*args)


      return inner


def  hanshu_shuxing(func):
      '''通过函数属性来传递被修饰的实例'''

      def inner(*args):
            inner.calls+=1
            print('call  %s  to %s'%(inner.calls,func.__name__))
            return  func(*args)

      inner.calls=0
      return  inner



class  tracer_wraps():
      '''基于描述符的类函数，修饰类方法不会报错'''
      def __init__(self,func):
            self.func=func
            self.call=0


      def __call__(self, *args, **kwargs):
            self.call+=1
            print('call %s  to  %s' %(self.call, self.func.__name__))
            return  self.func(*args, **kwargs )

      def __get__(self, instance, owner):
            print("开始执行__get__方法")
            def wrapper(*args, **kwargs):
                  return  self(instance,*args, **kwargs)
            return wrapper







@tracer
def spam(a,b,c):
      print(a+b+c)


@tracer
def spam2(a,b,c):
      print(a+b+c)


@ftracer
def su(a,b,c):
      print(a+b+c)


@ftracer
def su2(a,b,c):
      print(a+b+c)


@fatarcer
def sua1(a,b,c):
      print(a+b+c)


@fatarcer
def sua2(a,b,c):
      print(a+b+c)


@hanshu_shuxing
def one(a,b,c):
      print(a+b+c)

@hanshu_shuxing
def two(a,b,c):
      print(a+b+c)
# spam(1,2,3)
# # spam(2,3,4)






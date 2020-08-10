
'''
修饰类的装饰器，单例。
通过一个字典收集实例，如key作为类名，value

'''



def single(aClss):
      instances = None

      def onCall(*args):
            nonlocal  instances
            if instances==None:
                  instances=aClss(*args)
            return  instances

      return  onCall


@single
class Person:

      def __init__(self,name,hours,rate):
            self.name=name
            self.hours=hours
            self.rate=rate

      def pay(self):
            return self.hours*self.rate


bob=Person('bob',40,10)
anni=Person('anni',80,4)
print(bob.pay())


def  Tracer(aClass):
      '''利用getattr进行拦截类方法，做钩子函数
      '''

      class Wrapper:
            def __init__(self,*args,**kwargs):
                  self.fetches=0
                  self.wrapped=aClass(*args,**kwargs)

            def  __getattr__(self, attrname):
                  print('Tracer:'+attrname)
                  self.fetches+=1
                  return getattr(self.wrapped,attrname)

      return  Wrapper


@Tracer
class Spam:
      def display(self):
            print('Spam!'*8)


@Tracer
class Spam2:
      def display(self):
            print('Spam!'*8)

s=Spam()
s.display()
s.display()
s.display()

#没执行一次，调用getattr拦截方法
s2=Spam()

s2.display()
print([s.fetches],[s2.fetches])
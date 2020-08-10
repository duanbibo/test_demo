
''' 编写个装饰器工具类，用来控制检查实例方法传参的范围'''

def rangetest(*argchecks):   #最外部处理装饰器的参数
      def  onDecorator(func):#这个参数用来指明被装饰器修饰的方法
            def onCall(*args): #这个参数用来指明被装饰器修饰方法的参数
                  for (ix,low,hight) in argchecks:
                        #遍历最外部装饰器的参数，因为装饰器的灿说可能多个方法参数的映射
                        if args[ix]<low or args[ix]>hight:
                              errmsg='Argument %s not in %s ..%s' %(ix,low,hight)
                              raise TypeError(errmsg)
                  return func(*args)
            return  onCall
      return  onDecorator



@rangetest((1,4,100))
def person(name,age):
      print(name,age)

p1=person('李四',20)
#p2=person('张三',190)   当传入的参数不符合时，主动抛出异常

'''
使用第三方库 ，编写装饰器实现函数内省
'''

import wrapt
import inspect

def logging(level):
    @wrapt.decorator
    def wrapper(wrapped, instance, *args, **kwargs):
        print(level,instance,wrapped.__name__,args,kwargs,wrapped.__doc__,inspect.getfullargspec(wrapped),inspect.getsource(wrapped))
        return wrapped(args)
    return wrapper


class Person():

      def __init__(self, name, age):
            self.name = name
            self.age = age

      @logging(level='INFO')
      def say(self,value):
            '''类方法的说明文档'''
            print("i'm  %s ,i had  %d ,%s" % (self.name, self.age,value))

      def __str__(self):
            return  '[Person: name:%s ,age: %d]'%(self.name,self.age)

pc=Person('张三',28)
pc.say("你呢")


'''
目的：利用python3.0 注解的特性，在函数内编写注解后，利用工具类的装饰器，对调用时进行校验。


 思路： 由于需要从注解内提取参数，注解的信息可以由fuc通过内省的方式系统，所以只需要1层嵌套。
        由于注解是和参数进行绑定的，所以他的类型肯定是字典
        
 结果：不推荐使用，因为注解的个数和参数列表不确定。无法进行一一照应。
          不像装饰器一样能够根据索引提供对应的参数列表详细的参数       
'''
print("*"*40)
def rangetestan(func):
    def onCall(*pargs,**kargs):
        argchecks= func.__annotations__

        print(argchecks,"注解的返回字典")
        print(pargs,"打印实参")
        print(kargs,"打印")
        x=0  #外部声明个变量，在内部循环的时候每次+1
        for check in argchecks:  #遍历字典的时候，返回的对象是字典的key
              #x += 1
              print(pargs[x],":",argchecks[check])

              if  argchecks[check][0]< int(pargs[0]) <argchecks[check][1]:
                    print("pass")
              else:
                    raise  ValueError



        return func(*pargs,**kargs)
    return onCall

@rangetestan
def source(a:(1,10)):
      print(a)



s1=source(5,)
#s2=source(15)


def  attr(obj):
      return obj.value*4
def   attrfunc(obj,value):
      return  value+'func'




class  MetaOne(type):
      '''
      元类是一种类似于基于类的高级工具，其用途往往与类装饰器有所重合。他们提供了一种可选的模式，
      会把一个类对象的创建导向到顶级type类的一个子类
      元编程：当前的类名继承type类，并且在自己内部类定义new方法或者init方法


      '''

      def  __new__(meta,classname,supers,classdict):
            '''classname指的是使用元类的类名，supers指的是使用元类的当前类仍继承的其他类，
            classdict指的是使用元类的内部字典信息，包括执行模块、类名、属性、方法,
            核心就是这一块能够获取的话，就可以操作添加钩子函数'''
            classdict['attr']=attr
            classdict['func']=attrfunc
            print('In MetaOne.new:',classname,supers,classdict,sep='...')
            return  type.__new__(meta,classname,supers,classdict)

      def __init__(Class,classname,supers,classdict):
            print('In MetaOne init:',classname,supers,classdict,sep='...')
            print('...init class object:',list(Class.__dict__.keys()))


class Eggs:
      pass



print("making class")
class  Spam(Eggs,metaclass=MetaOne):
      '''在运行到class处，如果当前类使用了声明的元类，就直接进入元类去执行__new__'''
      data=1
      value= 'lei'
      def meth(slef,arg):
            print(arg)


print('making instance')
X=Spam()
print('data:',X.data)
print(Spam.__dict__) #元类中的方法只能被类继承，不能被类实例继承。
print(X.__dict__)    #实例属性查找通常只是搜索实例及其所有类的__dict__字典，元类不包含在实例查找中
print(X.attr())
print(X.func('instance'))







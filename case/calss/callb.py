def inp():
      return "aaa"
def first(a):
      print("zzzz",a)
first(inp())
print(inp.__dir__())

class  c(object):
      def __init__(self,name):
            self.name=name
      def i(self):
            #print(self.name)
            return self.name
      def __call__(self, *args, **kwargs):

            return self.name+"call"
      def __str__(self):
            return self.name+"str"
      def __repr__(self):
            return self.name+"repr"



ins=c(name="00")
ins.i()
print(c.__dict__) #打印实例内部的属性
print(ins.__dict__)
print(ins.__dir__())
print(type(ins)) # 他的类型是类
print(type(range)) #range也是个类，
print(type(type)) #type也是个类，
first(ins.i())           #正常回调实例的方法作为参数
first(ins.__call__())         #打印回调函数内容
first(ins) #打印str内容
first(ins)


a='456'
b=str(a)
print(eval(b),type(eval(b)))

d='789'
d=repr(d)
print(eval(d),type(eval(d)))

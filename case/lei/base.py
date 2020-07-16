import sys
import time
import string
import random
class base():


      na="全局属性"  #
      # 默认的熟悉是public，可以利用创建实例，进行直接赋值或修改覆盖
      _age=18  # protectd ,受保护的，但是也可以通过。对象._属性= value
      __course="python"  #私有的private ，不能在外部创建对象后重新赋值
      # 类的属性，python中类的属性不单独写，而是将所有的属性封装在构造函数__init__里面


      # def __new__(cls, na,*args, **kwargs):
      #       cls.na="oi"
      #       print("new")
      def __init__(self,name,age):
            self.name=name
            self.age=age
            print("我是子类构造函数")

      def getx(self):
            return self.name

      def setx(self, value):
            self.name = value

      def delx(self):
            del self.name

      # create a property
      x = property(getx, setx, delx, "I am doc for x property")

      def upname(self ,v):
            return  self.setx(v)


      def  __str__(self):

            return self.name+"  "+str(self.age)+"   "+self.__course

      def info(self,x):
          #方法在声明时，参数内必须传入self,在调用时就不用传入了。
          #self ：指代传入对象的本身。实例调用函数,和java中的this类似
          #在这通过self.属性 =参数值，可以定义调用类成员属性进行重新赋值
          #这里类中的na变量和方法中的na不是同一个。
          #如果在方法中使用类变量的话，可以用__class__.变量或者 类名.变量
          #在内中的方法中，可以操作init内的属性
          self.age=self.age+x
          # __class__.na="zzz"
          # print(x,__class__.na,base.na)
          print(self.age,"你长大了")
            # return None


a=base("zhangsan",17)  #创建个类的实例化对象
# a()# 调用 call函数
print(a)
print(a.na,a._age,a.setx(999),a.setx("zhang3"))
print(a)

a.na='lisi'  #类的实例化对象，进行修改类的成员变量的值。
a._age=20
print(a._age,)
a.info(80)

print("--------base over ----")
class base2():
      bb="我是类属性公开的"
      _b2="我是类属性受保护的"
      __bb="我是类属性私有的"

      def __init__(self,b2):
            self.b2=b2

      @classmethod
      def class_method(cls):
            print("是类方法")
            return cls._b2

      @staticmethod
      def static_method():
            print("是静态方法")


print(base2.bb,base2._b2)

print(base2.class_method(),base2.static_method())
print("-----------base2 over--")
class fa(base,base2):

      def __init__(self,name,age,score):
            #base.__init__(self,name,age)
            super().__init__(name,age)
            #super().__init__(b2)
            self.score=score
            print("我是父类构造函数")

            #子类覆写父类的方法，
      def info(self,x):
            self.age = self.age - x


            print(self.age,"你变小了")



f=fa("fa",18,40)
f._age+=6
print(fa.na,fa._age)
#子类实例默认调用自己内部的方法
f.info(4)
#以下两种是调用父类被覆写的方法
super(fa,f).info(8)
base.info(f,7)


help(f)


print(f.__hash__())



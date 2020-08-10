''''''
class  Base(object):

  #__slots__ = ('name','age','adress','tel')

  @classmethod
  def class_func(cls):
        """ 定义类方法，至少有一个cls参数 """
        print('类方法')

  @staticmethod
  def static_func(sta):
        # """ 定义静态方法 ，无默认参数"""
        print('静态方法',sta)

  def  __init__(self,name,age,adress=99):
        print("构造方法先执行")
        self.name=name
        self.age=age
        self.adress=88
        print("父类构造方法执行完毕--")


  '''类、类的所有方法以及类变量在内存中只有一份，所有的实例共享它们。
     类创建的时间，创建了实例方法，静态方法，类方法，以及类内的变量 
  '''
  #property(fget=None, fset=None, fdel=None, doc=None)

  def info(self): #普通方法
        print("实例方法")
        print(self.name,self.age,self.adress,"is a good  boby")


  def update_attry(self,updatevalue):

        ''''''''''
        #修改默认的参数值，通过一个方法。将原来参数值重新赋值，用修改方法内的参数赋值
             self.原参数=传参的值
             self.原参数+=传参的值 ，达到每次进行递增
        '''
        #在修改原参数值的时候，做一次判断更合理
        if int(updatevalue)>=self.adress:
           self.adress=updatevalue
        else:
            print("无需修改")


  def im(self):
        print("im baba")

class Son(Base):
      ss='ss'


      def __init__(self,name,age,adress,myself):
            super(Son, self).__init__(name,age,adress)

            print("开始执行子类的构造方法")
            print("先去继承父类的构造方法区")

            self.__myself=myself
            print("子类的构造方法--执行完毕")


      def update_attry(self,ab):
            # 重写父类的实例方法
           Base.update_attry(self,ab)
           print(self.ss,Son.ss)

           #super(Son, self).update_attry(ab)    #调用父类方法

      def im(self):
            Base.im(self)


      def __hide(self):
            print("隐藏的方法")


      #通过为指定方法添加property装饰器，将方法伪装为实例的属性
      @property
      def myself(self):
            # 重写父类的实例方法
            return  self.__myself

      #将属性进行设置单独set方法。需要配合 @property
      @myself.setter
      def  myself(self,myself):
            self.__myself=myself










a=Base("zhangsan",18,99)      #只要创建对象，就调用构造方法

a.home="house"  # 动态语言，可以在程序运行之中添加属性
print(a.home)  #添加的动态方法可以输出

a.info()           #  等同于  Base.info(a)   ==   a.info()
a.update_attry(-1)
a.info()


print("--------")

# z=Son()  #实例化子类对象
# z.info()
# z.update_attry()  #子类的调用和父类同名的方法，调用的是自己内部的方法。
Base.class_func()  # 通过类直接调用类方法，不需要实例化对象
Base.static_func(2)  #通过类可以直接调用静态方法，不需要实例化对象
print("=============")
s=Son('老王',3,15,"我自己的")     #只要创建对象，就调用构造方法

s.update_attry(40)
print(s.myself)
s.myself="我通过属性修改的"
print(s.myself)








#print(a.__dict__)
#del a
#print(Base.__dict__)

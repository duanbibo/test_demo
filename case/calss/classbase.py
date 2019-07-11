''''''
class  Base(object):

  @classmethod
  def class_func(cls):
        """ 定义类方法，至少有一个cls参数 """
        print('类方法')

  @staticmethod
  def static_func(name):
        # """ 定义静态方法 ，无默认参数"""
        print('静态方法',name)

  def  __init__(self,name,age,*adress,**kwargs):
        '''
        构造函数
        :param name:  姓名 不为空
        :param age: 年龄不为空
        :param adress:  地址可以为空，有默认值
        :param kwargs:   其他字段可以填写的
        '''
        self.name=name
        self.age=age
        self.adress=0
        self.tel=110
  '''类、类的所有方法以及类变量在内存中只有一份，所有的实例共享它们。
     类创建的时间，创建了实例方法，静态方法，类方法，以及类内的变量 
  '''
  # property(fget=None, fset=None, fdel=None, doc=None)

  def info(self):

        print(self.name,self.age,self.adress,self.tel,"is a good  boby")

  def update_attry(self,updatevalue):

        ''''''''''
        #修改默认的参数值，通过一个方法。将原来参数值重新赋值，用修改方法内的参数赋值
             self.原参数=传参的值
             self.原参数+=传参的值 ，达到每次进行递增
        '''
        #在修改原参数值的时候，做一次判断更合理
        if updatevalue>=self.adress:
           self.adress=updatevalue
        else:
            print("无需修改")
  def im(self):
        print("im baba")

class Son( Base ):

      def __init__(self,name,out):
            super(Base,self).__init__(name=name)
            self.out=out




      def update_attry(self,ab):
            # 重写父类的实例方法
            ab+=3
            print(ab)







a=Base("zhangsan",18)
a.home="house"  # 动态语言，可以在程序运行之中添加属性
a.info()   #  等同于  Base.info(a)   ==   a.info()
a.update_attry(15)
a.info()
print("--------")

# z=Son()  #实例化子类对象
# z.info()
# z.update_attry()  #子类的调用和父类同名的方法，调用的是自己内部的方法。
Base.class_func()  # 通过类直接调用类方法，不需要实例化对象
Base.static_func(2)  #通过类可以直接调用静态方法，不需要实例化对象




#print(a.__dict__)
#del a
#print(Base.__dict__)

from  case.zhuangshiqi.zhuangshiqidiaoyong \
      import tracer,ftracer ,spam,spam2,su,su2,sua1,sua2,one,two,tracer_wraps



class  person():

      def __init__(self,name,pay):
            self.name=name
            self.pay=pay

      @tracer
      def giveMonay(self,percent):
             self.pay*=(1+percent)

      @ftracer
      def giveMoney2(self,percent):
            self.pay *= (1 + percent)
            print(self.pay)
      @tracer_wraps
      def giveMoney3(self,percent):
            self.pay*=(1+percent)





if __name__ == '__main__':

      '''  同一个函数应用相同的装饰器，只初始化一次，这几个函数共享一个实例'''
      spam(4, 5, 6)
      spam(1, 1, 1)


      ''' 不同的函数应用同一个装饰器，返回的还不是一个实例'''
      print("类实例变量:不同的函数应用同一个装饰器，返回的还不是一个实例")
      spam(4, 5, 6)
      spam2(3, 5, 4)


      ''' 调用基于函数的装饰器：noclocal'''

      print("调用基于函数的装饰器：noclocal不同的函数不共享数据信息")
      su(1, 3, 3)
      su2(1, 3, 5)

      '''基于调用函数的装饰器，调用不同的函数，实例共享global '''
      print("基于调用函数的装饰器，调用不同的函数，实例共享global ")
      sua1(3, 6, 7)  # 说明
      sua2(1, 5, 7)  # 说明成功了

      ''' 基于 函数的属性：在外部定义个内部函数的属性'''
      print("基于 函数的属性：在外部定义个内部函数的属性,实现共享数据等同于 noclocal")
      one(1, 2, 3)
      one(2, 2, 2)
      two(1, 2, 3)

      ''' 装饰器修饰类的实例，执行对应的方法报错，缺少参数'''
      print("装饰器修饰类的实例，执行对应的方法报错，缺少参数，")
      p1=person('张三',1000)
      #m1=p1.giveMonay(0.2)   #这个是基于类装饰器修饰类方法，错误
      p1.giveMoney2(0.2)    #这个是基于函数装饰器修饰类方法，正常
      p1.giveMoney3(0.3)



class  shuxing(object):
      leishux='zhuangshiqi'

      #attr=['name','age','addr','tel']

      def __init__(self):
            self.name='name'

      def __getattribute__(self, item):
            ''' 无论属性存不存在都会被先调用'''
            print("getattribute：查询属性被访问了",item)
            #return  self.__getattr__(item)
            return 'aaa'


      def  __getattr__(self, item):
            '''当属性不存在时被调用拦截'''
            # if  item not in shuxing.attr:
            #
            #      raise  AttributeError
            print("getarrt 当属性不存在进行拦截",item)

      def  __call__(self, *args, **kwargs):
             return print("call  调用",args)


      # def  __setattr__(self, key, value):
      #       '''当对属性赋值时进行拦截,包括init内也进行拦截'''
      #       if  key =='tel':
      #             print("属性存在时，赋值调用")
      #             self.__dict__[key]=value
      #       else:
      #             raise  (AttributeError ,"not allowed")




if __name__ == '__main__':



     s=shuxing()
     print("类名直接调用")

     shuxing()("我真的传值了")

     print("调用结束")



     # 判断当前实例是否有这个属性
     print(hasattr(s, 'age1'),"hasattr函数判断类中是否有属性")
     print(hasattr(s, 'age'))
     #setattr(s,'age','19')   #映射类的重载setattr 方法，对已有和未存在的属性进行赋值
     getattr(s,'a')
     print(getattr(s,'a'),"利用getattr方法获取属性的返回值")
     print("---------fengexian")
     #s.age=18
     #s.name='zhangsan'
     #s.addr='beijing'


     print(s.age)
     print(s.name)
     print(s.addr)

     print(s.__dict__)
     #s.info
     #print(s.info)
     #print("测试下通过setattr时，能够调用getattrbute")
     #s.tel=80

     print(s.__dict__)
     print(s.leishux)






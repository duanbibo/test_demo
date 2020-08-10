import pickle
import json


class lei:

      def __init__(self,name,age):
            self.name=name
            self.age=age
      # def __str__(self):
      #       return '[%s :  name %s   age  %s ]' %(self.__class__,self.name,self.age)


if __name__ == '__main__':
    '''
    当对象没有被序列化时,是无法直接写入文件中，如果想写入文件中，即使是定义__str__重载运算符，
    也是只在控制台输出，而无法输入到持久化文件中,最多调用实例的str方法将类的str方法输出的字符串结果写入文件中，
    但是在读取的时候是一个字符串，不能获取它的属性等信息。所以是不可行的，就需要利用工具辅助将对象信息持久化到文件中
    
    '''

    l=lei("张三",20)
    print(l)


    '''
    序列化dump：使用pickle时，必现先利用open函数打开一个文件对象，同时序列化时用的是字节流，所以在encoding的时候不允许指定字符集
      在使用mode模式的时候，必选选择 b 字节流,否则还会报错
    '''
    f=open( 'xuliehua.txt',mode='ab')
    pickle.dump(l,f)

    ''' 反序列化load：去其他地方取出数据'''
    ff = open('xuliehua.txt', mode='rb')
    data=pickle.load(ff)
    print(data,type(data))
    print(data.name,data.age)



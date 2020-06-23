import  inspect
from  inspect import signature
'''
inspect库的作用：主要是来获取函数的详细信息。主要是为了获取参数列表进行处理

'''



def prin(x:int,z=None,y=3,*arge,d1=60,d2=80,**kwarge)->int:
      '''提取参数的doc'''
      print(x,y)

      return x

l=[4,5,6]
d={'k1':'v2','k2':'v2'}
c=prin(1)

#获取函数名称和文档
prin(prin.__name__)
hanshuming=prin.__name__
#获取函数名的参数
a=inspect.getfullargspec(prin)

print(a)
print("参数列表有参",a.args,"参数列表",a.kwonlydefaults)


sig=inspect.signature(prin)
print("参数的签名:获取形参和注解",sig)

#在已知函数名的情况下可以直接通过函数名.doc获取相关的资源，大部分的方法时返回数量而非参数。
print("函数的说明文档",prin.__doc__,"函数的名称",prin.__name__,"函数的内存地址和文件类型，以及文件位置和所在行号",prin.__code__,
      "函数的已赋值的形参数量",prin.__code__.co_argcount,
      "函数的所有形参参数数量",prin.__code__.co_nlocals,
      "函数的关键字且赋值的形参数量",prin.__code__.co_kwonlyargcount,
      "函数的所有形参变量名称",prin.__code__.co_varnames,
      "自由变量",prin.__code__.co_freevars)
#如果在不知道函数名的情况下就无法获取信息了








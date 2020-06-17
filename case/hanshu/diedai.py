from collections import Iterable
from collections import Iterator

l1=[0,1,2,3,4]
print(isinstance(l1,Iterable),type(l1))  #判断当前对象是否为可迭代对象
print(l1.__dir__())

l2=iter(l1) # 利用迭代器的构造函数，传入对象转化为迭代器对象
print(isinstance(l2,Iterator),type(l2))
print(l2.__dir__()) #类型为list类型的迭代器

d1=enumerate(l1)  #将列表转化为枚举对象,枚举对象本身就是迭代器，内部有iter方法和next()方法
print(d1,type(d1))
for i in d1:
      print(i)
d2=iter(d1)   #枚举类本身也是迭代器，使用迭代器的构造函数返回还是它本身类型

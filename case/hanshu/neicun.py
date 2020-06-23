import sys
import os
import gc

a=[]
b=[]
c=[]
a.append(b)
b.append(a)
del a
del b
del c

# print(hex(id(a)))
#print(hex(id(b)))
#print(hex(id(c)))  #打印对象的地址值 hex()函数时，函数用于将10进制整数转换成16进制，以字符串形式表示。把10进制的ID数转换为0x开头的地址值
print(gc.collect())

print(gc.get_threshold())


from array import array
import random

'''
计算机为数组分配一段连续的内存，从而支持对数组随机访问；
由于项的地址在编号上是连续的，数组某一项的地址可以通过将两个值相加得出，即将数组的基本地址和项的偏移地址相加。
数组的基本地址就是数组的第一项的机器地址。一个项的偏移地址就等于它的索引乘以数组的一个项所需要的内存单元数目的一个常量表示（在python中，这个值总是1）

array 模块是python中实现的一种高效的数组存储类型。它和list相似，但是所有的数组成员必须是同一种类型，在创建数组的时候，就确定了数组的类型

创建的时候与tuplename类型，第一个参数标志这个这个对象的类型 typecode
'''

arr=array('I',[0,1,5])
print(arr,arr.typecode)
print(arr.count(1),"打印数组中某一个数字出现的次数")
print(dir(arr),arr.itemsize,arr.__sizeof__())
print(len(arr),"3个元素")


''' 利用array对象的tofile方法把它写入文件内
      fromfile ,通过数组对象调用，将含有数组的文件读出指定长度的数据。
'''



li=list(arr)
print(li,type(li),"把数组转化为list")
from collections import Iterator,Iterable

'''
 查看元祖的核心内置方法， getitem  index
'''
tu=(1,2,3,3.5,5)
print(dir(tu))
print(tu[0],"元祖也有index 变量，也可以通过索引进行获取元素")
print(tu.__getitem__(4),"getitem方法是传入指定的索引获取对应的值")
isinstance(tu,Iterator)




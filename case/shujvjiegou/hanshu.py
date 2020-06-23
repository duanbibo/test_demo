



'''  将列表的每个元素取出，配上自己的索引，输出为元祖'''

'''   enumerate  函数 (可迭代对象，start=指定开始的数字)
 如果没有的话，从0开始，每个可迭代对象与索引组合成一个元祖
'''
l1=[11,22,33,44,55]
print(l1)
em=enumerate(l1)

l2=[i for i  in em]
print(l2)
print("-----")
zhuan=( dict(i)for i in l2)


''' zip  将2个列表或者元素，组合在一起，为一个字典，前者作为key列表，后者为value列表。
dict的长度，取决于他俩共有的长度 '''
list3=(1,2,3,4,5)
zip1=zip(l1,list3)


print(zip1,type(zip1))
dict1=dict(zip1)
print(dict1,type(dict1))

'''
obj.join([iterate]) : 
       obj指定的是分隔符，将后面的可迭代对象进行拼接：取出可迭代元素的第一个元素和分隔符进行组合，一直到结束。
          处理完后返回的类型是字符串
 interate.split("obj"):
        obj指的是分隔符，将前面的可迭代对象进行切割:拿着切割符去检验可迭代对象，如果符合就切割。切割出来的元素统一放在列表中。
          返回的是列表集合。     如果可迭代对象没有符合的，返回原内容 
'''
cas=('a','b','c','d')
b=" ".join(cas)
print(b,type(b))#  a b  c  d

c=b.split(" ")
print(c)       #['a','b','c','d']

'''locals  函数，返回文件中所有的全局变量'''
dd={"aa":11,"bb":22}
print(locals())









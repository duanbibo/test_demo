
print(dir(dict))
dict1={1:2,'c':3,4:'g',('a','b'):'c'}
#根据字典的key值获取value值

'''  字典的内置方法和字段 '''
sv=dict1.__getitem__("c")
print(sv,"字典的内置方法 getitem传的值是key值")


# setdefault :可以快速的添加元素。

de=dict1.setdefault('setd','setdk')
print("setdefault返回的是value的值",de)
print("字典的原始数据为：%s"%dict1)

v=dict1.get(4)
print("利用get方法传入key值，获取value值为%s"%v)
ks=dict1.keys()
print("利用keys获取全部的keys,%s"%ks)
vs=dict1.values()
print("利用values获取全部的keys,%s"%vs)
ie=dict1.items()
print("利用items获取全部的keys和value,%s"%ie)
dict1["11"]=4
print(dict1,"添加字典key和value")
sfh=dict1.setdefault(4,5)
print("利用setdefault进行根据value获取key值,如果有key存在，返回原始的值：%s"%sfh)
sfn=dict1.setdefault('w',5)
print("利用setdefaul获取key值没有，进行添加新的key和value值：%s"%sfn)
print(dict1)
#updata的参数必须为一个字典，它

dict1.update({1:3})
print('查看利用updata修改后的字典',dict1)
#使用字典进行格式化 是 format(**字典)  ；format_map(字典) ,
# 字典格式化输出的值默认是value值，按照一定顺序打印
stu={'name': 'Jack', 'sex': 'm', 'age': 22}
print("my name  is{name} ,im {sex} ,i hava {age}old".format(**stu))
print("my name  is{name} ,im {sex} ,i hava {age}old".format_map(stu))


cw=18
cw+=2 if cw>10 else cw-2
#  a?a++4:a-=3   三元运算符
print(cw)

''' 字典的拆包'''
dictc={"name":"zhangsan","age":24,"score":{"chinese":80,"math":69,"english":40}}

print("my name  is{name} ,im {age} ,i get {score[chinese]} score".format(**dictc))

# list dict tuple set


a="abcdef"
b=a[::2].upper()

a.replace(a[::2],b)
print(a)

''' 字典解析--遍历字典'''
dictjx={'a':'11','b':'22','c':'33','d':'44','e':'555'}
for i in dictjx:
      print("dictjx[%s]="%i,dictjx[i])
for (k,v) in dictjx.items():
      print("dictjx[%s]="%k,v)

print(dictjx['a'])
print(dictjx.items())
print(dictjx.get('a'))


l1=(1,2)
l2=[2,3]

D={k:v for (k,v)in zip(l1,l2)}
print(D)

'''zip 将2组数据打包'''
k=['你','好','呀']
v=['a','b','c']

zp=zip(k,v)

D={k:v for (k,v)in zp}
print(D)
print("{你},你好呀{好},{呀}".format_map(D))
print("{你}，你好呀".format(**D))

lis=[]
print(dir(lis))  #它的

from collections import Iterator
from  collections import Iterable
print(isinstance(D,Iterator))
print(isinstance(D,Iterable))  #字典是可迭代对象
print(dir(lis))


zidian={1:2,2:3}
aa=zidian.items()
print(aa)

''' 字典推导 ：可以从任何以键值对作为元素的可迭代对象中构建出字典'''
#提供数据源,数据源是列表嵌套元祖或者列表嵌套列表
data=[ (110,'警察'),(120,'医生'),(119,'消防')  ]

zidiantuidao={k:v      for k,v   in data}
print(zidiantuidao)




#默认字典工厂，产生的字典key是自定义的，value的类型是根据构造函数传入的数据类型。
import collections
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

# defaultdict
d = collections.defaultdict(list)
for k, v in s:
    d[k].append(v)
print(d.items())


#利用dictdefault工厂函数，实例统计key值变化，自增
#统计一个字符串中，各个字符的个数
di = collections.defaultdict(int)

s='daskjdhashdjkasj89798789122121'
for k in s:
      di[k]+=1
print(di)

'''   求字典的hash地址'''
d1={'key':'a1','key2':'a2'}
d2={'key':'a3','key2':'a4'}

str="key"
str2='key2'
print(str.__hash__(),str2.__hash__())
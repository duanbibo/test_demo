dict1={1:2,'c':3,4:'g',('a','b'):'c'}
#根据字典的key值获取value值
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
print("利用setdefault进行根据value获取key值：%s"%sfh)
sfn=dict1.setdefault('w',5)
print("利用setdefaul获取key值没有，进行添加新的key和value值：%s"%sfn)
print(dict1)
#使用字典进行格式化 是 format(**字典)  ；format_map(字典)
stu={'name': 'Jack', 'sex': 'm', 'age': 22}
print("my name  is{name} ,im {sex} ,i hava {age}old".format(**stu))
print("my name  is{name} ,im {sex} ,i hava {age}old".format_map(stu))


cw=18
cw+=2 if cw>10 else cw-2
#  a?a++4:a-=3
print(cw)
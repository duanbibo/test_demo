from functools import  reduce

#求1-100之间带3的数之和
li=  [i  for i in range(1,100) if str(i).__contains__('3')]
print(sum(li))

#合并两个相同长度的数据为字典
tel_number=(110,120,119)
name=('警察','医院','消防')

d=dict(zip(tel_number,name))
for k,v in d.items():
      print(k,"是",v)

#列表转化为字典
ld=[('警察','110'),('医院','119'),('消防','120')]

di={}
for i in ld:
      di.setdefault( i[0],i[1])
print(di)

a=sum(range(1,100))
print(a)
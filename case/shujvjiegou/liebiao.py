
list1=[1,2,3,4,5,6,8,9]
#列表追加append方式，可以追加任意类型,相当于将内容当做一个整体了
list1.append([8,9])
print(list1)
#extend方式追加，只能追加能够迭代的类型，如字符串，元祖，列表等
list1.extend([7,8,9])
print(list1)
#移除元素，使用remove时，采用的是列表的值，不需要双引号
list1.remove([8,9])
print(list1)
#移除元素，通过pop移除时，后面的值为列表的下标
p=list1.pop(3)
print(p)
print(list1)
#列表进行翻转，可以使用[::-1] 或者  list.
list1.reverse()
print(list1)
s=list1[::-1]
print(s)
#列表的排序,默认为升序
lt=[1,7,454,663,678,343,0]
s2=sorted(lt)
print(s2,)
'''
列表和元祖的区别
 1.列表是可变的，元祖是不可变的
 2.声明同一个数据，用列表存储和用元祖存储大小是不一样的。元祖占用空间小，处理块
 3.列表中一般存储同质同类型数据，元祖一般存储异质不同类型的数据
     [1,2,3,4](1,zhangsan,24,[daxue])
 4.由于可变和不可变原因。元祖在存储上是安全的
'''
#打印元祖中元素出现的次数,如果是字符类型的必须加‘’
tp=(1,3,'4',4,567,6,'4','4')
print(tp.count('4'))
#求字符出现的位置，索引 index(value,start,end)
print(tp.index(3))  #在全局范围内查找，单个元素的索引
print(tp.index('4',2,7))#在指定范围内查找，单个元素的索引，只匹配第一个。


list7=[4,5,6]
list8=[4,5,7,8]
#需求1，将2个列表合并为1个列表，实现去重的功能
#列表可以转化为set集合，set是无序的，不能够重复,实现列表合并去重的需求
print(list(tuple(set(list7+list8))))
#需求2：将2个列表合并成一个字典，实现[4:0,5:1,6:2,7:3,8:4] 这种类型

#第一步：根据列表1的下标生成新的列表
list9=[]
for i in range(0,len(list7)):
      list9.append(i)
#print(list9)
print(list7,list9)
#将两个列表组合成一块ZIP，可以是字典，也可以是集合，也可以是列表，zip时，取公有的长度内容。
dic1=dict(zip(list7,list9))
print("根据列表值和下标生成的字典1是：%s"%dic1)
ziplist=list(zip(list8,list7))
print("根据列表值和下标生成的列表1是：%s"%ziplist)



list10=[]
for i in range(0,len(list8)):
      list10.append(i)
dic2=dict(zip(list8,list10))
print("字典2是：%s"%dic2)

print(set(zip(dic1,dic2)))
set2=set(zip(list8,list10))
print("根据列表值和下标生成的元祖1是：%s"%set2)

li=[12,45,67]
l=[12,34]
setsame=set(li).intersection(set(l))
setunion=set(li).union(set(l))
setdiff=set(li).difference(set(l))
print(list(setsame),list(setunion),list(setdiff))


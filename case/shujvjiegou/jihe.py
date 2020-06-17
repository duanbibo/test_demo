import queue
#集合分为几类：set集合 dict字典 queue
'''
set 集合特性：set内的元素不允许重复，所以经常用来去重的操作，可以将tuple,list，dict数据类型进行转换
 set集合的声明和字典一样，采用{}表示，元素之间用，隔开,set集合内可以装字符串，元祖。
'''
set1={'a',1,('a','b'),(1,2)}
''' set集合在打印的时候是无序的，元素内的排序不同'''
print(set1)
#add方法，向集合内添加元素。
set1.add('w')
print(set1)
''''    updata( 可迭代对象  进行多个添加)'''
set1.update([0,1,2,3,4])
print("通过updata方法实现多了可迭代对象进行添加",set1)

'''  删除集合内元素，调用remove()方法执行删除时，如果传入的参数在集合内不存在的话，会报错
   建议使用 discard()方法对其删除，及时元素不存在也不会报key错误
'''
#set1.remove(8)
set1.discard(8)



li=[12,45,67]
l=[12,34]
'''   set集合内的一些方法用来进行求差、和、并集
   差值  相减                difference             -
   并集  相同的项只取一份    union   |
   交集   只取相同的部分     intersection        &
   
 
'''
setsame=set(li).intersection(set(l))
setunion=set(li).union(set(l))
setdiff=set(li).difference(set(l))
print(list(setsame),list(setunion),list(setdiff))

set2={1,3,5,6,7}
set3={2,4,5,7,9}
'''
集合推导:推导出来的数据不能有重复的、
'''

jihetuidao={ i for i in range(1,20) if  i%3==0 }
print("集合推导结果",jihetuidao)

value = {j if j%3==0 else 0 for j in  range(20)}
print("集合推导+三元运算，三元运算要放前面，数据推导放后面",value)

'''
操作两个集合的方法 和U对应的运算符
'''
'''&:用来连接2个集合的共同部分'''
ssame=set2&set3
print("两个集合的相同的元素&表示：%s"%ssame)

'''|:用来连接2个集合的共同部分'''
sunion=set2|set3
print("两个集合一共的元素|表示：%s"%sunion)

'''-:用来表示第一集合的部分，减去2个集合重复的部分'''
sdiff=set2-set3
print("第一个集合的全部减去2个集合重复的部分-表示：%s"%sdiff)


'''^:用来表示两个集合不重复的部分  ：对称差集'''
schaji=set2^set3
print("两个集合不重复的部分^表示：%s"%schaji)
duichen=set2.symmetric_difference(set3)
print("对称差集",duichen)







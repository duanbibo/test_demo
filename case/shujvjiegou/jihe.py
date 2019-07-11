import queue
#集合分为几类：set集合 dict字典 queue
'''
set 集合特性：set内的元素不允许重复，所以经常用来去重的操作，可以将tuple,list，dict数据类型进行转换
 set集合的声明和字典一样，采用{}表示，元素之间用，隔开,set集合内可以装字符串，元祖。
'''
set1={'a',1,('a','b'),(1,2)}
''' set集合在打印的时候是无序的，元素内的排序不同'''
print(set1)
li=[12,45,67]
l=[12,34]
'''   set集合内的一些方法用来进行求差、和、并集'''
setsame=set(li).intersection(set(l))
setunion=set(li).union(set(l))
setdiff=set(li).difference(set(l))
print(list(setsame),list(setunion),list(setdiff))

set2={1,3,5,6,7}
set3={2,4,5,7,9}

'''&:用来连接2个集合的共同部分'''
ssame=set2&set3
print("两个集合的相同的元素&表示：%s"%ssame)

'''|:用来连接2个集合的共同部分'''
sunion=set2|set3
print("两个集合一共的元素|表示：%s"%sunion)

'''-:用来表示第一集合的部分，减去2个集合重复的部分'''
sdiff=set2-set3
print("第一个集合的全部减去2个集合重复的部分-表示：%s"%sdiff)

'''^:用来表示两个集合不重复的部分'''
schaji=set2^set3
print("两个集合不重复的部分^表示：%s"%schaji)







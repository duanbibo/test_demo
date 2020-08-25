
import bisect

'''
bisect模块实现了二分查找和 插入算法
  二分查找： 找序列中指定值的右侧索引，即插入的值比传入参数的值相同时，占位的索引
  插入算法： 指定序列和插入值，根据策略不同，当出现插入值和序列中的值一样时，执行的策略。
  
  bisect 就是调用的bisect_right  ,不执行插入操作，默认返回指定序列中值的右侧索引
insort 就是调用 的insort_right，  默认执行插入时如果当前元素和比较的元素相同时，执行插入右侧。后添加的索引值大


  
'''

list1=[434,342,32,45,23,56,6,7,42,56]
#使用二分法必须先进行sort排序

list1.sort()
print(list1)

#使用二分查找方法，传入一个序列和序列中的元素，返回其右侧的索引
weizhi=bisect.bisect(list1,45)
print(weizhi)


#使用二分查找法，传入一个序列和一个任意元素，返回当插入该元素时，左侧数据的索引
bucha=bisect.bisect_left(list1,88)
print(bucha)

#使用二分法，传入一个序列和任意元素，执行插入,返回结果是None
cha=bisect.insort_left(list1,343)
print(cha,list1)

#二分法插入根据值
ins=bisect.insort(list1,88)
print(list1)
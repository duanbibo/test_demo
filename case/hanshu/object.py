'''

'''
from functools import reduce
'''
内建函数： 一部分是，实现的是函数的功能作用 如sum ,sort等，可以直接拿来用
          另一部分的内建函数的参数，可以传入函数为参数，能够再实现一次重写。
          
   以第二部分的内建函数为例：       
  经常使用到的 range() :用于列表生成式 ,它返回的是迭代中的一个元素
         map(func,[]):它返回的是一个迭代器，能够打印迭代器中的所有元素 。
          filtter(func,[])    :它是一个拦截器，用来处理参数的，如果参数符合func就返回迭代器
         
'''


'''
      range()使用后返回的是迭代中的每一个元素
'''
lis=[]
for i in range(1,4):
      lis.append(i*i)
print(lis)






'''
eval 函数： 可以将字符串转成表达式并执行，并且能够对字符串执行
   eval(expression[, globals[, locals]])

expression ： 表达式。
globals ： 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
locals ： 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
  
'''
# 将字符串拆分，还原到原来的格式
print(type("4"))
print(type(eval("4")))

#能够执行表达式的内容
print(eval("print('执行')"))

# 第一个参数字符串，第二个参数字典对象，全局对象，用于替换第一个参数内的值
stringdict="{'name':'linux','zzz':age}"
print(eval(stringdict,{"age":1822}))
#第一个为表达式，第二个为参数字典对象，局部对象，局部对象的值替换全局对象的值
age=18

print(eval("{'name':'linux','age':age}",{"lunux":"window"},locals()))


'''
map 返回的是一个迭代器，可以用list进行转换，做整体输出。

'''
'''
用map实现的是，返回一个迭代器，将里面所有的元素一次性全部输出
map()函数接收两个参数，一个是函数，一个是Iterable，
map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
map(函数，可迭代对象，)：参数1必须传，指的是参数2的类型或者采用的什么函数。如str,sum
                       参数2指的是被参数1方法操作的值，是实际值
'''
print(list(map(lambda x:x*x ,range(1,4))))



#执行过程为 ： 从a这个可迭代对象 里取出一个值，然后传递给 x， 并返回 x*x 的值 放到迭代器，然后list 转化为列表。
#  类似于   i*i for  i in a
a=[1,2,3]
diyige=next(map(lambda x:x*x,a)   )          #可以用next，说明这是个迭代器
print(diyige)
a=list(map(lambda x:x*x,a)) # lambda 是匿名函数 ， 用
print("我是用map以及lambda匿名函数的%s"%a)

b=[1,2,3]
'''   用这种map+for循环方法同时样式打印三个数的平方'''
dierzhong=list(map(int ,(i*i  for i in b ))   )
print("我是用map以及for循环的%s"%dierzhong)

'''   
需求; 求1-100之间数字的平方
使用map返回1-100的平方  ，然后计算，他们的和   '''
print(list(map(lambda x:x**2,range(101))))
num=0
for i  in  list(map(lambda x:x**2,range(101))):
      num=num+i
print("求和1-100之间数字平方",num)


'''
 reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
 reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
      把第一组参数放入函数内，求得结果后记录累加，将这组参数当做第一个参数，从列表中下一个参数放进来。
      比如计算 1-4的平方： 1的平方+2的平方 ，第二次： (1的平方+2的平方)的平方 +3的平方
'''
''' 使用reduce计算列表的值'''
def fn(x, y):
 return x * 10 + y

print(reduce(fn, [1, 3, 5, 7, 9])       )

''' 使用reduce进行求和'''
b=reduce(lambda x,y:x+y,range(101))
print(b)



# 首先 list 中第一位 0 ，传递给x， 第二位 1 传递给 y ，
# 求和 x+y =0+1 =1，
# 让1 作为x 的值继续传递 ， 然后取 2 为y
# 然后继续求和 2+1=3， 然后作为 x值， 依次循环 得出 总和
'''
      排序：
       a.sort(reverse=True)       进行倒序
       sorted(a)              默认正序
       sorted(a,reverse=1)           倒序排序

'''

'''
zip: 将前后2个对象进行压缩，每个对象内的第一个元素 组成一个元祖。
'''
z1=[1,2,3]
z2=[4,5,6]
print(list(zip(z1,z2)))
print(dict(zip(z1,z2)))

'''
     filter()也接收一个函数和一个序列，返回值也是一个迭代器。和map()不同的是，
     filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
     
 例如，在一个list中，删掉偶数，只保留奇数，可以这么写：
     
     def is_odd(n):
         return n % 2 == 1
     
     list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
     
  '''
'''  需求：求出1-10之间偶数的数字'''
print(list(filter(lambda x:x%2==0,range(1,11) )))

'''  需求：求出两数相加等于10的数字'''
# print(list(filter(lambda x,y:x+y==10,{range(1,10):range(1,10)})))

ls=[1,3,4,5,7,8,9]
kong={}
for i in ls:
      for z in ls:
            if i+z ==10 :
                  kong[i]=(z)
print(kong)


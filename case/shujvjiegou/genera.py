
#生成器 ，返回的是一个内存对象

g = (x * x for x in range(10))
# print(g)
# for n in g:
#       print(n)
#
''' 输出生成器对象的核心属性：
  __iter__,__next__  这两个私有的内置方法 是迭代器的属性，说明生成器也是迭代器     
   send ,thorw ，close 是生成器独有的一些方法。
   '''
print(dir(g),g)

#help()  #通过help函数能够调用python的doc,能够查看函数的信息
from  collections import Iterator
print(isinstance(g,Iterator),"事实证明生成器对象也是迭代器对象")

#列表推导式 ,返回的是一个列表
l=[x * x for x in range(10)]
print(l,dir(l))



print("===============")

'''   使用yield时，在执行一次生成器值的时候，虽然在执行到yield关键字的时候会暂停将这个状态保存下来，
在yield之后仍用的是本次生成器的值，它的声明周期是在本次循环内'''

def gensqu(h):
      for j in range(h):
              #print("之前",j)
              yield j*2
              #print("之后",j)

a=gensqu(3)
print(a)
for i in a:
      print(i)


'''  
通过调用生成器对象的next()内置发现，每次执行一次会在yield处返回；
下次调用next()时继续从上次调用的执行。
手动的进行调用时无法确定次数，有可能导致stopItera异常。
所以可以直接利用for循环,for循环。
'''
# print(a.__next__())
# print("第二次调用")
# print(next(a))
# print(a.__next__())





''' yield from 语法：

需求：当对多个可迭代对象的内部进行再遍历时，可以用两个for 循环，
        第一个for循环遍历每一个可迭代对象，第二个for循环遍历在最内层减小调用yield i ，
另外一种方式就是在第一个for循环遍历完每一个个可迭代对象后，
自动使用yield from 语句将返回可迭代对象的每一个元素， yield from iterable 自动会遍历输出每一个元素
它其实是一个语法糖。读起来更为顺畅。
yield from 还会创建通道，把内层的生成器与外层生成器的客户端练习起来。


'''
def pinjie(*iterables):
      ''' 实现iteratortool库的chain拼接多个可迭代对象'''
      for it in iterables:
            for i in it:
                  yield i
p=pinjie(['a','v','c'],[1,2,3],['w','o'])
print(list(p))

def pinjiefrom(*iterables):
      '''利用 yield from 语法将可迭代对象进行自动遍历'''
      for i  in iterables:
            yield from i

fp=pinjiefrom(['a','v','c'],[1,2,3],['f','m'])
print(list(fp))

''' 通过协程 yield 语法，实现平均数计算'''

def avg():
  total = 0
  count=0.0
  avg=None

  while True:
           term= yield avg
           count+=1
           total+=term
           avg=total/term
           print(avg)




ag=avg()
ag.__next__()
ag.send(5)



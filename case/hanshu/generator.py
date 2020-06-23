

# g=( x*x for x in range(0,10))
# for n  in g:
#       print(n)
#
''''''
#yield 只能在函数里面用
''''
 生成器 与列表解析比较;
     生成器表达式大体上可以认为是对内存空间的优化，他们不需要像方括号的列表解析一样，一次构造出整个结果列表。
     它们在实际中运行起来可能稍慢一些，所以它们可能只对于非常大的结果集合的运算来说是最优的选择。
'''
def creatgn():
      for i  in range(0,10):
            yield i*i
a=creatgn()

print(a,dir(a))
# 生成器返回的是一个生成器对象，必须放入for循环内，才能一次获取执行
#生成器主要的内置方法:send ,throw ,__next__ ,__iter__
#print(a.__next__(),a.__next__(),a.__next__())
for i  in a:
      print(i,"yield")


def fib(max):
    n, a, b = 0, 0, 1
    while b < max:
        yield b
        a, b = b, a + b
        n = n + 1

y=fib(10)
for i in y:
      print(i)

'''
列表推导式
'''
def squared(x):
    return x*x
multiples = [squared(i) for i in range(30) if i % 3 is 0]
print (multiples)


'''   range() 迭代器,
python2  返回一个 list
python3 返回为一个 迭代器'''
for i in range(1,10):
      pass


''' 利用zip和dict工厂函数，将两个长度相同的列表或者元祖组合为一个字典'''
l1=[1,2,3,45]
l2=[0,9,8,7]
z=zip(l1,l2)
print(dict(z))




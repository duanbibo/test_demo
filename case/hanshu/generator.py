

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





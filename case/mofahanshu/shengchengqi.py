'''

自定义类实现生成器内的内置方法：
所谓的协同程序就是可以允许的独立函数调用，函数可以暂停或者挂起，并在需要的时候从程序离开的地方继续或者重新开始
自定义生成器只需要含有yield关键字就可以，解释器会自动构建send next itear thorw方法
'''

def mygenerator(n):
      print("生成器开始运行")
      while n>0:
            yield n
            n-=1


g=mygenerator(5)
print(g)          #这里返回一个生成器对象，这个对象里已经保存了生成器对象，可以直接运行依次产生销毁一个实例。
g.__next__() #这一步手动运行了，next()，直接返回到yield右边的值输出，由于这里没有调用print 语句，没有接受yield后面的值，所以没有打印第一次yield的主
for i in g:   #下一步从这个运行的结果开始 ,利用for循环内置的next()遍历调用
      print(i,end="...")

g2=mygenerator(7)
g2.close() # 直接结束生成器的运行,
#g2.__next__()  #结束后无法继续运行，运行会报错

'''
yiled from  i  完全代理了内层的for循环
'''
def genfro(*iter):
      for i in iter:
            for j in i:
                  yield  j
ff=genfro("abc","123","ABC")
print(list(ff))

def genfrom(*iter):
      for i in iter:
            yield  from  i
gf=genfrom("12","AB","ab")
print(gf)
print(list(gf))
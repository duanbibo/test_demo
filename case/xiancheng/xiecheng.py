'''
协程：

  c= yield  a
 利用yield 关键字的生成器。每次停止(stop)返回在yield处。输出yield后的值，
 下次调用next()继续运行生成器，返回当前语句块的yield出。
 协程首次需要激活运行，在yield输出值。协程类似于 与do while 语句，必须执行一次。



'''

def  xiecheng():
      print("预激活协程")

      value1=yield    'X'       #第一步暂停到这执行,输出yield以前的语句和yield后面的值，
                               # 第二步调用send（）发送数据时，是对yield 等号左边进行赋值
      value2 = yield value1
      value3 = yield   value2
      yield  value3

g=xiecheng()
print(g.__next__())
print(g.send(8))
print(g.send(7))
print(g.send(6))

print("==============")


def  averGen():
      '''编写一个计算平均数的协程'''
      count=0
      aver=None
      item=0
      while True:
            value= yield aver
            item+=1
            count+=value
            aver=count/item

ag=averGen()
ag.__next__()
print(ag.send(8))
print(ag.send(15))

'''
让协议有返回值，在求平均值的基础上进行使用具名元祖，return具名元祖，
        并且在send的时候，根据传输的值进行break，然后停止迭代，内部捕获stopIteration异常并使用as从句，赋值。
        获取异常的结果，异常的结果就是返回值。
'''
from collections import namedtuple
Result=namedtuple('Result','count average')
def genReturn():
      total=0
      count=0
      aver=None
      while True:
            term=yield
            if term is None:
                  break
            total+=term
            count+=1
            aver=total/count
      return Result(count,aver)

gr=genReturn()
gr.__next__()
print(gr.send(80))   #这里返回None是正常的，因为还在内部执行中，没有产出值。yield 后面是空的
print(gr.send(8))
#print(gr.send(None))

''' 利用yield from 语句 '''
print("利用yield from 语句代替内部的循环")

def   genFrom(c):
      for i in c:
          yield from  i

f=genFrom(['abcde','ABCDE','12345'])
print(f.__next__())   # 输出打印a
print(list(f))

'''
利用yield from func 编写  表达式
分为三部分：调用方  、委派生成器 、子生成器
 调用方负责发送数据 ，
 委派生成器内由 yield from func表达式(指向子生成器) :它的参数为send
 子生成器内部有 yield关键字产出值  :它不需要参数，它的参数由调用方发给委派生成器，自动会在委派生成器内部发给自己。

'''
def  averager():
      '''子生成器'''
      total = 0
      count = 0
      aver = None
      while True:
            term = yield
            if term is None:
                  break
            total += term
            count += 1
            aver = total / count
      print(Result(count, aver))
      return Result(count, aver)

def grouper(result,key):
      '''委派生成器'''
      while True:

            result[key]=yield from  averager()
            #
            print("While True",result,key)

def report(results):
      #print(results)
      for key,result in sorted(results.items()):
            group,unit=key.split(';')
            print('{:2} {:5} avering {:.2f}{}'.format(result.count,group,result.average,unit))


def  mian(data):
      results={}
      for key,values in data.items():
            print(results,key, "main方法内")
            group=grouper(results,key) #这一步引用委托类生成器,发送数据va
            next(group)
            for value in values:
                  group.send(value)
            group.send(None)     #这里很重要，发送send为Nones时，代表让子生成器停止。委派生成器产出值
      #print(results)
      report(results)

data={
      'grils;kg':[40.8,30.8,47.0],
      'girls;m':[1.6,1.7,1.5,1.65],
      'boys;kg':[34,54,35,57],
      'boys;m':[1.45,1.34,1.60,1.40],
}
mian(data)


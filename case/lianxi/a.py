li=[(1,2),(3,4,5,6,7)]
a,*b=li
print(b)

'''迭代解包，先从第一个可迭代对象进行解包'''
for a,*b in li:
      print(b,end="..")


print("----------")
def out():
      out=9
      print("外部",out)
      def inner():
            print("inner")
            nonlocal out
            print("内部修改前",out)
            out+=1
            print("内部修改后",out)



            return  'over'

      return inner()
out()


# var 解析object含有dict属性，可以解析自定义的类实例
class person:

      def __init__(self,name,age):
            self.name=name
            self.age=age

p=person('田七',23)
print('{name} has {age} age'.format_map(vars(p)))
print(vars(p))


#试着注册一个func，利用eval 解析字符串。当传入的字符串包含  参数名(x)  会将他解析
def func(a):
      #print(a+1)
      return a+1

eval("func(3)")

from case.lianxi.b import funb

#eval函数返回一个对象，打印对象，调用的是字符串内的变量的return结果
ev=eval("funb(3)")
print(ev)

def ex(c):
      print(c)
      return c

e=exec('ex(5)')         #这里只做执行函数处理 -执行函数内的print语句。
print(e)  #它的返回值是None

''' 使用exec 能够访问当前命名空间内的所有内容 locals globals'''


with open('H://test.txt', 'r') as f:
    ss = f.read()
    #print(ss)

exec(ss)

#exec('h://log.txt')

#使用列表推导式打印九九乘法表
#分析从左到右进行 先用  \n 换行符      使用格式化数字 %2d
#       两个for循环 第一个代表每行的数据，第二个代表总次数。执行时先执行第二个，第一个在最内层
print('\n'.join([' '.join(['%2d *%2d = %2d' % (col, row, col * row)
                           for col in range(1, row + 1)]) for row in range(1, 10)]))

jiujiu=( '\n'.join([ ''.join(['%2d *%2d =%2d'%(col,row,col*row)for col in range(1,row+1)])for row in range(1,10)]))
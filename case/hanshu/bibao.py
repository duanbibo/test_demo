'''


了解变量的作用域： LEGB
本地，上层，全局，内建  四个空间部分，优先级由高到低。
调用时，可以直接调用。但是对函数做更改操作时，会导致不能引用操作成功。
在函数内部对全局变量操作时，可以声明下变量。将函数内的变量提升为全局，
然后在内部操作后全局的变量，更改后全局的原始变量也会变更。


目标：了解 globals()  locals()  global ,nonlocal  的使用
globals()获取当前类所有的全局属性返回类型为字典。
locals()获取当前局部变量返回类型为字典。
global:当内部变量与外部有冲突时，由于在局部优先调用局部的变量，所以如果要调用全局的变量必须用global 变量 声明，然后就赋值、调用
     用法二：将当前内部的作用域提升为全局 ，供其他函数内调用   ，也是先声明
nonlocal: 主要用在闭包内，内部函数调用外包函数的变量且可以修改外部变量的值。



'''

quanjv="quan"
a=4

def  out():
      '''  '''

      global  a
      a=a+5
      print(a)    #修改全局变量的值为9



      ou="外部自由变量"
      print(id(ou),"外部变量的id")


      def inner():
            global c
            c=8
            print(c)    #将本地变量提升到全局属性


            nonlocal  ou
            ou=ou+"+内部修改"
            #print("内部调用外部自由变量",ou)
            print("内部修改后的自由变量",ou,id(ou))
            return  ou  #返回ou值
      return inner()


out()
print("------")
print(out())
print(c)  #可以获取到内部提升的变量

o=out()

def A():
     x=4
     action= lambda  n:x**n
     return action

x=A()
print(x(3))  #3的4次方

def creat_counter():
    i=0
    def counter():
        nonlocal i
        i=i+1
        return i
    return counter

print(creat_counter())



def creat_add():
      i=3
      l=lambda x:i*x

      return  l
ad=creat_add()

print(ad(5))

g_b=90

def inner():
      global  g_b

      g_b=g_b+9
      print("局部",)
inner()
print("全局",g_b)

'''
 引用闭包内部的变量
'''

def oj():
      global  ojvar
      ojvar=8

#函数运行过后，就会将globals变量提升到全局
oj()
print(ojvar+2)
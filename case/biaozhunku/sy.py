import sys

'''
sys库主要是python解释器之间的输出，
 获取python解释器在执行代码时的  基础信息，执行信息，以及可以发送一些解释器的指令。如退出
 
'''
#sys返回当前python的环境变量。输出的有模块搜索的环境变量
print(sys.path,"获取python的模块搜索路径")
print(sys.platform,"操作系统名称：window")
print(sys.argv ,"输出程序的执行路径,是一个动态的")
print(sys.exc_info(),"输出程序执行当前的异常类型，异常值，异常对象")

print(sys.modules,"打印python解释器内的模块")
a=sys.stdout.write('plase')
print(a,"标准输出输出内容的值,返回结果是一个内容的len,可以利用这个做一个进度条")

'''  python解释器相关的内容：主要输出 对象引用，大小，以及解释器对于对象类型的元数据控制'''
d="大萨达所打算"
b=d
print(sys.getsizeof(a),"返回对象的大小")
print(sys.getrefcount(a),"返回对象的引用计数")
print(sys.float_info,"返回类型对象的详细信息")
print(sys.int_info,"返回int对象的统一信息：最大值，最小值")

print(sys.exit(),"程序直接退出，后面的不会执行")

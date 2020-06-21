import sys

'''
sys库主要是python解释器之间的输出，获取解释器的基础信息，执行信息
'''
#sys返回当前python的环境变量。输出的有模块搜索的环境变量
print(sys.path)
print(sys.platform,"操作系统名称：window")
print(sys.argv ,"输出程序的执行路径")
print(sys.exc_info(),"输出程序执行当前的异常类型，异常值，异常对象")

print(sys.exit(),"程序直接退出，后面的不会执行")
print("============")
'''写点啥呢'''
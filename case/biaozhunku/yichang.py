import traceback
import sys

'''
异常处理：处理了可能出现的任何意外或异常情况的方法。
python的异常处理使用try : catch ,else ,finally 关键字来进行尝试可能未成功的操作、处理失败及政策情况，以及事后的资源清理

try :
   执行的代码块
except   ExecptionA:
    print
except  ExeceptionB: 
    todo
else:
    没有匹配去做这件事
    
finally:
     必须做这件事
             
   

'''
import random


try:
      print("请输出数字和随机数一起进行运算")
      base=random.randint(0,10)
      a = input()
      '''把这个计算的过程放在try语句中，进行处理'''
      c=base+int(a)
except    ValueError as e:
      print(e,"类型错误,不同类型不能够参与计算,请输入数字")
except  RuntimeError:
      print("运行错误")
else:
      print(c)
      print("没有错误，输出运行结果",c)
      #print(sys.exc_info)
finally:
      print("运行结束")
      #print(sys.exc_info)


''' 自定义异常 使用，利用sys的exc_info()获取执行的结果

获取traceback中信息'''
import sys
import  traceback
from case.tool.logi import *
#模块导入后，直接会输出模块的路径


class MyExcept(Exception):

      def __str__(self):
            return "超过输入长度限制"

#运用定义的异常
try :
      print("请输出2位数字")
      base = random.randint(0, 10)
      a = input()
      '''把这个计算的过程放在try语句中，进行处理'''
      if a.__len__()>2:
            raise  MyExcept()
except RuntimeError as e:
      print(e,"???")
except MyExcept as e:
      #print(sys.exc_info()) 通过sys库中的exc_info方法获取执行的异常类型，异常输出值，以及异常的回溯信息

      '''
      sys.exc_info()获取了当前处理的exception的相关信息，
      并返回一个元组，元组的第一个数据是异常的类型(示例是NameError类型)，
      第二个返回值是异常的value值，第三个就是我们要的traceback object.
      '''
      exc_type, exc_value, exc_traceback_obj = sys.exc_info()
      #调用traceback模块，打印traceback信息出来，可以指定级别和输出流
      #print(traceback.print_tb(exc_traceback_obj ))
      #print("=====")
      #print(traceback.print_exception(exc_type, exc_value, exc_traceback_obj,file=open('source.txt',mode='a',encoding='utf-8')))
      #print("=========")
      #print(traceback.print_exc(file=open('source.txt',mode='a',encoding='utf-8')))
      #这个异常打印的格式是普通的，没有红色字体
      logging.error(traceback.format_exc(limit=1))



      '''
      当我们需要对回溯的对象信息更为详细的了解时，比如具体是哪里出问题了，
      如果系统的异常类能够打印出文件所在文件夹路径、模块、行号，就需要借助traceback模块。
      
    trackback模块中关于打印异常信息的有2个方法， 
    第一个是print_tb(traceback), 默认在控制台打印是没有标题的
    第二个是print_exception(exc_type, exc_value, exc_traceback_obj) 需要的参数就是sys.exc_info()元祖的返回值，
    打印出来的结果：多了开头的"Traceback (most...)"信息以及最后一行的异常类型和value信息  
                         还有一个不同是当异常为SyntaxError时，会有"^"来指示语法错误的位置
    
这里我们可以发现打印的异常信息更加详细了，下面我们了解下print_tb的详细信息：
traceback.print_tb(tb[, limit[, file]])  ：将回溯的信息打印出来。

tb: 这个就是traceback object, 是我们通过sys.exc_info获取到的
limit: 这个是限制stack trace层级的，如果不设或者为None，就会打印所有层级的stack trace
file: 这个是设置打印的输出流的，可以为文件，也可以是stdout之类的file-like object。如果不设或为None，则输出到sys.stderr。
     
     
   
      '''
      print(e)
else:
      print(a,"没有异常才执行")
finally:
      print("必须执行的")
print("执行完异常体，继续执行")










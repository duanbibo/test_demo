import requests   #导入系统的模块
import sys
import os



#第一种方式
from  case.calss.filea import *  #导入其他文件中的全部变量,不推荐这样，这样会影响当前文件命名空间管理。
bianliang="456"
print(bianliang,"如果用*的话，我无法导入filea文件中的某个变量，或者本地变量与它有冲突导致互相覆盖，引用最近的")  #引用导入后文件中的吧变量


#为导入的文件提供了属性最好 ，第二种方式，为导入的文件提供但单独的命名空间管理，方便与本地变量不起冲突。
import case.calss.filea as f
print(f.bianliang)

#使用form和import时，后面都可以增加as，进行重命名，与本地的变量名进行区分
from case.calss.filea import bianliang  as a

print(a,"使用form。。import ，最好导入需要的内容")



imp='imp'


print(locals())
print(sys.path)
#print(sys.modules)




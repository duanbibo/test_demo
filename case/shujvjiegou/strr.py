import os
import decimal

str1="1a2b3c4d5f"
j='-'.join(str1)   #拿指定字符与可迭代对象的每一个元祖去拼成一个新的字符。参数为可迭代对象
print(j)
a=str1[0:5]
#split截取，只能用在str上，返回的是一个列表
b=str1.split('3')
print(a)
print(b)
cur_path=os.path.abspath(__file__)
print(cur_path)
#获取当前路径，然后根据反斜杠进行截取，返回列表
lujing=os.path.abspath(__file__).split("\\")
print(lujing)
#利用字符串 ''.join 将路径拼接
huanyuan='\\'.join(lujing)
print(huanyuan)



#数字round方法 四舍五入
# ,%.3f  也是四舍五入
a=44.90889
c=a.__round__(3)
print(c)
print('%.3f' % a)
print(decimal.Decimal('1.23'))
#floorf(x)取整数部分


sst="oldstr"
new=sst+"sss"
print(new)


ssi=78.8777
print( '%d'% ssi)  #利用数值类型只保留整数位
print('%0.3f'% ssi)  #利用浮点型保留3位小数
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


stf='stf123g5555g'
print(stf.find('5'),"使用find函数，传入字符串返回它出现的第一次的索引值，找不到返回-1")
print(stf.index('5'),"使用index函数，传入字符返回它出现的第一次的索引值，找不到报错")
print(stf.split('g',),"使用split进行分割，分割的元素被取消掉，同时返回一个列表")
print(stf.split('5',1),"第二个参数可以指定分割的次数，如果不指定的话默认会将出现次数进行全部分割")
print('='.join(stf),"join插入，指定插入负调用join方法，参数传入被插入的可迭代对象")

''' 目标：遍历字符串 '''
print('='.join(stf).split('='),"先用指定出入分隔符，调用join方法传入字符串，然后再分割实现字符串每个对象的分割")
#第二种方式 利用for循环  ,在for循环外声明个列表，每次循环后append到列表内
lis=[]
for i  in stf:
      lis.append(i)
print(lis,"第二种方式 利用for循环  ,在for循环外声明个列表，每次循环后append到列表内")




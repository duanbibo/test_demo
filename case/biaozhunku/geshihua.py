

''' 格式化字符串 '''

'''
字符串格式化
'''

str1="111"
str2=str1+'2'
print(str2)

f="123.56"
'格式化字符串 :利用百分号'

print(' %s ' %(str2))
print('%d'%int(str2))
print('%.2f'%float(f),"格式化小数点  .2f   设置小数点后2位数字")

listf=['0','1','2']
print( "-".join(listf),"使用join进行将字符串的可迭代对象进行迭代，与前面的字符进行拼接")

lists=[0,1,2]
print('{}'.format(lists)," 使用字符串的format函数 ,前面字符串用大括号当做占位符，前后数量必须一致，前面是一个{}时，format参数内的可迭代对象会当做一个整体输出")
print('{},{},{}'.format(*lists)," 前后如果不一致时，后面的参数必须用* 拆包将参数赋给前面的大括号")
print('{1},{2},{2}'.format(*lists),"在格式化的时候，可以在占位符中使用{下标}，表示当前格式化的内容赖在format函数内的什么参数")

dicts={'key1':'value1','key2':'value2'}

print('{key1},{key2}'.format(**dicts),"字符串格式化时，使用字典时，字符串内的大括号必须写上字典的key值")
print('{key2},{key1}'.format_map(dicts),"使用format_map格式化，直接将字典对象传入")


import time

t=time.strftime('%Y-%m-%d %H:%M:%S')
print(t  ,"格式化日期时间利用strftime函数，在函数中字符串占位指定代替的 年月日，时分秒")
structt=time.localtime(time.time())
print(structt,"大部分time返回的要么就是int类型的毫秒值，"
                                  "要么就是结构化time元祖，必须要对整个元祖重新拆包赋值给指定字符串转化人类human易识别的")
'''time.struct_time(tm_year=2020, tm_mon=6, tm_mday=8, tm_hour=14, tm_min=57, tm_sec=54, tm_wday=0, tm_yday=160, tm_isdst=0)
                                                                                     一周的第几天[0,6] :0代表周一
                                                                                      一年的第几天
                                                                                       当前是否为夏季                                                                                 
 '''
structtt=time.strftime('%Y-%m-%d  ',structt)
print(structtt,"重新对结构化的数据进行格式化")

import datetime

#d=datetime.time.strftime()

#print(d)



import  calendar
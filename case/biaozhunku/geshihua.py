

''' 格式化字符串 '''

'''
字符串格式化： 
               百分号将字符串转化为其他类型，
               字符串中用大括号占位，符字符串的format/format_map方法。 
               字符串的join方法
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



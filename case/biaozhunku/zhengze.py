import re

'''
正则表达式进行匹配后输出目标的索引、替换、分割等操作。
正则本身是为了查找，至于查找后的后续结果就是多种样的
'''
st="daskjdk0980989ZDSDDSiuiu看见  323 、 \s"

teshuzifu=re.search(r'\d{7}',st)#匹配到第一个字符串。
 # 返回他的信息,
# 如果找到的话，返回的是一个对象
#  span:为匹配到的开始下标和结束下标,match为匹配到的元素值,可以直接用group()方法返回匹配到的元素
# 如果没找到返回 None
print(teshuzifu,teshuzifu.group())

fall=re.findall(r'\d',st) #findall将全部匹配的结果返回一个列表。
print(fall)

sub=re.sub(r'\d','-',st) # sub 替换,贪婪模式
print(sub)

subn=re.subn(r'\d','=',st,count=5) #subn 替换，指定替换的次数
print(subn)

'''
match 匹配：如果字符串开头的零个或多个字符与正则表达式模式匹配，则返回相应的匹配对象
  。None如果字符串与模式不匹配，则返回；否则返回false。请注意，这与零长度匹配不同。
'''

m=re.match(r'\w{8}',st)  #从开头完全匹配8个字母或数组，如果中间有任意一个不符合就返回None
print(m.group(),"使用match从开头完全匹配")


fm=re.fullmatch(r'\S',st)
print(fm,"这个fullmatch 要求更严格，要求完全符合，包括长度")



'''
编译正则表达式：将正则表达式模式编译为正则表达式对象，

 re.compile使用compile 编译正则表达式返回的对象可以直接调用 正则的serch ()和match()方法
'''


rc=re.compile(r'\d{2}')# 匹配2个
result=rc.search(st).group()
print(result,"使用编译后的对象，这个对象调用serch方法，传入字符串对象进行匹配")


'''   finditer:返回一个可迭代对象，可以遍历后调用group()方法输出。和findall()最后的结果类似。'''
it=re.finditer(r'\d',st)
print(it,"finditer:返回一个可迭代对象，可以遍历后调用group()方法输出。和findall()最后的结果类似。")
for i in it:
      print(i.group())

'''
re.split():正则的切片，可以指定切片的次数，如果不指定默认是贪婪匹配。maxsplit=3的话，只进行3次切片，返回4个列表元素
'''
sp=re.split(r'\s',st,maxsplit=3)
print(sp)



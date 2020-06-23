import re

'''
字符串切割：  re.split
将符合条件的给取出，然后将用源字符串去减到这些内容。
将元素切割为几个不同的部分，返回为列表
 re.split(pattern,string,flags=0)
 re.split(分隔符的正则表示，原字符)
 
 
'''
strl="one   tow  three  four"
print(strl.split(" ")) #如果用字符串 切割的话，会将每个空格
print(re.split(r" +",strl))# 空格+ 作为分隔符

'''
re.finditer函数
功能：与findall，扫描整个字符串，返回的是一个迭代器

'''
str2="duanbibo is goodman ! duanbibo is superman"
d=re.finditer(r"(duanbibo)",str2)
for i  in d:
      print(i)

'''
字符串的替换和修改  re.sub()
  返回为替换后的字符串
 sub(pattern,repl,string,count,flags=0)
       正则  ，替换为 ，待替换字符串，替换几次 默认所有
'''
str3=re.sub(r"(d[a-z]{3})","dan _ ",str2,)
print(str3,"------------")

'''
分组：
概念;除了简单的判断是否匹配之外，正则还有提取子串的功能。
re.match(  pattern，string)
     pattern进行分组 r"()-()-()"
     用()表示的就是提取分组 ，各组中用 - 进行间隔
使用序号获取组内的对应信息  
      group(0) 表示原始字符串
      group(1) 表示第一组字符串
       group(2)   表示第二组字符串
可以对组起名字 ,在组括号前面  (？P<组名> 表达式)
      r"(?P<name>\d{3})-(\d{8})"
'''
str4="010-45678906"
m=re.match(r"(?P<name>\d{3})-(\d{8})",str4)
print(m.group(0))
print(m.group("name")) # 使用起名后的组
print(m.group(1))
print(m.group(2))

'''
re.compile
编译：当我们使用正则表达式时，re会干这件事
 1.编译正则表达式，如果正则表达式本身不合法，会报错
 2.用编译后的正则表达式去匹配对象

'''
pat=r"^1(([3578]\d)|(47))\d{8}$"
re_telephon=re.compile(pat)   #编译后的正则表达式对象

#使用的使用直接可以传参就可以
print(re_telephon.match("13812345708"))
print(re_telephon.search("13812345708"))







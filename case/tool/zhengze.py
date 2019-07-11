import re
'''
re.match 函数
原型：match(pattern,string,flags=0)
patter: 匹配的正则表达式
string：匹配的字符串
flags=0 标志位，用于控制正则表达式的匹配方式
 re.I    忽略大小写
 re.M    多行匹配
 re.S    匹配包括换行符在内的所有字符
参数：
功能:从头开始匹配，返回None 或者位置


'''

a=re.match("C","cac",flags=re.I)
print(a)
if a==None:
      print("fail")

'''
re.search函数
功能：返回第一个成功的匹配
'''
b=re.search("w","ijoiw")
print(b)

'''
re.findall函数
功能:扫描整个字符串，并返回结果列表list
'''
b=re.findall(".","Abcadab",flags=re.I)
print(b)

'''
正则的写法
匹配内容
.                           匹配任意字符
[0-9],[a-z] ,[abc] [01]    匹配列表内任意的字符
[0-9a-zA-Z_]                   匹配任意数字、字母和下划线
^[0-9a-z]   [^a-z]          脱字符。不匹配集合之中的字符  
 \d   \D         数字，非数字，相当于[0-9] [^\D]
 \w   \W       匹配[0-9a-zA-Z_] 数字，字母，下划线
 \s    \S        匹配任意的空白符 (空格、换行、回车、换页、制表) \f \n \r \t
^  $                行首匹配，行尾匹配
\A               匹配字符串开始，和^区别是,\A只匹配整个字符串的开头
(xyz)               用小括号当做整体去匹配 
   匹配模式次数
 贪婪匹配：主要匹配的结果符合，就一直匹配下去，进行叠加
*                 0次或者多次
？               0次或者1次 ，
     *？ +？ x?          用来解决贪婪模式
+                 1次或者多次
  {m,n}            匹配m-n次
  x|y                  匹配的是x或者y
  
'''
print(re.search("[a-z]","kjk4"))
print(re.findall("[^a-z]","kj7J4_"))
print(re.findall("[\s]","kj7J4\t _"))
print(re.search("^[4]","kj7J4\t _"))
print(re.findall(r"[a-z]{3,3}","kj7jbj4m3jg5sJgg4\t _"))
print(re.search(r"(jj)","kj7jj4m3jg5sJg4g4\t _"))
print(re.search(r"^4m3$","kj7jj4m3   jg5sJg4g4\t _"))
st="dsadsadsa1 - dsadsa _dsad !@# 3432"

print("-------")
print(re.findall(r"^dsa[a-z]+",st))

def checkPhone(str):
       #1开头，第二位是[3,5,7,8],8位数字，最后一位数字结尾
     # pat=r"^1[3578]\d{9}$"
      pat=r"^1(([3578]\d)|(47))\d{8}$"
       #147开头的
      res=re.findall(pat,str)
      return res

print(checkPhone("15688888888"))

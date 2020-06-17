import time
import os
from datetime import datetime

'''以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符 分隔符.join(seq)
   相当于进seq[0]+str+seq[1]+str
'''
strz="i\"m  \n   duanbibo"    #转义符 \+"特殊标志的符号" 输出  特殊符号
lujing="C:\\Users\\87842\\Desktop\\Work"
'''
window下的路径是 反斜杠--转义符号，需要进行反转义,转义的目的是让解释器理解这不是转义符号，仅仅是一个字符
#需要将路径进行转义 ，将里面的反，因为\+字母等开头的话，解释器有可能理解为特殊指令。如\\u \\t \\n  进行反转义
转义： n换行 v 纵向制表符 t 横向制表符  r 回车 f翻页 
'''
plujing=os.path.dirname(__file__)# 获取父类的路径
print(lujing)
print(plujing) #python下，输出的路径是斜杠，
print(strz)
str1="abc757344"
z='-'.join(str1)
print(z)
str2="admin"
op=str2.join("a")
print(op)

'''字符串切割  ,返回一个列表,后面跟切割符号,进行切割多少次
  如果没知道分隔符的话，默认将字符串转化为列表
'''
print(str)
str1='1234567890'
strlip=str1.split("5")
print(strlip,"qiege")

'''  利用split 获取url的最后一个路径 '''
strurl='http://www.baidu.com/dsa/89/'
value=strurl.split('/')[-2]
print(value,'=====================')


'''
格式化方法  
         1. %s字符 %d十进制 %f浮点类型  
                  如果需要精度的话，%.2d 代表小数点后2位小数
         2.{}{}.format([列表],(元祖))
'''
zz="zhangyuqi  %s"
print(zz%"aini")

im="duanbibo"
print("my name  is %s,%d，%.2fm"  %(im,15,1.74))
#多个需要格式化的参数用一个%，然后把所有参数括起来
# ，需要保证需要格式化的数量>=参数数量
#如果不匹配的话，就会循环使用参数内的数据

kong="my name is {0},i hava {1}age,{2:.2f}cm"
#在声明字符串的时候，在内部用占位符{}表示，
#{}{} ,再占位的时候默认第0,1个，可以
#但是可以自定义控制取的参数是哪个 。如{1}{0} 代表：取 格式化参数的顺序
#   :.2f 是集合内固定的写法， 效果与  %.2f ，一样。对数据进行保留小数点后2位小数
#在进行格式化的时候，调用format内部的变量，传入禁区
print(kong.format("duanbibo","26",1.74))
info=['chenyingmei','27',1.74]
#格式化的参数，可以用数据结构列表、元祖来放入，
# 但是参数列表的时候需要依次取出
print(kong.format(info[0],info[1],info[2]))
infot=('chenyingmei','27',1.74)
print(kong.format(infot[0],infot[1],infot[2]))

#用字典存放格式化参数，取的时候是根据key来取value做参数化的值
#使用字典的时候，需要进行解包
#需要在定义字符串的时候，在集合声明接受的key值，再format的时候实现自动解包
#解包的**数据类型 ，就是一个不定长参数（**kwargs）:代表键值对的参数字典
sd="我们是{student},我们的目标是上{daxue}"
infodict={"student":"高考生","daxue":"清华"}
print(sd.format(**infodict))






'''  将字符串的大小写反转'''
str1.swapcase()



'''获取当前的时间'''
a=datetime.now()
print(a)
now = time.time()

'''格式化年月日时分秒'''
local_time = time.localtime(now)
date_format_localtime =  time.strftime('%Y-%m-%d %H:%M:%S',local_time)
print(date_format_localtime)
'''以XX字符分割原字符串，形成列表'''
slist=date_format_localtime.split(" ")
print("日期分割后的列表分别为为%s"%slist)
ltime=slist[1].split(":")
print("时间分割后的列表分别为%s"%ltime)



'''
time=time.strftime('%Y-%m-%d %H:%M:%S',a)
# print(time)
字符串替换  (old ,new ,times) 指定替换的次数
'''

strg="aabbcdbaaabc"
strg=strg.replace("ab","--")
print(strg)

'''字符串截取切片[x:y:z]在x-y的范围内，每隔在个数字进行截取,返回为截取的值,即'''
a=strg[1:5:2]   #截取的结果为用一个变量接受： bd
print(a+"就是你了")
cou=strg.count('a')
print("a出现了%s次"%cou)

'''字符串转换,字符串可以转换为list列表，tuple，但是不能转换为字典'''
abc=(2,3,4,5,6,7)
abc=list(abc)
print(abc)
abc=tuple(abc)
print(abc)

'''将字符串进行每三个进行倒序
range(开始位置，结束位置，间隔单位)
s[i:i+3]将列表的每3个元素进行切割，分为一个列表；
[::-!]  将列表进行反转'''


s = "123456789"
lis = ''.join([s[i:i+3][::-1] for i in range(0,len(s),3)])
print(lis)

'''range 在迭代器中进行取数规则'''
print([s[i:i+3] for i in range(0,len(s),3)])
for i in range(0,9,3):

      print(i)
'''判断字符串的开头/结束值 返回值为True/False'''
Ls="  zy34324"
'''判断字符串内的元素全部是否数字'''
print(Ls.isalpha())
print(Ls.isalnum())
print(Ls.isdigit())#是否数组
print(Ls.islower())#是否全部小写字母
print(Ls.startswith('z'))
'''求元素在字符串响应索引位置，返回-1时，表示不存在'''
print(Ls.find('3',0,5))
'''指定元素出现的索引,和find方法一致'''
print("索引%s"%(Ls.index('3')))
'''将全部字母进行大写'''
print(Ls.upper())
'''将字符串的前后空格进行去掉'''
print(Ls.strip())
#将开头字母大写
print(Ls.capitalize() )
#计算字符串的长度
print(len(Ls))

'''字符串的属性和方法'''
print(dir(Ls))

'''
将字符串中的元素，作为分隔符，将字符串分割为几个不等的列表
 (value,times)  以字符串的哪个元素作为分隔符，进行分割多少次，-1默认全部，可以不填。
 '''
print(Ls.split("3",5))


''' 比较2个字符串的相应的元素是否一致'''
strbefor="123456"
strafter="167890"
print("这俩字符是%s,%s"%(strbefor[0:2],strafter[3:5]))


'''
 if条件1 执行语句,elif条件2 执行语句 ,elif条件3  执行语句, else 执行语句
  可以在条件语句外面添加 try。。finally 进行每个分支都进行执行这段话
'''
try:
  if int(strbefor[0:2])==int(strafter[3:5]):
      print("相等")
  elif int(strbefor[0:2])>int(strafter[3:5]):
      print("前面的大")
  else :
      print("后面的大")
finally:
      print("他俩之和为,%d"%(int(strbefor[0:2])+int(strafter[3:5])))

'''
将字符串，添加分隔符
使用正则表达式
123456 变为12:34:56
思路:  1.将匹配的进行分组用() 进行
       2.由于分组的内容是迭代器。所以直接用符号.join(groups)
'''
import re
stri="123456"

pat=r"([\w]{2})([\w]{2})([\w]{2})"
nj=re.search(pat,stri)
print(":".join(nj.groups()))




'''
数字串添加分隔符
12345678 变为 123,456.78
思路： 
    1.判断长度为2位数 1位数，进行 增加0.0 或者 0.
    2.长度大于2位时，
'''
nm="123456"
def parse(n):
      if len(n)==1:
        return '0.0' + str(n)
      elif len(n) ==2:
         return '0.' + str(n)
      else:
         l = n[0:-2]
         lis = []
         for i in range(len(l),0,-3):  # 关键这一部，i的取值是每隔3个数来取的
            if i >3:
                  lis.append(l[i-3:i])
            else:
                  lis.append(l[0:i])
      lis=list(reversed(lis))
      return ','.join(lis)+'.'+n[-2:]
print(parse(nm))

'''
将  123,456,789.89 进行还原为 字符串  123456789
 思想：分为2部分 ，第一部分为小数点后面的；第二部分为小数点前面的。
      第一部分和第二部分 可以根据切片来获取 [0:-3] ,[-2,len(str)]
      第二部分的操作，直接用split(",")切片获取，返回为切割后的列表
'''
strh="1,234,567.89"
def huanyuan(a):

      listbefore=strh[0:-3]     #获取
      listafter=strh[-2:len(strh)]
      aa=listbefore.split(",")
      strss=''.join(aa)
      print(strss+listafter)

huanyuan(strh)
'''
需求：将列表元素进行组合，为 11,111,18,2,23,46
  解决思路： 根据ASCII码排序规则，将数字转换为字符类型。字符类型排序时，会根据每个字符的首位进行排序。
             比如说  z>zx>d>bx>b>af>a
            sorted 就是这种倒序规则,它只不过是倒序了而已。 
            所以实现的方式:只需要  
'''
s = "123456789"
lis = ''.join([s[i:i+3][::-1] for i in range(0,len(s),3)])
print(lis)

listh=[2, 23,18, 11, 111, 46,9,98]

print(sorted(one for one in listh))
print( [int(two) for two in(sorted(str(one) for one in listh))])
print("----------"*8)
ll= ['a:1', 'b:2', 'c:3']
# print( {k:v for j in z for k in j.split(":")[0] for v in j.split(":")[1]})
# print({str(i.split(':')[0]):int(i.split(':')[1]) for i in a})
dic = {}
for i in ll:
    dic[i[0]] = i[2]
print(dic)
'''sort  排序'''

'''repr函数 和 str函数'''
zz=45
print(repr(zz),type(repr(zz)),type(str(zz)))
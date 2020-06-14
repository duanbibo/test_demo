import collections


#counter ：简单的计数器，返回一个字典，显示字符串中各个字符出现的次数
cd=collections.Counter('dksdasjdhasjhdjkas')
print(cd)

c = collections.Counter()
for ch in 'programming':
     c[ch] = c[ch] + 1
print(c)


#deque 双端队列 ,提供了append，pop的left操作的方法
link=collections.deque()
link.append('one')
link.appendleft('appendleft')
#link.popleft()  #从左边删除
link.append('three')
link.remove('appendleft')
print(link)

#OrderDict  提供有序字典
order=collections.OrderedDict()
order[1]="1"
order[0]="0"
print(order)

#nametuple 具名元祖，可以对元组内的每一个值进行命名
city=collections.namedtuple('city','name  jvli   play   price   pingjia  ')
beijing=city('gugong','888km','guanjing',50,'yiban')
print(beijing)
print(beijing.jvli)


login_user=[  (r'http://www.baidu.com', 'usr1', 'pwd1'),
    (r'http://www.youdao.com', 'usr2', 'pwd2'),
    (r'http://mail.126.com', 'usr3', 'pwd3')]

page_info=collections.namedtuple('login_info',['url','username','password'])
for user in login_user:
      x=page_info(*user)
      print(x)


#根据列表嵌套的元祖，将列表中的元祖指定的字段值进行排序

from operator import  itemgetter
'''   itemgetter : 构造器内是下标，将数据按照给定的下标 进行排序  ，
 一般与  sorted( data  ,key=itemgetter(0)) 一起使用   '''

data=[ (1,"张三",18),(0,"李四",16),(3,"王五",12),(2,"赵六",11),(5,"田七",9)]

#首先利用sorted函数进行排序升序，key可以指定可迭代对象的哪个字段值
# itemgetter中的参数为一个时，实现按照可迭代对象中的 第一个值对排序输出
#当itemgetter中的参数为多个时，只输入指定的参数


for info in sorted( data,key=itemgetter(0)):
      print(info)


for info2 in sorted( data,key=itemgetter(0,1)):
      print(info2)

'''  利用上面学习到的具名元组，将没有字段名称的元祖通过
     利用声明的具名元组的工厂函数，将原始数据传入到具名元祖内*自动拆包 进行赋值到一个变量内。'''
all=[]
data2=collections.namedtuple('user_info','name mingci age')
for user in data:
      one=data2(*user)
      all.append(one)
print(all)






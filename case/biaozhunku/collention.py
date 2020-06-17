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

'''
  #nametuple 具名元祖，可以对元组内的每一个值进行命名,
   添加数据： make方法，为具名元祖添加数据。添加可迭代对象，传递的参数个数必须与声明的具名元祖个数一致，只能一个一个添加。如果有多条，先用for循环迭代
              利用具名元祖的指定的参数列表的构造器添加。  推荐使用make方法
            _asdict方法：将具名元祖转换为有序字典OrderDict。
'''
city=collections.namedtuple('city','name  jvli   play   price   pingjia  ')
#利用具名元祖返回的函数，添加单条数据，相当于走的是构造器按照每个字段赋值
beijing=city('gugong','888km','guanjing',50,'yiban')
print(beijing,"利用具名函数的构造器添加的数据")
print(beijing.jvli)

#利用make函数将数据包装为可迭代对象作为参数传入。通过具名函数调用
yizu=['gugong','888km','guanjing',50,'yiban']
zidianzu={ 'name':'yiheyuan','jvli':'99km','play':'youwan','price':'100','pingjia':'haixing'}
m1=city._make(yizu)
print(m1,"利用具名函数的make方法添加可迭代对象列表为参数，添加数据")
m2=city._make(zidianzu)
print(m2,"利用具名函数的make方法添加可迭代对象字典为参数，添加数据")
d1=m1._asdict()
print("利用具名元祖的asdict方法把它转换为有序字典",d1)

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


''' ChainMap ：  将多个map连接chain在一起，提供一个统一的视图。因为是视图，所以原来的map不会被影响'''

datadict1={'a':1,'c':2}
datadict2={'b':2}
datadict3={'c':'3','d':4}
cmap=collections.ChainMap(datadict1,datadict2,datadict3)
print(cmap,"ChainMap连接的多个字典中，不同的字典key值不起冲突")
print(cmap.get('d'),"在视图内 获取多个字典内的key指定的value，会遍历所有的字典，如果字典内有相同的key，优先匹配第一个")
print(cmap.maps,"返回的是一个统一视图，可以调用maps方法将返回列表嵌套的字典")
print(cmap.__len__(),"获取链路map的大小")


'''  利用collections工具类判断一些数据类型是否为可迭代对象,迭代器'''
from collections import Iterator,Iterable

dict1={'1':2,'3':4}
t=(1,2,3,4,5)
print(isinstance(dict1,Iterable),isinstance(t,Iterable))
print(isinstance(dict1,Iterator),isinstance(t,Iterator))






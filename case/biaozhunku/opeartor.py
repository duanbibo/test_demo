import operator
from operator import mul
from operator import itemgetter
from operator import attrgetter
'''
operator 库主要提供了一些简便的操作类 ，能替代从序列中取出元素或者读取出对象属性的lamdba表达式
       ，大部分是一些比较类，如判断大小，取模，平方等
         
     itemgetter:根据元祖的某个字段将元祖列表排序，参数是字段的下标
'''

data=[('北京',100,'just'),('上海',80,'well'),('tokyo',120,'nice'),('newyork',70,'good')]

paixu=sorted(data,key=itemgetter(1))
print(paixu) #[('newyork', 70, 'good'), ('上海', 80, 'well'), ('北京', 100, 'just'), ('tokyo', 120, 'nice')]

new=itemgetter(0,2)
for pingjia in data:
      print(new(pingjia))

''' 利用 attrgetter 主要用在面向对象的类上面，将对象按照构造器内的属性进行排序，
    不能够重新构造对象，也不能改变单个对象中的位置。
   '''
class user():

      def __init__(self,name,age):
            self.name=name
            self.age=age
      def __str__(self):
            return self.name,self.age

      def say(self,x):
            return  "我明年要 %s 岁了" %(self.age+x)
      def __repr__(self):
            return repr((self.name,self.age))



objectdata=[user('zhangsan',15),user('lisi',20),user('wangwu',17)]
print(objectdata)

paixu=attrgetter('age')
objectpaixu=sorted(objectdata,key=paixu)
print(objectpaixu,"使用attrgetter将列表中嵌套的对象按照指定属性值排序")

#也可以使用原始的lamdba函数
objlambdapaixu=sorted(objectdata,key=lambda o:o.age)
print(objlambdapaixu,'完全使用lambda函数对列表嵌套的多个元祖排序')


'''  methodcaller :自行创建函数，创建的函数会在对象上调用参数指定的方法'''

from operator import  methodcaller
st=" abcdefg"
upcase=methodcaller('upper')
print(upcase(st))
print(st.upper())
    #调用面向对象中过的方法。
user=user('麦斯',29)
user_say=methodcaller('say',1)
print(user_say(user))
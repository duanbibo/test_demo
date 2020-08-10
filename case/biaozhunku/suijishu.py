import random

#使用random库中的random生成的数字默认是0-1之间的小数
xiaoshu=random.random()
print(xiaoshu)

r=random.randint(60,100)
print(r)


#随机数生成
i=random.randint(40,90)/100
print(i)

rl=[135,145,138,158,189][random.randint(0,4)]
#维护个列表，列表存放合法的手机开头3位数组
#然后产生一个【0，数组长度-1】的随机数，当做这个列表的下标，进行取数。
print(rl)

end=random.randint(0,99999999)
#生成个后9位的随机数，这个随机数
#将2个随机数转化为字符串类型，然后拼接
tel=str(rl)+str(end)
print(tel)

#random.sample( 字符串，长度)   从迭代对象中依次生成指定个数的随机数
s=random.sample("1234567890",2)
print(s,"sssssssssss")

#randrange ,指定生成的数字符合一定的步长
si=random.randrange(0,99,4)
print(si)

#choices:从任何类型中选择一个数据，返回一个列表
anytype=[0,(3,4)]
any=random.choices(anytype)
print(any)

#洗牌操作，只对数据进行重排序，无返回值
shu=[0,1,2,3,4,5,6,7,8,9]
random.shuffle(shu)
print(shu)

#choies 从集群中选中数据，可以设置权重 ,以下的权重为前几位不进行抽取，从后四位
ten=[0,1,2,3,4,5,6,7,8,9]
c1=random.choices(ten,weights=[0,0,0,0,0,0,1,1,1,2],k=5)
c2=random.choices(ten,cum_weights=[0,0,0,0,0,0,1,2,3,5],k=5)
print(c1,c2)


#写一个func，根据传入的参数生成指定类型的随机字符串
''' 需要解决的问题：
1.每次生出来的都是列表内的一个元素，所以需要利用字符串的join方法，利用空格将列表的每个元素拼接返回一个str的数据
2.如果生成的类型为数字，第一位永远不可能是0，所以在执行时需要判断 如果小于1位在0-9中执行，如果大于2位
'''
def suiji(lei,cishu):
      if lei=='int':
            if cishu==1:
                  new = random.sample("123456789", cishu)
                  return  "".join(new)
            else:
               one=random.sample("123456789",1)
               same=random.sample("123456789",cishu-1)
               return  "".join(one)+"".join(same)
      elif lei=='str':
        return "".join(random.sample("abcdefghizj",cishu))

i=suiji('int',1)
print(i)
s=suiji('str',8)
print(s)
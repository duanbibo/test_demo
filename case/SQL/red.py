import redis
r=redis.Redis(host='localhost',port='6379',decode_responses=True,password='duanbibo')
#r=redis.Redis(connection_pool=pool)
#r.set('age',27)
#redis取出的内容默认是字节
r.incr('age',amount='5')   #
age=r.get('age')
#d=r.delete('age')

print(age,type(age))

#添加object类型的数据， hset(对象，属性，属性值) ,hmset
r.hset("room","bed","2m",)
r.hset("room","book",5)
objectdict={"k3":"k3","null":" "}
r.hmset("piliangobject",{"k1":"v1","k2":"v2"})  #批量添加一个对象的多个属性，需要2个参数第一个是对象，第二个是属性和值组成的字典
r.hmset("piliangobject",objectdict)
bed=r.hget("room","bed")
obj=r.hgetall("room")           #获取当前对象所有的属性和属性值，
print(bed)
print(obj,type(obj))
# r.hdel(name ,*key)  将name对应的key属性键值对删除
print("打印某一个hash对象的键值对个数",r.hlen("piliangobject"))  #获取hash类型 key数量



#添加列表类型的数据  lpush(列表的名字，*列表的值)
r.lpush("list","list1","list0","list001")
r.lpush("list","list2")
all=r.lrange("list",0,10)   #获取列表的值  r.lrange(列表名，起始位置，结束位置)
r.lset("list",5,"list5") #添加列表中指定索引位置的数字
l=r.lindex("list",7) #获取列表指定索引的值
print(all,l)


#添加无序列表 set ,内部值不能相同，集合主要的作用就是用来交、并、差集的计算，很少直接输出一个集合的内容
r.sadd("set","set0","set1")
r.scard("set")  #获取集合内个数
r.sadd("s","set0","set3")
print(r.sdiff("set","s"))  #比较两者不同，第一个集合减去两个集合公共部分

print(r.sinter("set","s"))     #获取两个集合内的交集
r.sinterstore("jiaojiset","set","s")   #获取连个集合的交集，并将存入一个集合中。

#zset为有序列表



#删除任意类型的数据 ，根据name名称
b=r.exists("age")   #检测redis中任意类型的name是否存在
print(b)


#管道技术，py-redis默认每次执行的时候都需要创建链接，使用管道技术可以在一个请求中执行多个命令
pipe=r.pipeline()
pipe.set('one','second')
pipe.set('two','sencond')
pipe.execute()

pipe.set('lianlu','lianlu').hset('lianluobject','shuxing1','value1').hset('lianluobject','shuxing2','value2').execute()
import redis

r.subsribe('redis').parse_response()
r.publish('redis','me')
print(r.parse_response())
class RedisHelper:

    def __init__(self):
        self.__conn = redis.Redis(host='localhost')
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'

    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()  # 打开收音机
        pub.subscribe(self.chan_sub) # 调频道
        pub.parse_response()  # 准备接收
        return pub

obj1 = RedisHelper()
redis_sub = obj1.subscribe()

while True:
    msg= redis_sub.parse_response()
    print (msg)


obj2.public('hello')
import redis

conn = redis.Redis(host="127.0.0.1", port=6379, decode_responses=True,password='duanbibo')

#可以将redis内的数据发送出去
string_value=conn.get("age")
hash_value=conn.hgetall("room")
print(hash_value)
r=conn.publish("gaoxin333", hash_value)
print(r)
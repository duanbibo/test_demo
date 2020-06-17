import redis
import time

conn = redis.Redis(host="127.0.0.1", port=6379, decode_responses=True,password='duanbibo')

# 第一步 生成一个订阅者对象
pubsub = conn.pubsub()

# 第二步 订阅一个消息

pubsub.subscribe("gaoxin333")

# 创建一个接收

while True:
    #print("working~~~")
    time.sleep(1)
    msg = pubsub.parse_response()
    print(msg)
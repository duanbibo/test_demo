#coding=utf-8
import requests
print("hello word")

print(" webhook begin")


#自定义钉钉机器人的url
url="https://oapi.dingtalk.com/robot/send?access_token=878e9edb2c45ef7aab6024d64c76120a1397991e9d07fca14853ff6e5b61e659"

headers = {
"Content-Type": "application/json ;charset=utf-8 "
}
body={
      "msgtype": "text",
      "text": {
            "content": "测试执行成功，查看测试报告，http://121.36.102.233:8090/"
      }
}
r=requests.request("post",url=url,headers=headers,json=body)

print("webhooks end")


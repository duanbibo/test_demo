import requests

url="https://oapi.dingtalk.com/robot/send?access_token=878e9edb2c45ef7aab6024d64c76120a1397991e9d07fca14853ff6e5b61e659"

headers = {
"Content-Type": "application/json ;charset=utf-8 "
}
body={
      "msgtype": "text",
      "text": {
            "content": "测试执行成功，查看测试报告，http://121.36.102.233:8080/"
      }
}
r=requests.request("post",url=url,headers=headers,json=body)
res=r.content
print(res)
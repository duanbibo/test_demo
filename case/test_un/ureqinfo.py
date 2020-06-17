from ddt import *
from .read_e import *
import unittest
import requests
import time
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urllib3.PoolManager(num_pools=100000)

@ddt
class Testinfo(unittest.TestCase):

 @data(*one)
 @unpack
 def test_login(self,name,uname):
       url ='https://api.xinzhili.cn/v0/oauth/token'
       data = {
             "device_type": "android",
             "password": "111111",
             "device_token": "0f86eb7fd5a14e8dcdbbfac9f555da99",
             "username": int(uname),
             "grant_type": "password"
       }
       headers = {
             'Authorization': 'Basic cGF0aWVudF9hcHA6'
       }
       print(data)
       res=requests.post(url=url,data=data,headers=headers,verify=False)
       #global token
       assert "access_token" in res.json()
       token = res.json().get("access_token")
       #time.sleep(2)

       url2 = 'https://api.xinzhili.cn/v0/patient/user'
       data2={

                  "name": "{0}".format(name),
                  "tel": "{0}".format(uname),
            }

       headers2 = {
            'Authorization': 'bearer {0}'.format(token),
           'Content-Type': 'application/json'
       }
       print(token)
       print(headers2)
       result= requests.put(url=url2,json=data2,headers=headers2,verify=False)

       print(result.text)


 if __name__ == '__main__':
       # 实例化TestSuite创建测试套件
       suite = unittest.TestSuite
       # 把用例test_01添加到测试套件中
       suite.addTest(test_login)
       # run()方法是运行测试套件的测试用例，入参为suite测试套件。
       unittest.TextTestRunner().run(suite)


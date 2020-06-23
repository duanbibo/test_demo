from ddt import *
from .read_e import *
import unittest
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def updata(uname,name,idcard,sex):
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

       url2 = 'https://api.xzlcorp.com/v0/patient/user'
       data2={
                 "idCard": "{0}".format(idcard),
                  "name": "{0}".format(name),
                  "sex": "{0}".format(sex),
                  "tel": "{0}".format(uname),
            }

       headers2 = {
            'Authorization': 'bearer {0}'.format(token),
           'Content-Type': 'application/json'
       }
       print(token)
       result= requests.request("put",url=url2,json=data2,headers=headers2,verify=False)
       print(result.text)
       assert "success" in result.text











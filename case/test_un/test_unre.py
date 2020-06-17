from ddt import *
from .read_e import *
import unittest
import requests
import HTMLTestRunner


@ddt
class TestRq(unittest.TestCase):

 @data(*lie)
 @unpack
 def test_zhuce(self,tel):
      url = 'https://api.xinzhili.cn/v0/oauth/token'
      data = {
            "device_type": "android",
                "password": "111111",
                "device_token": "0f86eb7fd5a14e8dcdbbfac9f555da99",
                "username": int(tel),
                "grant_type": "password"
      }
      print(tel)
      headers = {

             'Authorization': 'Basic cGF0aWVudF9hcHA6'
      }
      result= requests.request('post',url=url,data=data,headers=headers,verify=False)
      print(result)
      assert "access_token" in result.json()
      token = result.json().get("access_token")
      print(token)

if __name__ == '__main__':

       print("11111111")
       # 实例化TestSuite创建测试套件
       suite = unittest.TestSuite()
       # 把用例test_01添加到测试套件中
       suite.addTest(TestRq("test_zhuce"))
       # run()方法是运行测试套件的测试用例，入参为suite测试套件。
       rp = open('./result.html', 'wb')
       runner=HTMLTestRunner.HTMLTestRunner(stream=rp, title=u'测试报告', description=u'用例执行情况：')
       runner.run(suite)
       rp.close()




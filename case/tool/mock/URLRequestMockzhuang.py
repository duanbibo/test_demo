import unittest
from unittest import mock
from unittest.mock import patch


from .URLRequest import PayAPI
'''
通过装饰器的写法，实现mock  ， @patch.object(mock的class，’mock的方法‘)
          测试函数，需要额外传一个形参数，mock函数，实际上相当于装饰器参数组合返回的一个实例
'''
class TestPayApi(unittest.TestCase):


      #将创建待mock的类实例
      def   setUp(self) :
            self.instance=PayAPI()


      @patch.object(PayAPI,'auth')
      def  test_success(self,mock_auth):
            mock_auth.return_value={'status_code:''200'}
            status=self.instance.pay('id',"cdcard",'5555')
            self.assertEqual(status,'支付成功')

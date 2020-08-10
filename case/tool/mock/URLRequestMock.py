import unittest
from unittest import mock



from  .URLRequest import PayAPI


'''

Mock的第二种场景：
  第一个接口未开发完毕后，第二个接口依赖第一个接口，可以直接用第一个接口mock的返回值。
'''

class TestPayAPI(unittest.TestCase):



      def test_success(self):
            pay=PayAPI()
            pay.auth=mock.Mock(return_value={'status_code':'200'})
            status=pay.pay('1000','123456','10000')
            self.assertEqual(status,"支付成功")



      def test_fail(self):
            pay = PayAPI()
            pay.auth = mock.Mock(return_value={'status_code': '500'})
            status = pay.pay('1000', '12345', '10000')
            self.assertEqual(status, '支付失败')

      def test_error(self):
            pay = PayAPI()
            pay.auth = mock.Mock(return_value={'status_code': '300'})
            status = pay.pay('1000', '12345', '10000')
            self.assertEqual(status, '未知错误')

      def test_exception(self):
            pay = PayAPI()
            pay.auth = mock.Mock(return_value='200')
            status = pay.pay('1000', '12345', '10000')
            self.assertEqual(status, 'Error, 服务器异常!')


if __name__ == '__main__':
    unittest.main()
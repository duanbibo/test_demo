#mock
from mock import  Mock
import unittest
from unittest import  mock


'''
使用mock模块，对于python2 mock需要单独下载，python3内置在了unittest框架里面


这里mock只用于mock一个尚未完成的函数，
     1.需要利用Mock()类创建实例， mock的函数=Mock(  函数的返回值)
     2.调用mock的函数传入实参，并且找个变量接受它
     3.断言  变量的值是否等于在创建mock时的mock的返回值。
     
     

'''

def  func(p1,p2):
      pass


class SubClass():

      #待mock函数只需要定义参数列表 就可以了
      def add(self,a,b):
            pass

class TestSub(unittest.TestCase):

      def test_mkfunc(self):
            func=mock.Mock(return_value=2)
            result=func(1,1)
            self.assertEqual(result,2)
      def test_sub(self):

            #创建mock类的实例
            sub=SubClass()

            #调用mock库的Mock类创建实例。  类实例.函数=mock(函数的返回值)

                            #当它为
            sub.add=mock.Mock(return_value=10)
            #调用mock方法，传入实参
            result=sub.add(5,5)
            self.assertEqual(result,10)

      def test_sub2(self):

            #创建mock类的实例
            sub=SubClass()

            #side_effect:当添加这个参数的时候return_value就会失效，mock就不起作用了
            #目的在于减少代码的重新变动
            sub.add=mock.Mock(return_value=10,side_effect=sub.add)
            #调用mock方法，传入实参
            result=sub.add(5,5)
            self.assertEqual(result,10)



if __name__ == '__main__':
    unittest.main()


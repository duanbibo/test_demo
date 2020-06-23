

import pytest
# 不带参数时默认scope="function"，每执行一个；类中的函数会被多次执行。

import sys

class TestCase(pytest):



 def test_s1(self,login):
    print("用例1")
    raise  IOError   #引发异常后，使用yield 进行teardown的时候，照样能够执行剩余部分


 def test_s2(self):  # 不传login
    print("用例2：不需要登录，操作222")


 @pytest.mark.usefixtures("login")
 def test_s3(self):
    print("用例3：登录之后其它动作333")
    assert 4==7                #断言失败后，也能进行teardown部分。



  #当满足条件后，此条用例不用执行   ，然后输出摘要reson摘要 , 类型属于error
 #单独打标
 @pytest.mark.skipif(9>0,reson="ban ben tai  di le ")
 def test_skipif(self):
       print("当满足条件后，不需要执行用例了")
       assert 4 == 7  # 断言失败后，也能进行teardown部分。


  #将标机单抽取出来，使用的时候。直接放在测试函数上，当装饰器使用
 #  @标记，放在一个测试模块内，用的时候导包，能够重复使用。
 #批量打标，可以应用到所有的测试类上
 minversion_mark=pytest.mark.skipif(sys.version_info<(3.6),reson="low")

 @minversion_mark
 def test_mark_skipif(self):
       print("当满足条件后，不需要执行用例了")
       assert 4 == 7  # 断言失败后，也能进行teardown部分。


 @pytest.mark.skip(reson="这个跳过")
 def test_mark_skip(self):
       print("这个直接跳过")
       assert 4 == 7  # 断言失败后，也能进行teardown部分。

@pytest.importorskip("模块")
def test_mark_skip(self):
      print("缺少某些导入时，跳过模块中的测试")
      assert 4 == 7  # 断言失败后，也能进行teardown部分。

@pytest.mark.wew
def test_mark_skip(self):
      print("缺少某些导入时，跳过模块中的测试")
      assert 4 == 7  # 断言失败后，也能进行teardown部分。





if __name__ == "__main__":
    pytest.main(["-s", "pytest_fixtrue.py"])

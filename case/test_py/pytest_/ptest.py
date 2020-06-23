


import  pytest


#1.在内部参数化，直接参数用
# @pytest.mark.parametrize('形参参数列表1，2'，实参用元祖包括，多个实参的话，用列表包括)
@pytest.mark.parametrize('a,b',[(5,5),(6,4),(3,7),(8,2)
                                ])
 #标机单个实例的参数化结果: 标机失败的用例就不运行了，标记x
def test_add(a,b):
    def equivalent(a,b):
        return  a+b
    assert 10 == equivalent(a,b)

#2. 可以把参数列表放在同一个类内，相当于全局变量。做到分离。

from    case.test_un.outconfig import *
@pytest.mark.parametrize('a,b',dataout)
def test_add2(a,b):
    def equivalent(a,b):
        return  a+b
    assert 10 == equivalent(a,b) ,"%s  +%s 不等于10 " %(a,b)


# 3.第三部演化： 直接放在测试类上，利用pytest.param(参数1,2，id="描述信息")，方便控制台输出有效信息。
data=[pytest.param(5,5,id="5+5:passed"),
      pytest.param(6,4,id="6+4:passed"),
      pytest.param(5,4,id="5+4:failed")]

@pytest.mark.parametrize('a,b',data)
class Test_add:

    def test_add(self,a,b):
        def equivalent(a,b):
            return  a+b
        assert 10 == equivalent(a,b)


'''  组合参数化，遍历'''
@pytest.mark.parametrize('a',[1,2,3])
@pytest.mark.parametrize('b',[1,2,3])
#循环遍历，先将外层遍历，再遍历内存
def test_add(a,b):
    print('参数化组合循环比遍历{}，{}'.format(a,b))
    assert a>b ,"%s 不大于 %s"%(a,b)


'''  主动引发异常'''
@pytest.mark.parametrize('a,b',[(8,4),(1,0)])
def test_add(a,b):
     with pytest.raises(ZeroDivisionError):
         1/0

''' 跳过用例  skip'''
@pytest.mark.skip
def test_skip(a,b):
    assert a>b

''' 用例标机失败，不执行  xfail'''
@pytest.mark.xfail(reason="尚未开发完成，执行也是失败")
def test_skip(a, b):
    assert a > b


''' 参数化过程中，不执行某个参数化标机  xfail  '''
@pytest.mark.parametrize('a,b',[(6,3),(5,9),pytest.param(6,8,marks=pytest.mark.xfail)])
def test_fail_p(a,b):
     assert  a>b


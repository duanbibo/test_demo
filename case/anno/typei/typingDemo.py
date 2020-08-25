from typing import List,Tuple,Dict

'''
typing:主要通过注解方式来限制类型，主要目的还是为了嵌套时对可迭代对象的元素类型控制
        不需要控制str .主要还是可迭代对象的内部元素类型
'''

#python3.5 的类型注解
a:int=2
#python3.6 func内变量和返回值类型的注解


'''
 需求： 计算乘积，第一个是固定的被乘数，第二个是一个可迭代对象的乘数
       使用第一个方式时，由于传入字符串是也会被执行，所以不合理。
'''
#这是个没加约束的，没有定义列表内对象的类型
def scal(x,*y):
      return[x*i for i in y ]

print(scal(5,4,3))
print(scal(5,4,'y'))

li=List[int]
def scal(x,y:li):
      return [x*i for i in y ]


#定义函数参数的类型为list，并且元素为float，其实int类也行。
# 然后把这个赋值给一个变量，在使用注解时直接写变量就可以

Vector = List[float]
def scale(scalar: float, vector: Vector)->Vector:
    return [scalar*num for num in vector]

new_vector = scale(2.0, [1,1])
new_vector2 = scale(2.0, [1.0,2.5])
#new_vector3 = scale(2.0, ['1','4']) #这样是不行的
print(new_vector,new_vector2 )

'''
New  Type  新类型: 辅助函数创造不同的类型，一般用到面向对象上面
'''

from typing import NewType
UserId=NewType("UserId",int)

someid=UserId(122)
#someid=UserId('122')

#这里直接使用
def get_user_name(user_id:UserId)->str:
      pass


'''
Any是一种特性的类型，与任何类型兼容,在传入参数时不校验
'''
from typing import Any

def an(item:Any)-> int:
      return item
print(an(4),type(an(4)))


'''
回调 callable：

'''
from typing import Callable

def async_querry(on_success:Callable[[int],None],
                 on_error:Callable[[int,Exception],None]) ->None:
      ...

'''
泛型：generics ，容器中的元素类型信息由于泛型不同通过一般方式静态推断，因此抽象类必须用来拓展表示容器中的元素
           泛型数据结构   mapping  sequence  利用数据结构的抽象类，最顶层
           泛型指定的对象   TypeVar 工厂
           泛型类可以具有任意数量的类型变量，并且类型变量也能收到约束

'''
#泛型，使用数据集合的抽象类mapping和Sqquence
from typing import Mapping ,Sequence

#定义个雇员类
class Emoloyee:
      ...

def notify_by_email(employees:Sequence[Emoloyee],
                    override:Mapping[str,str])->None: ...

from typing import TypeVar

#使用泛型通配符，
T=TypeVar('T')

#将泛型的统配传入序列类中
def first(l:Sequence[T])->T :
      return l[0]

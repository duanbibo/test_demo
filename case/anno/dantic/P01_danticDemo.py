from pydantic import BaseModel  #类必须继承这个类或者被下面的装饰器修饰
from pydantic.dataclasses import dataclass

from datetime import datetime   #类的字段名为datetime 格式
from enum import Enum,IntEnum   #调用基础类的枚举类
from typing import List,Dict    #调用根据注解提示文档类型




'''
当前的实体类，必须继承BaseModel或通过类装饰器 , 
        在内部使用的时候先做:类型判断, 再做 =后面的值判断
        如果没有= 则表示该字段必传。 当= 后面有值时，不为必传，且有默认值
        对于冒号后面的类似，除了typing和基础类型之外，还可以与data,time,datatime使用
         data 在使用时是一个毫秒值；time 在使用时时一个元祖（时，分，秒），datatime是一个字符串的时间戳
'''
class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: datetime = None
    friends: List[int] = []


#基于注解的方式实现
#@dataclass
# class User2:
#       id: int
#       name: str = 'John Doe'
#       signup_ts: datetime = None
#       friends: List[int] = []


external_data = {'id': '123', 'signup_ts': '2017-06-01 12:22', 'friends': [1, '2', b'3']}
user = User(**external_data)
print(user)
print(user.friends)

from pydantic import BaseModel,ValidationError,validator
from datetime import datetime   #类的字段名为datetime 格式
from enum import Enum,IntEnum   #调用基础类的枚举类
from typing import List,Dict    #调用根据注解提示文档类型


class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: datetime = None
    friends: List[int] = []




#这里调用验证器的异常模块，当处理异常后打印异常的json()方法，每个属性都会打印属性信息，msg提示信息，type信息。
try:
    User(signup_ts='broken', friends=[1, 2, 'not number'])
except ValidationError as e:
    print(e.json())




class UserModel(BaseModel):
      name:str
      password1:str
      password2:str

      @validator('name') #这里面写验证的属性
      def name_must_contain_space(cls,v):
            if ' 'not in v:
                  raise  ValueError('Must contain a space')
            return v.title()

      @validator('password2')
      def passwords_match(cls, v, values, **kwargs):
            if 'password1' in values and v != values['password1']:
                  raise ValueError('passwords do not match')
            return v



try:
    UserModel(name='samuel colvin', password1='zxcvbn', password2='zxcvbn')
    print("验证通过")
except ValidationError as e:
    print(e)

print(" 通过validtor装饰器验证属性值，将错误的")
print("=======================")
try:
    UserModel(name='张三',  password1='zxcvbn', password2='zxcvbn2')
except ValidationError as e:
    print(e)

print("=======================")
print(" 通过validtor装饰器验证属性值，将错误的e.json()打印校验不通过的所有字段、"
      "msg提示信息Error后面跟的提示字符串、错误类型")

try:
    UserModel(name='张三',  password1='zxcvbn', password2='zxcvbn2')
except ValidationError as e:
    print(e.json())

print("=======================")
print(" 通过validtor装饰器验证属性值，将错误的e.errors(),返回类型为列表")
try:
    UserModel(name='张三',  password1='zxcvbn', password2='zxcvbn2')
except ValidationError as e:
    print(e.errors())

print("=======================")
print(" 通过validtor装饰器验证属性值，str(e),以人类可读的方式返回")
try:
    UserModel(name='张三',  password1='zxcvbn', password2='zxcvbn2')
except ValidationError as e:
    print(str(e))

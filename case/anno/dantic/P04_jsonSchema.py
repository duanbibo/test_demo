from enum import  Enum
from pydantic import BaseModel,Schema,Field

class FooBar(BaseModel):
    count: int
    size: float = None

class Gender(str, Enum):
    male = 'male'
    female = 'female'
    other = 'other'
    not_given = 'not_given'

class MainModel(BaseModel):

   '''

   通过聚合到mainModel内，在里面设置子model是否必须，设置别名。
    field：设置左边属性在当前类作用域中的是否必须，设置别名
   '''
   foo_bar: FooBar = Field(...)
   gender: Gender = Field(None,alias='Gender',  )
   snap: int = Field(
       42,
       title='The Snap',
       description='this is the value of snap',
       gt=30,
        lt=50,
    )
   class Config:
       title = 'Main'

#BaseModel.schema 会返回一个表示JSON Schema的字典对象。


#BaseModel.schema_json 会返回一个表示表示JSON Schema的字符串。
print(MainModel.schema())
#{'title': 'Main', 'description': 'This is the description of the main model', 'type': 'object', 'properties': {'foo_bar': {'$ref': '#/definitions/FooBar'}, 'Gender': {'title': 'Gender', 'enum': ['male', 'female', 'other', 'not_given'], 'type': 'string'}, 'snap': {'title': 'The Snap', 'description': 'this is the value of snap', 'default': 42, 'exclusiveMinimum': 30, 'exclusiveMaximum': 50, 'type': 'integer'}}, 'required': ['foo_bar'], 'definitions': {'FooBar': {'title': 'FooBar', 'type': 'object', 'properties': {'count': {'title': 'Count', 'type': 'integer'}, 'size': {'title': 'Size', 'type': 'number'}}, 'required': ['count']}}}
print(MainModel.schema_json(indent=3))





from typing import List
from pydantic import BaseModel,Schema


'''
#递归模型，类与类之间的关系，组合和聚合
'''
class Foo(BaseModel):
      #...表示的意思是省略，与require意思一样
      count:int =...
      size: float =None
class Bar(BaseModel):
      apple = 'x'
      banana ='y'
class Spam(BaseModel):
      foo:Foo= ...
      bars:List[Bar]=...

      #通过内嵌类，为当前的类设置jsonschema对应的title
      class Config:
            title='Main'

s = Spam(foo={'count': 4}, bars=[{'apple': 'x1'}, {'apple': 'x2'}])
#打印当前模型的字典结构
print(s.dict(),)
print(s.json())
print(s.schema())
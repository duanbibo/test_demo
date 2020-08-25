from  pydantic import BaseModel,PydanticValueError,validator, ValidationError


#自定义错误类，继承系统的错误类，并写重写错误混合类的属性 code 和msg_template
#使用文本插值{wrong_value} ,插值的内容将返回ctx 的键和值
class NotABarError(PydanticValueError):
      code='not_a_bar'
      msg_template = 'values is not  "bar", got "{wrong_value}"'


class Model(BaseModel):
      foo:str

      @validator('foo')
      def name_must_contain_space(cls,v):
            if v !='bar':
                  raise  NotABarError(wrong_value=v)
            return v

try :
      Model(foo='ber')
except ValidationError as e:
      print(e.json())

# [
#   {
#     "loc": [
#       "foo"
#     ],
#     "msg": "values is not  \"bar\", got \"ber\"",
#     "type": "value_error.not_a_bar",
#     "ctx": {
#       "wrong_value": "ber"
#     }
#   }
# ]
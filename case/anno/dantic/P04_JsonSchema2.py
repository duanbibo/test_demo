

''''
编写jsonschema 验证接口返回的数据: 数据结构 ： array， object
                              数据类型：   integer， str
                               数据约束： 长度、范围
                               数据规则：  正则

 jsonschema.validata(instance=result, schema=schema)

 #validate() 函数将首先验证所提供的模式本身是否有效，因为不这样做会导致不太明显的错误消息，
# 并以不太明显或一致的方式失败。然后再验证json数据。
#如果JSON数据实例是无效的，则抛出 jsonschema.exceptions.ValidationError 异常
#如果schema模式本身是无效的，则抛出 jsonschema.exceptions.SchemaError 异常#

'''

from jsonschema import validate
from jsonschema.exceptions import  ValidationError
from jsonschema.exceptions import SchemaError

result = {
    "code": 0,
    "msg": "login success!",
    "token": "000038efc7edc7438d781b0775eeaa009cb64865",
    "username": "test"
}

schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "test demo",
    "description": "validate result information",
    "type": "object",
    "properties": {
        "code": {
            "description": "error code",
            "type": "integer"
        },
        "msg": {
            "description": "error msg ",
            "type": "string"
        },
        "token":
        {
            "description": "login success return token",
            "maxLength": 40,
            "pattern": "^[a-f0-9]{40}$",  # 正则校验a-f0-9的16进制，总长度40
            "type": "string"
        }
    },
    "required": [
        "code", "msg", "token"
    ]
}

#验证后是没有返回值的，
#validate() 函数将首先验证所提供的模式本身是否有效，因为不这样做会导致不太明显的错误消息，
# 并以不太明显或一致的方式失败。然后再验证json数据。
#如果JSON数据实例是无效的，则抛出 jsonschema.exceptions.ValidationError 异常
#如果schema模式本身是无效的，则抛出 jsonschema.exceptions.SchemaError 异常#


try:
      #在编写时，需要处理json数据和schema本身的异常。
      validate(instance=result, schema=schema)
except ValidationError as ve:
      print(ve,"实例不符合")
except SchemaError as se:
      print(se,"Schema编写错误")
else:
      print(" 校验通过")

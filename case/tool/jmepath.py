import json


from  jmespath import search

'''

jmespath.serch( experss ,data): 第一个参数是表达式，第二个参数是数据

  jmespath源码解析：
     内部做了词法分析 这个文件  lexer 
     
     SIMPLE_TOKENS = {     //token 符号
        '.': 'dot',
        '*': 'star',
        ']': 'rbracket',
        ',': 'comma',
        ':': 'colon',
        '@': 'current',
        '(': 'lparen',
        ')': 'rparen',
        '{': 'lbrace',
        '}': 'rbrace',
    }


'''


d={
        "error_code": 0,
        "stu_info": [
                {
                        "id": 2059,
                        "name": "小白",
                        "sex": "男",
                        "age": 28,
                        "addr": "河南省济源市北海大道32号",
                        "grade": "天蝎座",
                        "phone": "18378309272",
                        "gold": 10896,
                        "info":{
                            "card":434345432,
                            "bank_name":'中国银行'
                        }

                },
                {
                        "id": 2067,
                        "name": "小黑",
                        "sex": "男",
                        "age": 28,
                        "addr": "河南省济源市北海大道32号",
                        "grade": "天蝎座",
                        "phone": "12345678915",
                        "gold": 100
                }
        ]
}

print(type(d))
s=search('stu_info[0].info',d)   #使用 .  和数组相结合
s2=search('stu_info[*].id',d)         #使用通配符

print(s,s2)

#利用json库，将一个字典对象保存到一个文件中
# f=open(r'pakckage.json',encoding='utf-8',mode='a')
# json.dump(d,f)

with open( r'pakckage.json','r',encoding='gbk')as f:
      s=json.load(f)
      result=search('stu_info[0]',s)
      print(result)

dat={"a": {
  "b": {"d":['d1','d2'],
    "c": [
      {"d": [0, [1, 2]]},
      {"d": [3, 4]}
    ]
  }
}}
dat1=search('a.b.c[0].d[0]',dat) #jmespath查询的返回结果是一个确定的值
print(dat1,type(dat1))

import jsonpath
jsult=jsonpath.jsonpath(dat,'$.a.b.c[0].d[0]')
 #这个查询结果两者不一样，jsonpath返回的数据是一个列表，包括数组中的最外层[]
print(jsult,type(jsult))


'''  jsonpath  更强大吧，能够递归查找所有符合key值'''
jsult2=jsonpath.jsonpath(dat,'$..d')
print(jsult2)
import jsonpath
import json

def read_jsonpath(file,express):
      with open(file,'r',encoding="utf-8")as jf:
            data=jf.read()
            #将读出来的数据转换为dict格式
            jdata=json.loads(data)
            print(jdata,type(jdata))
      sult=jsonpath.jsonpath(jdata,express,result_type='VALUE')
      print(sult)


#当jsonpath表达式的结果为属性值是能够正常显示符合对应key的一个或者多个value

#使用。。可以递归查找
read_jsonpath("package.json","$..name")
read_jsonpath("package.json","$.stu_info[*].sex")
# 查找某个列表中属性值符合条件的。
read_jsonpath("package.json","$.stu_info[?(@.age==24)]")
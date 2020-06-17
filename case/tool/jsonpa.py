import jsonpath
import re
import os
import json


'''
语法：    匹配到的是value值， 
          返回的value值，取决于最后一个表达式的对象为哪一个节点。
适用类型： 接口返回的json类型数据。在一个返回中提取多个值作为变量。
            同时在提取变量的时候，还能够对值做一些过滤，如果符合就提取，不符合就舍弃。

'''
'''         def jsonpath(obj, expr, result_type='VALUE', debug=0, use_eval=True):

              返回值类型; list
表达式：
$	          查询的根节点对象，用于表示一个json数据，可以是数组或对象
@	          过滤器断言（filter predicate）处理的当前节点对象，类似于java中的this字段
*	          通配符，可以表示一个名字或数字
..	      可以理解为递归搜索，Deep scan. Available anywhere a name is required.
.<name>	    表示一个子节点
[‘<name>’ (, ‘<name>’)]	表示一个或多个子节点
[<number> (, <number>)]	表示一个或多个数组下标
[start:end]	数组片段，区间为[start,end),不包含end
[?(<expression>)]	过滤器表达式，表达式结果必须是boolean

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


#jsonpath  输出的结果都是list
res= d["stu_info"][1]['name'] #取某个学生姓名的原始方法:通过查找字典中的key以及list方法中的下标索引
print(res) #输出结果是：小黑



res0=jsonpath.jsonpath(d,'$..gold')  # $.. 可以进行模糊匹配。能够匹配到子级更下级,模糊匹配可以多个。
print(res0)

import jsonpath
res1=jsonpath.jsonpath(d,'$...name') #嵌套n层也能取到所有学生姓名信息,$表示最外层的{}，..表示模糊匹配
print(res1) #输出结果是list：['小白', '小黑']

res2= jsonpath.jsonpath(d,'$..bank_name')
print(res2) #输出结果是list：['中国银行']
print(type(res2))

res3=jsonpath.jsonpath(d,'$..name123') #当传入不存在的key(name)时,返回False
print(res3) #输出结果是：False

res4=jsonpath.jsonpath(d,'$.stu_info[0:2]') #取根节点的stu_info节点的第1,2个元素值
print(res4)

res5=jsonpath.jsonpath(d,'*')   # 匹配整个json字符串的value值，以及镶嵌子串的key和value
print(res5)

res6=jsonpath.jsonpath(d,'$.stu_info[(@.length-1)]') #求 最后一个的子节点
print(res6,type(res6))
print("----------------------")
resa=jsonpath.jsonpath(d,'$..stu_info[?(@.gold>100)]..gold') #返回一个子元素，要求这个子元素的值符合一定的条件
print(resa)
res7=jsonpath.jsonpath(d,'$..stu_info..[?(@.gold>100)]')#返回一个子节点，整个子节点的下属节点的值符合一定条件
print(res7,"0000000000")
res8=jsonpath.jsonpath(d,'$..stu_info[?(@.length>8)]..id')#返回子节点，要求同类节点的数量必须大于8个
print(res8)
res9=jsonpath.jsonpath(d,'$..stu_info[?(@.id>2050)]..id')#返回子节点，要求子节点的值必须的范围
print(res9)
print(res9[1],'1111111111111')
print((res7[0]).get("id"))  #根据返回值进行获取
'''
获取指定文件夹下的json文件，并利用jsonpath解析内容
'''


'''
 文件路径的处理部分：   
                      os.getcwd()获得文件的当前路径
                      os.path.dirname(__file__) :获得文件夹的父级目录
                      os.pardir : ..  返回上级目录
                      os.path.join(path1,path2) :将多个个路径进行拼接
'''

xiangmu=os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir,os.pardir))
jsonfile=os.path.join(xiangmu,"read/package.json")

print(jsonfile)
with open(jsonfile,"r",encoding='utf-8')as f:
        all=f.read()
        #print(type(all))    str
        r = json.loads(all)
        print(type(r),"格式为")  # dict
        # zj=json.load(f)
        '''
    从其他文件读取出来的数据是字符串类型,是不能够进行使用的，需要用 转换为数据类型，
     解析后使用，才能够用jsonpath进行匹配
     1.第一种方式： json.load(file) ：直接将文件载入，转换数据类型。转换格式为数据的结构
     2. 第二种方式:    json.loads(file.read()) :文件读取完毕后形成字符串，然后转换为字典类型dict
     
     知识扩充：json数据转换的其他方法
          dump :直接将数据写入json文件中，前提是必须 打开这个文件，才能够写入
          dumps:将python中的字典转化为 字符串，
      
        '''

# quanbu= jsonpath.jsonpath(zj,'*')
# print(quanbu,type(quanbu))
print("-----------")
quanbu2= jsonpath.jsonpath(r,'*')
print(quanbu2,type(quanbu2))
print("---"*20)

zi=jsonpath.jsonpath(r,'$..stu_info[?(@.id==2067)]..id')
print(zi)


'''           json的扩展方法'''
'''     将字典类型的数据转化为字符串'''
stringj=json.dumps(r)
print(stringj,type(stringj))
print("+++"*20)

'''        json .dumps 直接写入文件中'''
file = open('1.json', 'w', encoding='utf-8')
jfile=json.dump(quanbu2,file)







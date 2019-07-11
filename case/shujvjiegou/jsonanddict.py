import requests
import json
import re
import os
from collections import deque

# def dict_to_json():
#     dict = {}
#     dict['name'] = 'many'
#     dict['age'] = 10
#     dict['10'] = 'male'
#     print(dict)  # 输出：{'name': 'many', 'age': 10, 'sex': 'male'}
#     print(dict.__class__)
#     a=dict[1]
#     print(a)
    # j = json.dumps(dict)
    # print(j)  # 输出：{"name": "many", "age": 10, "sex": "male"}
    # print(j.__class__)
    # # d=json.loads(j)
    # # print(d)
    # # print(d.__class__)
    # # del dict['age']  #根据key值删除字典内的一组数据
    # # print(dict)
    # dict['name']='zhangsan' #根据key值进行插入或者更新
    # print(dict)
    # dict['name2'] = 'lisi'
    # print(dict)
    # b=dict['name2']
    # print(b)
    # print('name' not in dict)
    # print(dict.items())
    # print(dict.items().__class__)
    # print(dict.keys())
    # print(dict.values())
    # a=dict.pop('name')
    # print(a)
    # c=dict.setdefault('name3','wangwu')
    # print(dict)

    # t={'name':'三国演义','price':10,'auth':'罗贯中'}
    # w = '书名是：{name},价格是：{price}，作者是：{auth}'
    # print(t % w)
    #
    # d=re.search('ssc','sss',flags=2)
    # c='wd2wd2wd'
    # re.sub('s','wc456',c)
    # w=re.fullmatch((r'c\Dt'),'c2t')
    # print(w)

# c=[e for e in dir ( deque) if not e.startswith('_')]
# d=[e for e in dir ( deque) ]
# print(c,'\r\n',d)
a=os.getcwd()
c=a.split('/')
d=os.listdir(a)
e=os.walk(r'C:\Users\87842\PycharmProjects\test_demo\case')
print(a,c,d,e)

    # with open('1.json')as f:
    #    str=f.read()
    #
    #
    # print(os.path.abspath('1.json'),'\r\n',str)
# with open('1.json','a') as f:
#         f.write('python is good\n')
#
#
# with open('1.json','r')as f:
#         c=f.readlines()
#         w=c[13]
# print(c)




    # stu={'name': 'Jack', 'sex': 'm', 'age': 22}
    # print('his name is {name}, his age is {age}'.format(**stu))
    # print('his name is {name}, his age is {age}'.format_map(stu))

#     with open('1.json','w')as f:
#          json.dump(dict,f)
#
# def json_file_to_dict():
#     j= {"name": "many", "age": 10, "sex": "male"}
#     with open('1.json','r')as f:
#           dict2=json.load(j)
#           print(dict2)



# if __name__ == '__main__':
#     json_file_to_dict()

# import json
#
# def json_file_to_dict():
#     with open('1.json', 'r') as f:
#         dict = json.load(fp=f)
#         print(dict)  # {'name': 'many', 'age': 10, 'sex': 'male'}
#
#
# if __name__ == '__main__':
#     dict_to_json()



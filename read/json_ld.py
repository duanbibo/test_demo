import json
import os

#配置当前项目的路径
cur_path=os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))
#利用os.path.join拼接路径的时候，后面的不要带斜杠开头
file_path=os.path.join(cur_path,"resource/package.json")
print(cur_path,file_path)

#load 加载文件中的内容并将字符串转字典
with open(file_path ,'r',encoding="utf-8" ,)as j:
      data=json.load(j)
      print(data,type(data))
#dumps 处理将字典类型转换为str字符串,由于在内存存储，展示的中文值为
s= json.dumps(data)
print(s,type(s))

#loads 处理字符串 将字符串转换为字典。
d=json.loads(s)
print(d,type(d))

#dump 将字典对象存储到文件中，接受2个参数，第一个为对象第二个为文件对象
with open( "package.json","a",encoding='utf-8')as fw:
      stu=json.dump(d,fw,ensure_ascii=False)
      print(stu)



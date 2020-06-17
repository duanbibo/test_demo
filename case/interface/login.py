import requests
import  base64
import re

from retrying import retry

s=requests.session()
#参数化账号
username="18903719017"
#参数化校验。权限1代表医生  权限2 代表护士
authorities=['QUESTION_WRITE','IMAGE_WRITE']


#参数化内输入值的内容
basic="doctor_web:".encode()
res=base64.b64encode(basic).decode()
#print(res)

#指定URL路由，可以划分为 baseurl +路径
url='https://api.xinzhili.cn/v0/oauth/token'

h={ 'Authorization': 'Basic  %s'%res}
d={
           "username": username,
            "password": "123456",
            "grant_type": "password"
 }

#发送请求，获取响应文本

r=s.post(url=url,data=d,json=None,headers=h,verify=False)
text=r.text
#利用requests工具类获取response内的cookie组成的键值对
c=requests.utils.dict_from_cookiejar(r.cookies)
print(text,c)

#正则匹配access_token的值
token=re.findall(r'"access_token":"(.+?)"',text)
print("---token",token[0])

#匹配到accesstoken中间负荷部分。
infotoken=re.findall(r'\.(.+?)\.',token[0])
print(infotoken[0])

#print(len(infotoken[0])%3)  如果token的值不满足3的整倍数需要后面补充几个“=”
#base64解码后还原为bytes字节，还需要转码utf-8
info=base64.b64decode(infotoken[0]+"=",).decode('utf-8')

#转码为utf-8,还需要转换为字典类型，方便提取值
dictinfo=eval(info)
print((eval(info)))
print("-----")


#正则表达式匹配出来的都是列表,匹配登录用户名
#info_username=str(re.findall(r'"user_name":"(.+?)",',str(info)))

#验证部分 账号  权限 。确认从token中获取到的登录手机号与参数化的登录手机号一致；登录的域的权限列表符合预期结果。
#verify=[username,authorities[0]]
assert authorities[0] in dictinfo["authorities"] and  username ==dictinfo["user_name"]













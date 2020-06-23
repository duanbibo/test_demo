import requests

urllogin='http://bsso.yunduoketang.cn/sso/userLogin'
datal= "userName=test007&password=111111&redirectUrl=&appCode="
l=requests.post(url=urllogin,data=datal)
tl=requests.utils.dict_from_cookiejar(l.cookies)
print(tl.keys())

s=requests.session()

# 不带上Cookie就访问不了这个页面
cookie = "anonymid=jk63khrk-y97r4p; _r01_=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn421/20180720/1740/main_JAWQ_0aa000000ceb195a.jpg; _ga=GA1.2.273332130.1532825428; depovince=HUN; JSESSIONID=abcE5k0CiAJDc9ESVEcuw; ick_login=026ba348-e4e9-4871-9ce3-5868b95cfdd3; first_login_flag=1; loginfrom=syshome; wp_fold=0; BAIDU_SSP_lcr=https://www.baidu.com/link?url=VRx_HKUd53I5rYWZHvrQ9VVLotqST6-jtaZDlscFYCO&wd=&eqid=e957aec400037928000000065b64fcab; ick=64518f30-9a22-47df-b3c3-4114f185c3c6; t=8fcf47068763c279eea2620b51b7a3311; societyguester=8fcf47068763c279eea2620b51b7a3311; id=967272361; xnsid=fd736c63; jebecookies=3f9a3853-3371-4857-8268-308d663ca146|||||; jebe_key=19041c4e-4d38-4dc1-bfb9-124b81afae61%7C33b1d8f602cf6dd5a9834fe6f2bf97f2%7C1533346094265%7C1%7C1533346099750"

# 将上面哪个cookie转化成字典类型
#观察复制的cookie是文本样式，每个键值对都是以分号隔开的，同时键左边是key,值在右边。
#利用字典组成的列表推导式
cookie_d={ i.split("=")[0]:i.split("=")[1] for i in cookie.split("; ")}
print(cookie_d,"=====")
cookie_dict = {i.split("=")[0]:i.split("=")[-1] for i in cookie.split("; ")}
print(cookie_dict,"-----")


pu='http://uctcrm.yunduoketang.cn/user/updateUserOnlineStatus'
h={'Content-Type':'application/json;charset=UTF-8','Cookie': 'JSESSIONID=454846F40DA411BC9490730739EB7120'}
datapu={'status': '2'}
up=s.post(url=pu,json=datapu,headers=h)
print(up.cookies)
a=requests.utils.dict_from_cookiejar(up.cookies)
print(a)




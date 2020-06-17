import time

''' time类是基础，获取的对象信息最全，年月日时分秒，一年第几天，一周第几天，当前是否夏季
  time.time():返回当前时间的浮点型数值
  time.localtime():传入一个浮点型的数值，返回一个time结构化的对象
  time.strftime(，):传入指定的formt样式，和结构化time对象，返回一个string时间戳
  time.strptime(，):传入字符串，和指定解析的formt样式，返回衣蛾time结构化对象
  asctime([t]). ctime(localtime()) :返回一个string对象这个对象的无年只有月份且是英文，传入的对象分别是元祖和浮点型的时间值
  time.mktime():传入一个时间元祖对象返回一个浮点类型的时间值

'''

t = time.strftime('%Y-%m-%d %H:%M:%S')
print(t, type(t), "格式化日期时间利用strftime函数，在函数中字符串占位指定代替的 年月日，时分秒")

pd = time.strptime('2020=10=10 23:20:08', "%Y=%m=%d %H:%M:%S")
print(pd, "利用time.strptime()函数解析字符串日期值，需要指明解析的格式,返回的是一个结构化时间对象具名元祖")

structt = time.localtime(time.time())
print(structt, "localtime() 函数本身传入的参数为一个浮点型的数值返回的是一个结构化time对象。这个对象内存储的是当前time的所有信息")
print(structt, type(structt), "大部分time返回的要么就是int类型的毫秒值，"
                              "要么就是结构化time具名元祖，必须要对整个元祖重新拆包赋值给指定字符串转化人类human易识别的")
'''time.struct_time(tm_year=2020, tm_mon=6, tm_mday=8, tm_hour=14, tm_min=57, tm_sec=54, tm_wday=0, tm_yday=160, tm_isdst=0)
                                                                                     一周的第几天[0,6] :0代表周一
                                                                                      一年的第几天
                                                                                       当前是否为夏季                                                                                 
 '''
print(structt.tm_hour, "能够获取time的具名元祖对象。通过具名元祖对象获取他的各个字段值")
structtt = time.strftime('%Y-%m-%d  ', structt)
print(structtt, type(structtt), "重新对结构化的数据进行string格式化")

shijianzhi= time.time()
print(shijianzhi,type(shijianzhi), "time.time()返回浮点型的时间戳")

ct=time.ctime(shijianzhi)
print(ct,type(ct),"返回time是英文月、日 时间 组成的字符串")
asc = time.asctime(structt)
print(asc, "ctime和asctime:接受时间的元祖并返回一个可读形式的字符串，不传值时默认为当前时间")

timetuple = structt
mk = time.mktime(timetuple)
print(mk, "time.mktime()返回一个时间戳，传入的参数是一个元祖对象，这里用的是结构化time。是localtime的返回值")

import datetime

'''  datatime :
     由于time库对时间类操作类比较少，在实际中经常用到对时间和类型的转换。
     datetime库中主要用到的三大类 一个是date类，一个是time ,一个是datetime类 继承自date类
'''
print("=========date类中默认的对象内容和样式 年-月-日 "
      "date方法中提供了日期的一些加减、变化的方法支持"
      "===============")

today = datetime.date.today()

print(today, type(today), "today()是datetime库中date类下的类方法,返回一个datetime.date对象，年月日为人类可识别的")

print(today.year, today.month, today.day, type(today.month), "这个通过date对象获取的年月日int类型"
                                                             " 在源码中是被@property修饰的方法"
                                                             "这些方法都伪装成属性被data实例调用 ,这些方法也能后被子类datetime调用")

datachuo = datetime.date.fromtimestamp(1231324)
print(datachuo, type(datachuo), "fromtimestamp()根据传入的时间戳作为参数返回一个data对象，返回的对象默认格式为 年-月-日")

dateduix = datetime.date(2018, 5, 6)
print(dateduix, type(dateduix), "利用date() 函数传入多个参数 年、月、日 进行返回一个对象")

#这部分是time库没有的，对时间的修改，单独修改其中一个值。replace是开了一个先河
r = dateduix.replace(day=5)
print(r, "利用replace()函数修改data属性中年月日的值，会生成一个新的日期对象")

#同样的，timedelta方法是计算日期的一个好的方法，它是一个多继承的混合类
dl = datetime.timedelta(10)
print(dl, type(dl))
print(r + dl, "利用timedelta()函数生成一个datetime对象，这个对象可以被其他datetime对象进行计算，如计算指定日期的前后几天")

w = r.weekday()
print(w, "weekday()返回当前时间位于一周的第几天，周一为0")
rili = r.isocalendar()  #iso国际标准日历
print(r,rili, "ioscalendar返回系统的日历，由年，一年第几周，一周的第几天组成。是一个元祖")


print(r.isoweekday() ) # 周一为1   ios :国际化标准日历
print("over--date")
''' datetime类：datatime类是data和time的结合体，包含两者所有的信息。所有的属性和方法都有
   datetime类的构造主要是年、月、日、时、分、秒，与data类似，可以用 fromtimesstamp 传入时间戳返回datetime对象

'''

riqi = datetime.datetime.today()
print(riqi, type(riqi), "实际上还是调用父类date的方法，但是返回的对象还是子类")

date = datetime.datetime.now()
print(date, type(date), " 利用datetime库下的datetime类的now函数，返回的是格式化后的时间类型为datetime，而非毫秒值")

datett = datetime.datetime.strftime(date, '%Y-%m-%D %H:%M:%S')
print(datett, type(datett), "利用strftime()函数直接将date数据格式化为字符串。")

print("==========================")

'''自定义 解析时间类型转化'''

''' 提前准备好的数据，字符串对象和 datetime对象'''

st = "2020-08-07  11:11:30"
dd = datetime.date.today()  # 获取的day是零点的。
dt = datetime.datetime.today()


def date_toString(dt):
      ''' 日期转化为字符串 很神奇呀：这里也没指定调用哪个库/类的strftime呀'''
      print(dt.strftime("%Y-%m-%d %H:%M:%S"))


date_toString(dd)
date_toString(dt)


def str_toDate(str):
      ''' 核心利用strptime:将字符串格式化'''
      print(datetime.datetime.strptime(str, "%Y-%m-%d %H:%M:%S"))


str_toDate(st)


def str_toTimestamp(str):
      '''核心利用time的.mktime返回时间戳'''
      print(time.mktime(time.strptime(str, "%Y-%m-%d %H:%M:%S")))


str_toTimestamp(st)


def Timestamp_Str(tamp):
      ''' 把时间戳转换为字符串str'''
      print(time.strftime("%Y-%m-%D %H:%M:%S", time.localtime(tamp)))


Timestamp_Str(1111111111)

import calendar

'''
日历库主要就是给定日期来进行计算
'''

print(calendar.calendar(2018))
print("niubile,将当年的日历对象直接打印出来")
print(calendar.firstweekday())
print(calendar.isleap(2018), "判断当年是否闰年")
print(calendar.leapdays(200, 2345), "返回两个年之间的闰年总和数")
print(calendar.monthcalendar(2020, 6), "返回一个整数的单层列表嵌套，每个嵌套代表一周。第一个代表周一，"
                                       "元素为1的代表当前月份第一天为周几，如果在第三个元素代表当月第一天为周三，前面和后面用0补充")
print(calendar.monthrange(2020, 6), "返回两个参数第一个为当月第一个星期一的日期码，第二个参数为当月多少天")
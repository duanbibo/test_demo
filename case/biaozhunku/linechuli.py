import linecache
'''
linecache :可以用它方便的获取某一文件某一行内容，而且它被traceback模块用来获取相关源码信息来展示
'''

'''
在使用open函数进行读取时，会将全部的内容载入内存中，如果出现较大的文件读取时，是不可行的。
 file.readlines 是返回所有行组成的一个列表。是读取完毕后才能获取的内容
'''

with open('source.txt','r',encoding='utf-8')as f:
      af=f.readlines()
      print(af[-1],"这是使用open函数读取的结果")

df=linecache.getline('source.txt',9)
print(df,"这是使用linecache函数读取固定的结果")

adf=linecache.getlines('source.txt')[-1]
print(adf,"使用linecache函数从缓存中读取，然后使用切片读取指定范围")

#读取的结果展示时 \n ，可以借助字符串的strip方法进行处理
#如果读取的字符串是空行，可以用len()函数处理决定是否进行显示。
# for i in adf:
#       c=i.strip()
#       print(c)

''' 对文件更新，再调用open函数，重新获取内容'''
with open('source.txt','a',encoding='utf-8')as f:
      s="追加的内容"
      f.write(s)
with open('source.txt','r',encoding='utf-8')as f:
      aaf=f.readlines()

      print(aaf[-1],"这是使用open函数读取的结果")
'''  实时证明，在对文件内容进行getlines后，
即使文件内容更改了，再次进行获取行内容，也是获取上次缓存内的值。'''
print("  ===以下为没有执行更新输出缓存的内容====")
updf=linecache.getlines('source.txt')[-1]
print(updf,"更新后查看")

#执行缓存清除或更新
print("=============执行缓存更新或检查==============")
linecache.checkcache('source.txt')
newline=linecache.getlines('source.txt')[-1]
print(newline,"以上为检查后自动清除缓存重新getlines数据")

#使用linecache.updatecache() 方法
up=linecache.updatecache('source.txt')
print(up,"update方法返回文件全部内容")



'''尝试读取excel'''
# ex=linecache.getlines('东方.xlsx')
# print(ex)
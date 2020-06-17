import os
import shutil

# f=open( 'ttt.txt','a+')  # 使用open函数，采用a/w的方式进行操作文件内容时，如果文件不存在就会创建。
# f.write("aaaaa"+"\n")
# f.close()

r=open( 'ttt.txt','r')
yihang=r.read(9)            #指定读取多少个字符内容
neirong=r.read()            #读取全部文本内容 ,默认为字符串类型
quanbu=r.readlines()          #读取内容装在列表内，每一行为一个列表元素 ，
print(yihang)
print(neirong )
print("---------- ",type(neirong))
print(quanbu)
r.close()

#os.mkdir("mkdir")     #利用os模块创建目录
#os.mknod("mk.txt")  # 利用os模块无法创建文件，因为window系统没有

shutil.copyfile('ttt.txt','copy.txt')
#利用shtil工具类进行复制文件内容，参数是两个文件的名称。第一个是源文件 ，第二个目标文件可以不存在
shutil.copyfileobj(open('ttt.txt','r'),open('copy.txt','a'))
#将第一个文件内容写入到第二个文件中去，第一个文件对象返回的是一个object对象
shutil.move('copy.txt','./mkdir/move.txt')
#修改文件路径
shutil.copytree()
shutil.rmtree()

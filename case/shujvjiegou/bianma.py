

'''
内置函数：传入，根据传入的int类型数字输出对应的阿斯玛

'''
'''
unicode和字节字符串
str类型：
bytes 类型：
bytearray 类型：

'''
import sys
print(sys.getdefaultencoding(),"利用sys查看解释器默认的字符编码集")


print(ord('a'),"ord() 传入一个字节，输出它对应的Unicode代码点数字")
print(chr(222),"chr传入int类型的数字,返回对应的ASCII字符")
print(hex(1600),"hex()传入一个数字，返回它的十六进制字符串:0x__这样 ")
print(oct(800),"oct()传入一个数字，返回它的八进制字符串:0o__这样 ")

b=b'spam'   #在创建bytes对象时，必须是ASCII文本范围内
s='eggs'
print(type(b),type(s),b,s)
print(list(b),"其实bytes对象是一个列表对象，每个元素存储当前对应的Unicode代码点数字，它的范围是255之内=>[115, 112, 97, 109]")
print(b[0],ord('s'),"通过输出字节的第几位序列的代码点与单独利用ord()函数输出的代码点是一致的")


stren=s.encode()   #使用str的encode方法将str转换为byte对象，不声明就是bytes二进制编码
print(stren ,type(stren))

byde=b.decode(encoding='utf-8')    #使用bytes的decode解码方法指定utf-8编码集，将二进制转换为str字符串
print(byde,type(byde))



B=bytes('abc','utf-8')  #创建字节对象，声明创建使用的编码集
print(B,type(B))


ba=bytearray('abc','utf-8')
print(ba,type(ba),list(ba))
ba[0]=99
ba[1]=99
ba.append(99)
print(ba,list(ba))
strba=ba.decode('utf-8')
print(strba)

import struct


'''
struct ：主要处理二进制数据 处理图形或者音频文件形式或打包的数据。
'''

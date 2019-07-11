
''''''
'''
while 循环
'''
'''while True:
      print("while ture这是必须执行的，而且一直执行的")
'''

a=3
while a<9:
      print(a)
      a=a+1
''' while条件循环语句，里面跟条件语句，
条件语句进行判断，如果不符合break,退出死循环的执行'''
w=4
while True:
      w=w+1
      print(w)
      if w>10:
            break

z=4
z=z+1
while w>10:
      break

''' for 循环
 for  i  in  可迭代对象：  可迭代对象可以是list,str,tuple,dict
  以集合作为迭代对象的话，输出的值为key的值
'''
dict1={1:2,3:4,5:6}
for i  in dict1:
      print(i)
''' for 循环后的可迭代对象，可以利用range()函数，可以生成一个整数序列，
    range(start,end ,间隔) 一般开始和结束的数字，都是包含开头不包含结尾
'''
for j in range(0,10,2):
      print("迭代间隔为2时，分别是：%s"%j)



'''利用range循环求和'''
sum = 0
for i in range(1,101):

 sum += i
print(sum)

''' 写个求和的函数，能够计算0-参数之间的和'''
def sum1(x):
      res=0
      for i in range(0,x):
            res +=i
      return res
print(sum1(50))


s = "123456789"
lis = ''.join([s[i:i+3][::-1] for i in range(0,len(s),3)])
print(lis)

'''把这个写成方法，传入字符串和指定反转的位数'''
def resver(s,l=1):
      '''
      :param s:  传入的数字串
      :param len:  需要反转的长度
      :return: 返回结果
      '''
      return ''.join([s[i:i+l][::-1] for i in range(0,len(s),l)])
print(resver(s,4))

'''  
列表推导式： 值  值得由来  if  推导条件
'''
a3=(i for i in range(30) if i % 3 is 0)
lt=[]
for i in a3:
      lt.append(i)
print(lt)




''' 三目运算'''
yu=12
'''  判断数字如果能被2整除，就+1 ，如果不能就把这个数处理3    '''
c=(yu+1 if yu%2==0 else yu%3 )
print(c)
'''  跟定一个数组，将小于5的数，都进行+5处理 '''
l5=[1,2,5,6,7,7,4,2,0]
w5=( i+5   for i in l5 if i <5  )
print(w5)


'''--------- '''
a="ab"
b="ab"

print(id(a),id(b))
print(a is b)


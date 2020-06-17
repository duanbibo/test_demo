''''''

'''
python中的匿名函数lambda
'''

a=lambda x,y,z:x+y+z

print(a(4,5,6))

li=[4,6,7,8]
new=map(lambda x:x*2 ,li)
for i in new:
      print(i)
''' 如果列表中的元素的值除以二没有余数，将这个值进行平方'''
fnew=map(lambda  x:x*2,  filter( lambda x:x%2==0 ,li)     )
for f in fnew:
      print(f)
      '''方式二实现：    '''
enew= ( i*2  for i in li if i%2==0   )
for e in enew:
      print(e)

      ''' python中使用三元运算:假如当前元素除以三为0，就执行前面函数体，如果不等于就执行后面'''
san=567
sanyuan=   (san*2 if san%3==0 else san+2)
print(sanyuan)
'''三元运算符和for循环一起在列表推导式使用'''


g = (x * x for x in range(10)if x%3==0 )
i=[0,1,2,3]
new=map(lambda x:x+2,i)
for i in new:
      print(i)
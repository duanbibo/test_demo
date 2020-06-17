import  itertools

'''itertools 提供了许多针对可迭代对象的实用函数    
   如对可迭代对象进行无限自增，内部循环迭代，指定时间内一直打印整个迭代器内容
   如根据多个迭代对象进行生成一些组合：矩阵笛卡尔积，
   可迭代器内部的多个元素进行排列组合，指定参与组合的个数，指定重复与否
 
'''

'''  count  自增  无限迭代器一直增长，参数是start起始位置，step步长返回一个函数，可以通过for循环调用'''
five=itertools.count(start=1,step=0.5)
print(five)

''' itertool工具类返回的函数都是为生成器对象，并且它的生成器对象可以作为可迭代对象'''
zu=itertools.takewhile(lambda x:x<3,five)
print(list(zu))

# for i in five:
#       print(i)
rfive=range(1,100,5)  #range也是一个迭代器，但是他是指定了开始和停止的区间，并且可以声明步长
print(rfive)
# for i in rfive:
#       print(i)
''' cycle 循环   无限迭代器一直循环:它是一个不断循环迭代一个可迭代对象,比如一个列表是0-10 ，执行到10后再无限的进行循环'''
yizhi=itertools.cycle(rfive)
# for i in yizhi:
#       print(i)

'''repeat: 重复   在指定时间内一直返回参数内的对象'''
li=[0,1,2,3,4,5,6,7]
rep=itertools.repeat(li,times=10)
for i in rep:
      print(i)


'''排列组合迭代器
所谓排列，就是指从给定个数的元素中取出指定个数的元素进行排序。
组合则是指从给定个数的元素中仅仅取出指定个数的元素，不考虑排序。 同等条件下，排列的情况是大于组合的
'''

'''  product  主要用来组合 计算笛卡尔积，矩阵的排列组合,从元素个数意向的迭代器中每个迭代器分别去一个元素，生成的元素
      repeat：代表可以重复提取的次数
'''
prod=itertools.product([1,2],[3,4],[5,6],repeat=1)
# 135  ，136  ，145  146    235  236  245 256    一共8次 2的3次方
print(list(prod))

'''  pemutations : 排列 将p中的元素，长度为r的所有可能的排列。 位置不一样也属于另一种排列
   比如0-7 之间的8个数字，3个数字组成的一组，能有多少个 336个
  背后的算法是什么？
 '''

per=itertools.permutations(li,3)
zuhe=list(per)
print(zuhe,type(zuhe),len(zuhe))



''' combinations :组合，但是他的组合更为苛刻，要求不能重复而且即时位置不同也不行。不带重复的。
     比如 0-7  取出 0,1,2  这个排序，就不能再次取出  2,1,0  这个了   # 56
  '''
com=itertools.combinations(li,3)
quchongzuhe=list(com)
print(quchongzuhe,len(quchongzuhe))

print("zzzzzzzzzzzz")

'''   itertools.combinations_with_replacement(iterable, r)  
           允许重复但是要求次序不能变  #120种可能 '''
zuhe2=itertools.combinations_with_replacement(li, 3)
zuhexucixu=list(zuhe2)
print(zuhexucixu,len(zuhexucixu))

'''   以上三种排列组合：排列》次序组合》不重复组合'''


'''  zip_longest(*iterables ,fillvalue=None) 将多个可迭代对象进行组合为元祖，
  和zip的差别是缺失他会自动填充，根据多个可迭代对象最长的来 '''

z=zip(li,['0','1','2','3','4','5'])  #zip的组合是两者共同的部分组成的
#zip的解压 将两个可迭代对象组合为元组,然后可以用字典的工厂函数转换为字典
# for i in z:
#       print(i)
print(dict(z))

zip_l=itertools.zip_longest(li,['0','1','2','3','4','5','6','7','8'],['a','b','c'],fillvalue='空值')
for i in zip_l:
      print(i)


'''  takewhile  一次过滤器失败时取成功的数据：
主要用来对可迭代对象进行过滤的,当失败时停止，并返回过滤成功的数据
                    接受2个参数  第一个是回调的func ，第二个是可迭代对象
'''
li07=[7,6,2,5,8,9,3,1]
print(li07[::-1])  #切片反转
for i in reversed(li07):  # 利用reversed这个高阶函数返回一个可迭代对象
      print(i)

#  当条件返回true，获取数据
guolv=itertools.takewhile(lambda x: x<8,li07)
print(list(guolv))

'''dropwhile      一次过滤器失败时取  返回失败及后面的每一个元素
 :获取可迭代对象，当符合出现不符合的，获取不符合数据的后面素有可迭代对象的元素 ,
 如果同一个可迭代对象中，规则相同，与takewhile的取值相反'''
#当条件false时，获取数据
guolv2=itertools.dropwhile(lambda x:x<8,[7,6,2,5,8,9,3,1])
print(list(guolv2))



''' filterfalse全部过滤器 ，与filter取相反  ,只返回不符合的数据'''
ff=itertools.filterfalse(lambda x:x%2==0,li07)
for i in ff:
      print(i)

print("ffffffffffff")


'''groupby：切分迭代器,将迭代器进行分组切分为多个小迭代器。 
 如果后一个元素的key值等于前一个元素的key值，就将这两个元素放在同一个分组中
    如：对 7,6,2,5,8,9,3,1  模等于2进行分组 7 单独一组，为false；  6 和2分一组为True ,5 是false单独一组  
   '''
fenzu=itertools.groupby(li07,lambda x:x%2==0)
a=0
for i in fenzu:

      print(i)
      a+=1

      print(a)
print("gggggggggggg")

''' islice 切片，指定截取可迭代对象的多少位: 
除了可迭代对象外 一个参数是默认起始位置是0 ，两个参数指定开始和结束位置， 三个参数指的是步长'''

lice=itertools.islice(li07,2,5,2)
for i in lice:
      print(i)
print("========")



'''  chain 拼接多个可迭代对象 '''
pinjie=itertools.chain([0,1,2,3],['1','b'])
print(pinjie)
for i in pinjie:
      print(i)

'''   starmap  ：与map类似批量处理可迭代对象，生成值func(*item ) 
   ,其中item来自可迭代对象。主要用来处理列表嵌套元祖的数据，处理多个可迭代对象
   如 starmap(pow ,[(10,2),(10,4),(3,2)])    pow函数2个参数，实现 x的y次方 。批量执行多个可迭代西

'''
values=[(1,1),(2,2),(3,3)]
for i  in itertools.starmap(lambda x,y:(x,y,x*y),values):
      print('%d * %d = %d'%(i))

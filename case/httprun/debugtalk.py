import random



def get_number(num):
      list_nu=[]
      zero=0

      while zero<num:
            list_nu.append(random.randint(1,999))
            zero+=1
      else:
            return list_nu

#利用匿名函数和map  再进行过滤
# pf=map(lambda x:x*2 ,get_number(5))
# print(pf.__next__(),pf.__next__(),pf.__next__(),pf.__next__())
# for i in pf:
#       print(i)



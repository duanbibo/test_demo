


def sum(li):
   if not  li:
         return 0
   else:
      return li[0]+sum(li[1:])

a=sum([0,1,2,3,4])
print(a)



def jiecheng(n):
    if n==1:
        return 1
    return n * jiecheng(n - 1)

b=jiecheng(3)
print(b)



def jisuan(start,end):

      for i  in range(start,end+1):
            yield  i*i



b=jisuan(2,5)
for i in b:
      print(i)

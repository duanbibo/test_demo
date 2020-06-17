import ddt
def one(a):
      return a+1

def two(b):
      return b+1
def chengji(w,z):
      return w*z

cj=chengji(one(1),two(2))
print(cj)

value = [i * 2 for i in range(11) if i % 3 == 0]
value2=list(map( lambda x:x*x   ,filter( lambda  x:x%3==0,range(11))  )    )
sanyuan=[i*i for i in range(11)if i%3==0 ]
print(value,value2)



def canshu():
      list=[1,2,3,4,5,6]
      return  list


def hanshu(x):
      print(x)

a=canshu()
for i in a:
      hanshu(i)

values=[[1,2],[3,4],[5,6]]
v=len(str(len(values)))
print(v)
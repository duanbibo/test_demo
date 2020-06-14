import traceback


def chufa(a,b):
      try: a/b
      except ZeroDivisionError :
            print("除数不能为零",b)
      else:
            print(a/b)
      finally:
            print(a,b)

chufa(8,8)
print("=======")
chufa(5,0)

def paochu(a,b):

      if a<b:
            raise FutureWarning
      C = a - b
      print(C)


paochu(5,7)  # 主动触发异常，raise的异常
paochu(7,4)



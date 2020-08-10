import pithy


listype=['a',1]
print(listype.__dir__())

class ls:
      def __init__(self,name,*args,**kwargs):
          '''这里利用工厂函数进行包装下，在其他方法里面进行处理'''
          self.name=name
          self.info=list(args)
          self.addr=dict(kwargs)

      def printinfo(self):
            return  self.info

      def printadrr(self):
            return  self.addr

      def bianli(self): ...

      def  __str__(self):
            return  '[list: %s ] ' %(self.info)
















c=ls(4,[5,6],adr=1,ad2=2)

print(c.info,c.addr)
print(c.bianli)




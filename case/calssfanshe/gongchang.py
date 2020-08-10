def factory (aClass,*args):
      return aClass(*args)



class lei:
      def doit(self,message):
            print(message)

class Person:

      def __init__(self,name,job):
            self.name=name
            self.job=job

if __name__ == '__main__':

    p=factory(Person,'张三','IT')
    print(isinstance(p,Person))
    print(p.name)
    L=factory(lei)
    L.doit("干啥呢")
    



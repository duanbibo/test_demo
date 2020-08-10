
class  base:
      __slots__ = ['w','b']
      bshuxing='bshuxing'
      '''当前类为工具类：主要为了打印str 方法，输出做一些内省的工具'''



      def __str__(self):

            return  '<instance of  %s , address %s , \n %s>' %(self.__class__.__name__,id(self),self.__attrnames())

      def __attrnames(self):
            '''
            这里可以做一些内省的工具：比如dict打印类实例的属性，或者利用dir(o )打印内置的一些方法和值
            :return:
            '''
            result=''

            for attr in sorted(self.__dict__):
                  result+='\t name  %s=%s  \n' %(attr,self.__dict__[attr])
            return  result



class super():

      def __init__(self):
            self.data1='dat1'

class  Te(super,base):
      def __init__(self):
         super.__init__(self)
         self.data2='date2'
         self.date3='date3'




if __name__ == '__main__':

      b=base()
      print(b)
      c=Te()
      print(c)



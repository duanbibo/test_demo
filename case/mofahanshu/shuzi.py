
class shuzi:
      def __init__(self,chushihua):
            self.chushihua=chushihua

      def  __gt__(self, other):
            return self.chushihua >other
      def __lt__(self, other):
            return self.chushihua <other

      def  __bool__(self):
            '''布尔类型'''
            return  True

      def   __sub__(self, other):
            '''这里非常重要，返回结果为这个实例本身'''
            return shuzi(self.chushihua-other)
      def  __add__(self, other):
            '''正常加法：左侧指的是类的实例'''
            return  shuzi(self.chushihua+other)

      def __radd__(self, other):
            '''右侧加法，可以把实例放在右侧'''
            return shuzi(other+self.chushihua)

      def __iadd__(self, other):
            '''原处增加，相当于自增'''
            self.chushihua+=other

            return  self.chushihua

      def __str__(self):
            return  '%s '% self.chushihua


class shuzier(int):
      ''' 利用继承int内置类型，来实现它内有所有的运算符重载'''

      pass

if __name__ == '__main__':
      ''' 
      运算分为add 和radd(rightadd) ,普通的加法左侧代表实例，右侧代表other，如果没有radd运算符重载
      那么当前类实例就不支持，与左边的other数字求和。
      当左右两边都是当前类的实例，且当前类都已经实现了左右add，优先使用add，即把右侧当做other
      '''
      n=shuzi(9)
      o=n-4
      print(o)
      a=o+3
      print(a)
      print(5+a)
      print(a)  #8
      n+=3
      print(a)  #11

      print(bool(n))

      if bool(n):
            print("真")
      else:
            print("假")

      print(a<12) #使用gt， lt   大于和小于


      s2=shuzier(9)
      print(s2-n)
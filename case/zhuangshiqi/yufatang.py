def w(func):
      print('im in w')
      return func


class A:
      def _a(self):
            print('a')

      a=w(_a)

      @w
      def _b(self):
           print('b')

      def  _c(self):
            print('c')

A().a()
A()._b()





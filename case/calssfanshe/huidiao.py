
class huidiao:


      def __init__(self,value):
            self.value=value



      def __call__(self, other):
            return  self.value*other


if __name__ == '__main__':
      h=huidiao(5)
      print( h(3)," ==>   call()* shili")

      print(h.__call__(3))


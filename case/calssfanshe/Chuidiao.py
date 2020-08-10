

class  Reader:

      count=0

      def __init__(self,name,nationality):
            self.name=name
            self.nationlity=nationality
            Reader.count+=1

      def __call__(self, behava):
           print('Reader: %s' % self.name)
           print('Nationality: %s' % self.nationlity)
           print('%s is being %s.' % (self.name,behava))
           print('The total number of readers is %s.' % Reader.count)


if __name__ == '__main__':
    a=Reader('张三','中国')
    a('Nice')

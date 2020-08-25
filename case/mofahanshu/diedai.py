

class diedai:
      '''
      自定义的迭代对象：必须要同时重载iter和next方法，才是一个迭代对象。
      迭代对象 iter负责产生数据迭代对象，next负责拿到这个数据。
      iter的返回部分可以是其他对象的实例，然后next可以在这个对象内。实现
      在这里时，iter负责返回对象本份，next对数据进行加工处理。
      当创建实例后，调用next时，直接执行next
      当遍历的时候，调用for range时，是先执行iter部分

      '''

      def __init__(self,start,stop):
            self.value=start-1
            self.stop=stop
      def __iter__(self):
            ''''''
            return self

      def __next__(self):
            '''进行迭代的时候必须引发异常，进行停止迭代。'''
            if self.value==self.stop:
                  raise StopIteration
            else:
                  self.value+=1
            return  self.value


'''
委托代理
'''
class  diedaier:

      def __iter__(self):
            return  nex()

class nex:
      pass




if __name__ == '__main__':
    from collections import  Iterator,Iterable

    d=diedai(5,9)
    print(d,isinstance(d,Iterator))
    print(d, isinstance(d, Iterable))
    #调用__next__方法时，先执行next
    print(d.__next__())
    print(d.__next__())
    print(d.__next__())
    print(d.__next__())

    #遍历时，先执行iter
    for i in diedai(4,9):
          print(i,end='')

    #迭代一些iter和next写在两个不同的类里面，
    d2=diedaier()
    print(isinstance(d2,Iterable))
    print(d2)

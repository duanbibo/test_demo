
'''   索引和切片'''
class  lie:
      '''注释：自定义类实现序列结构'''

      def __init__(self,*li):
            self.li=list(li)
      def  __getitem__(self, item):
            '''  用来处理切片用的方法'''
            return  self.li[item]
      def __setitem__(self, key, value):
             '''用来切片赋值的'''
             self.li[key]=value
      def __contains__(self, item):
            '''用来检测是否成员的'''
            return  item in self.li
      def __str__(self):
            return ' %s'%(self.li)
      # def __iter__(self):
      #       return self.li





if __name__ == '__main__':
    from collections import Iterable, Iterator

    #利用getitem进行切片
    X=lie(1,2,3,4,5,6)
    print(isinstance(X, Iterable))
    print(X[2])
    print(X[:3])



    for i  in range(5):
          print(i,end=' ')  #end='' 代表不换号

    for  o in X:
          print(o,end='')

    #利用setitem进行赋值
    list1=[1,2,3]
    list1[2]=2
    print(list1)

    X[2]=5
    print(X)
    print(X.__dict__,lie.__dict__)

    #自定义的序列竟然不是可迭代对象
    #因为定义的序列对于解释器而言，可以进行迭代操作
    #我定义了iter后，判断是可迭代对象了，但是由于我只定义了iter后，没有定义next方法，在迭代的时候报错。
    # 如果我不定义iter方法，可以正常的进行迭代。
    print(isinstance(X,Iterator))
    print(isinstance(X, Iterable))

    li=[1,2,3,4,5]
    print(isinstance(li, Iterable))

    #测试关系运算符 in
    print(2 in X)


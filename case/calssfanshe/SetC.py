
class Setclass1:
      '''
      通过自定义创建set集合的类型，首先要明白set集合的特性
      1.set集合初始化生成后具有去重功能
      2.set集合本身是list集合+去重
      所以在构造器里面，我们制定一个空列表接口传的参，同时在构造器内直接调用方法来处理初始化后列表，检验是否去重

      '''

      def  __init__(self,value=[ ]):
            self.data = []  # 这个属性主要是用来装处理后的数据
            self.concat(value)                 #  这个方法主要是每次调用对象时去调用的方法



      def concat(self,value):
            '''  这个方法主要来处理列表元素校验，进行去重'''
            for x in value:
                  if not x in self.data:
                        self.data.append(x)

      def __str__(self):
            return  'Set:  %s' %(self.data)

if __name__ == '__main__':

    s=Setclass1([1,3,4,4,5])
    print(s.data)
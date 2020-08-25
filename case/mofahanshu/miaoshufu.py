

'''

描述符： 将类的属性通过其他类的get ,set ,del的内置方法定义。

'''

class  nameDecriptor:

      def __get__(self, instance, owner):
            print(instance,owner)

      def __set__(self, instance, value):
            print(instance,value)
      def __delete__(self, instance):
            pass

class  person:

      #方式一：通过类描述符
      name=nameDecriptor()

      def getAge(self):
            return  self.age

      def setAge(self, value):
            self.age = value

      def delAge(self):
            del self.age
       #方式二：通过特性函数，将多个方法写在内。
      age=property(getAge,setAge,delAge,"说明文档")

      #方式三：通过特性的装饰器



if __name__ == '__main__':
      p=person()
      p.name  #调用get方法
      p.name='张三'  #调用set方法







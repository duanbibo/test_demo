from decorator import decorate


class lei():

      def __init__(self,func):
            self.func=func
            print("执行装饰器的构造函数")

      def __call__(self, *args, **kwargs):
            print("执行回调函数")
            print(*args,"打印参数列表")
            return self.func(*args)  #核心就这这部分。
           # print("回到回调函数内")


@lei
def  fangfa(x):
      return print(x,"哈哈")


fangfa("5")

import shelve
class o:

      def __init__(self,name):
            self.__name=name


      def info(self,id):
            print(self.__name+"的学号是"+id)



a=o("张三")
a.info("001")



f=shelve.open(r"G://settings.txt")

f["k"]=a
f.close()
print("over")





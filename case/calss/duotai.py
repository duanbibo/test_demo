class Animal:

    def kind(self):
        print("i am animal")


class Dog(Animal):

    def kind(self):
        print("i am a dog")

class Job():

    def kind(self):
        print("i am not animal, i am a job")
        self.kind()
        Animal.kind()


# 这个函数接收一个animal参数，并调用它的kind方法
def show_kind(animal):
    animal.kind()


d = Dog()
j = Job()


show_kind(d)
show_kind(j)

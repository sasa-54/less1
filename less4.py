#успадкування дочірнє
class Grandparent:
    height = 170
    satiety = 100
    age = 60

class Parent(Grandparent):
    age = 40

class Child(Parent):
    height = 50
    def __init__(self):
        print(self.height)
        print(self.satiety)
        print(self.age)




#інкапсуляції
class Hello_world:
    hello = "Hello" #public
    __hello = "__Hello" #private (не використовуєтьяс ззовні)

    def __init__(self):
        self.world = "World"
        self._world = "_World"
        self.__world = "__World"

    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)

hello = Hello_world()
#hello.__hello - error



# super()  дозволяє використовувати батьківські методи у дочірньому класі.

class Grandparent:
    def about(self):
        print("I am GrandParent")

        print("I am Grandparent")


class Parent(Grandparent):
    def about_myself(self):
        print("I am Parent")


class Child(Parent):
    def __init__(self):
        super().about()
        super().about_myself()


# МНОЖИННЕ УСПАДКУВАННЯ
class Computer:
    def calculate(self):
        print("Calculating…")

class Display:
    def display(self):
        print("I display the image on the screen…")


class SmartPhone(Display, Computer):
    pass


iphone = SmartPhone()
iphone.calculate()
iphone.display()
























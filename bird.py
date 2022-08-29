#write a program that has a class bird wih constructor arguments name, color.
#And create a child named parrot from the class Birs,create a method.
#can_fly in the child class and call the method.

class bird:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def __del__(self):
        print("memory is freed")
class parrot(bird):
    def __init__(self, name, color):
        super().__init__(name, color)
    def can_fly(self):
        print(f"color is {self.color} and name is {self.name}")
bird = parrot(name="crow",color="black")
bird.can_fly()
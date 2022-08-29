class Dog:
    def __init__(self, name) :
        self.name = name


    def speak(self):
        print(f"{self.name} speaks woof woof!")


tommy = Dog(name='Tommy einstein')
tommy.speak()
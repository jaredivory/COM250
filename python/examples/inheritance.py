class Animal:
    def walk(self):
        print("walk")
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print('bork')
    def speak
    

class Cat(Animal):
    def meow(self):
        print("Meow")

dog = Dog('Rufus')
dog.walk()
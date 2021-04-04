# Object Oriented Programming in Python

class Cat:

    def __init__(self, name): # Instantiate the object right when it's created
        self.name = name
        print(name)

    def meow(self):
        print("Meow!")


class Dog:
    def bark(self):
        print("Vau!")

    def eat(self, belly):
        return belly + 1


# Instantiate these classes
c = Cat("Tom")
d = Dog()

c.meow()
d.bark()

print(d.eat(0))

print(type(c), type(d))


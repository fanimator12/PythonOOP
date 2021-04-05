# Object Oriented Programming in Python

class Cat:

    def __init__(self, name, age): # Instantiate the object right when it's created
        self.name = name
        self.age = age
        print(name)

    def meow(self):
        print("Meow!")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


class Dog:

    def __init__(self, name, age): # Instantiate the object right when it's created
        self.name = name
        self.age = age

    def bark(self):
        print("Vau!")

    def eat(self, belly):
        return belly + 1

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name


# Instantiate these classes
c = Cat("Tom", 10)
d = Dog("George", 4)
d2 = Dog("John", 6)

print(d.name, d.age)
print(d2.get_name(), d.get_age())
print(c.get_name(), c.age)

d.name = "Nielsen"

print(d.name, d.age)

c.meow()
d.bark()

print(d.eat(0))

print(type(c), type(d))


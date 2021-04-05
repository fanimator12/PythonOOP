# Object Oriented Programming in Python

class Pet:
    def __init__(self, name, age):  # Instantiate the object right when it's created
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("Don't know what to say")


class Cat(Pet):

    def __init__(self, name, age, color):
        super().__init__(name, age)  # Inherit the attributes from Pet class
        self.color = color

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

    def speak(self):
        print("Meow!")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


class Dog(Pet):

    def speak(self):
        print("Vau!")

    def eat(self, belly):
        return belly + 1

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name


class Frog(Pet):
    pass


# Instantiate

p = Pet("Tom", 5)
p.show()
p.speak()

c = Cat("Tom", 10, "brown")
c.show()

d = Dog("George", 4)
d.show()

d2 = Dog("John", 6)
d2.show()

f = Frog("Prince", 2)
f.speak()

print(d.name, d.age)
print(d2.get_name(), d.get_age())
print(c.get_name(), c.age)

d.name = "Nielsen"

print(d.name, d.age)

c.speak()
d.speak()

print(d.eat(0))

print(type(c), type(d))

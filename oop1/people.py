class Person:
    number_of_people = 0
    GRAVITY = -9.8

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):  # Acting on this class
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


person1 = Person("Jim")
person2 = Person("Joe")
print(Person.number_of_people_())

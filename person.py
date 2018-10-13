class Person:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_name(self):
        print('person name is %s' % self.name)

    def say_age(self):
        print('person age is %d' % self.age)

    def birthday(self):
        self.age += 1

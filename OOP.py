from enum import Enum

#OOP in python

class Gender(Enum):
    MALE = 1
    FAMALE = 2
    
class Person:
    def __init__(self, name, lastName, age, gender):
        self.name = name
        self.lastName = lastName
        self.age = age
        self.gender = gender
    def __str__(self):
        return "name: {} lastName: {} age: {} gender: {}".format(self.name, self.lastName, self.age, self.gender)

person = Person("sepehr", "mollaei", 20, Gender.MALE.name)
print(person)


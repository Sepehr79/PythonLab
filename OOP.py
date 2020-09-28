from enum import Enum

#OOP in python


#defining enum for gender
class Gender(Enum):
    MALE = 1
    FAMALE = 2
    
class Person:
    def __init__(self, name, lastName, age, gender):
        self.name = name
        self.lastName = lastName
        self.age = age
        self.gender = gender
    
    #__str__ method return string of object
    
    def __str__(self):
        return "name: {} lastName: {} age: {} gender: {}".format(self.name, self.lastName, self.age, self.gender)
        
    #methods to comparison objects    
        
    def __eq__(self, other):
        if(isinstance(self, other)):
            return (self.age == other.age)
    def __ne__(self, other):
        return (self.age != other.age)

    def __lt__(self, other):
        return (self.age < other.age)

    def __le__(self, other):
        return (self.age <= other.age)

    def __gt__(self, other):
        return (self.age > other.age)

    def __ge__(self, other):
        return (self.age >= other.age)
        
        
sepehr = Person("sepehr", "mollaei", 20, Gender.MALE.name)
ali = Person("ali", "mohammadi", 21, Gender.MALE.name)

if ali > sepehr:
    print("ali is grater!")


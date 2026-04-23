# in this session we will learn about inheritance and polymorphism
# inheritance is a way to create a new class from an existing class. T
# the new class is called the child class and the existing class is called the parent class.
# The child class inherits the properties and methods of the parent class.

# we can aslo understand it in Hinglish as
# "Ek class dusre class se apne properties aur methods ko inherit kar sakti hai"

# aur behtareen baat ye hai ki child class apne properties aur methods ko override kar sakti hai.
# iska matlab hai ki child class apne properties aur methods ko
# parent class ke properties aur methods se alag kar sakti hai.

# let's see an example of inheritance in python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.name)  # Output: Buddy
print(dog.speak())  # Output: Woof!
print(cat.name)  # Output: Whiskers
print(cat.speak())  # Output: Meow!

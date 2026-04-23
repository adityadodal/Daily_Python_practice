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
from abc import ABC, abstractmethod


class Animal:  # parent class
    def __init__(self, name):  # constructor method
        self.name = name  # instance variable

    def speak(self):  # method to be overridden by child classes
        return "I am an animal"  # default implementation of speak method


class Dog(Animal):  # ye Dog class Animal class se inherit kar rahi hai
    def speak(self):  # ye Dog class apne speak method ko override kar rahi hai
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


# Abstraction ek aisi concept hai jisme hum apne code ko is tarah se design karte hain ki user ko sirf zaroori information hi mile aur baki details chhupayi jayein.
# Iska matlab hai ki hum apne code ko is tarah se likhte hain ki user ko sirf wohi methods aur properties dikhai dein jo unke liye zaroori hain, aur baki implementation details chhupayi jayein.
# Abstraction ko achieve karne ke liye hum abstract classes aur interfaces ka use karte hain.
# Abstract class ek aisi class hoti hai jisme kuch methods abstract hote hain,
# matlab unka implementation nahi hota hai. Aur interfaces ek aisi class hoti hai jisme sirf abstract methods hote hain, matlab unka implementation nahi hota hai.
# Abstraction ko samajhne ke liye hum ek example dekhte hain.


class Shape(ABC):  # ye Shape class ek abstract class hai
    @abstractmethod
    def area(self):  # ye area method ek abstract method hai
        pass


class Circle(Shape):  # ye Circle class Shape class se inherit kar rahi hai
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # ye Circle class apne area method ko implement kar rahi hai
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circle = Circle(5)
rectangle = Rectangle(4, 6)
print(circle.area())  # Output: 78.5
print(rectangle.area())  # Output: 24


# Polymorphism ek aisi concept hai jisme hum apne code ko is tarah se design karte hain ki ek hi method ya function alag alag tarah se behave kare.
# Iska matlab hai ki hum apne code ko is tarah se likhte hain ki ek hi method ya function alag alag classes mein alag alag tarah se implement ho sake.
# Polymorphism ko achieve karne ke liye hum method overriding aur method overloading ka use karte hain.
# Method overriding ek aisi technique hai jisme child class apne parent class ke method ko override kar sakti hai, matlab apne tarah se implement kar sakti hai.
# Method overloading ek aisi technique hai jisme hum ek hi method ko alag alag tarah se implement kar sakte hain, matlab ek hi method ke multiple versions bana sakte hain.
# Polymorphism ko samajhne ke liye hum ek example dekhte hain.

class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass


class Sparrow(Bird):
    def fly(self):
        return "Sparrow can fly"


class Penguin(Bird):
    def fly(self):
        return "Penguin cannot fly"


sparrow = Sparrow()
penguin = Penguin()
print(sparrow.fly())  # Output: Sparrow can fly
print(penguin.fly())  # Output: Penguin cannot fly

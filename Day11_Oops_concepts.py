# In this session we will learn about OOPS concepts in python

# OOPS stands for Object Oriented Programming System

# In OOPS we have 4 main concepts
# 1. Class
# 2. Object
# 3. Inheritance
# 4. Polymorphism

# 1. Class: A class is a blueprint for creating objects.
# It defines a set of attributes and methods that the objects created from the class will have.

# 2. Object: An object is an instance of a class.
# It is created from a class and has all the attributes and methods defined in the class.

# 3. Inheritance: Inheritance is a mechanism in which a new class is derived from an existing class.
# The new class is called the child class or subclass, and the existing class is called the parent class or superclass.
# The child class inherits all the attributes and methods of the parent class and can also have its
# own attributes and methods.
# 4. Polymorphism: Polymorphism is the ability of an object to take on many forms.
# It allows us to use a single interface to represent different types of objects.
# Now let's see how to implement these concepts in python


# 1. Class and Object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Creating an object of the Person class
person1 = Person("Alice", 30)
# Accessing the attributes and methods of the object
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30
person1.display()    # Output: Name: Alice, Age: 30
# 2. Inheritance


class Student(Person):

    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call the constructor of the parent class
        self.student_id = student_id

    def display_student(self):
        print(f"Student ID: {self.student_id}")


# Creating an object of the Student class
student1 = Student("Bob", 20, "S12345")
# Accessing the attributes and methods of the object
print(student1.name)  # Output: Bob
print(student1.age)   # Output: 20
print(student1.student_id)  # Output: S12345
student1.display()    # Output: Name: Bob, Age: 20
student1.display_student()  # Output: Student ID: S12345
# 3. Polymorphism


class Animal:
    def sound(self):
        pass  # This is a placeholder method, it will be overridden by the child classes


class Dog(Animal):
    def sound(self):
        return "Woof"


class Cat(Animal):
    def sound(self):
        return "Meow"


# Creating objects of the Dog and Cat classes
dog1 = Dog()
cat1 = Cat()
# Accessing the sound method of the objects
print(dog1.sound())  # Output: Woof
print(cat1.sound())  # Output: Meow


# In this session we have learned about OOPS concepts in python and how to implement them using classes and objects.
# We have also seen how to use inheritance and polymorphism in python.
# OOPS is a powerful programming paradigm that allows us to create reusable and modular code.

# In the next session we will learn about more advanced OOPS concepts like encapsulation and abstraction.
# Stay tuned!

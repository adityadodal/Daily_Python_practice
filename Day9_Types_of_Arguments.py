# In this session we will learn about the types of arguments in python functions.

# 1. Positional Arguments: These are the most common type of arguments. They are passed to the function in the order they are defined.

def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")


greet("Alice", 30)  # Output: Hello Alice, you are 30 years old.


# 2. Keyword Arguments: These are passed to the function using the name of the parameter.
# This allows you to pass arguments in any order.

greet(age=30, name="Alice")  # Output: Hello Alice, you are 30 years old.

# 3. Default Arguments: These are arguments that have a default value.
# If the caller does not provide a value for that argument, the default value will be used.


def greet(name, age=25):
    print(f"Hello {name}, you are {age} years old.")


greet("Bob")  # Output: Hello Bob, you are 25 years old.


def add(first, second):
    return first + second


result = add(5, 10)

print(result)  # Output: 15

print(add(3, 4))  # Output: 7
print(add(first=10, second=20))  # Output: 30
print(add(5, second=15))  # Output: 20

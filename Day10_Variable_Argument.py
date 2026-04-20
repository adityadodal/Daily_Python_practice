# Variable Arguments in Python
# *args and **kwargs are used to pass a variable number of arguments to a function.
# *args allows you to pass a variable number of non-keyword arguments to a function.
# **kwargs allows you to pass a variable number of keyword arguments to a function.

def add(*numbers):
    sum = 0
    for i in numbers:
        sum += sum + i
    return sum


print(add(1, 2, 3, 4, 5, 6))


def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")


print_info(name="Alice", age=30, city="New York")
# You can also combine *args and **kwargs in the same function


def display_info(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)
    print("\nKeyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


display_info("Hello", "World", name="Alice", age=30)

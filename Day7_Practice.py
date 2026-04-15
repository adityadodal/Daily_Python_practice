# Built in functions

# print() - prints the given object to the console
# print("Hello, World!")

# def - defines a function

def testing():
    print("Testing function")
    print("Testing Completed")


# calling the function
testing()


def testing2(first_name, last_name):
    print(f"Testing function : {first_name} {last_name}")
    print("Testing Completed")
    print(f"Hello {first_name} {last_name}")


# calling the function
testing2("John", "Doe")

testing2("Aditya", "Dodal")


# this function takes two numbers and returns their sum
def add_numbers(num1, num2):
    return num1 + num2


# calling the function and storing the result in a variable
result = add_numbers(5, 56)
print(f"The sum of 5 and 56 is: {result}")

# we can also automatically print the result without storing it in a variable
print(f"The sum of 5 and 56 is: {add_numbers(5, 56)}")

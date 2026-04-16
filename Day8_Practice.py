# IN THIS SESSION WE WILL LEARN ABOUT TYPES OF FUNTIONS IN PYTHON

# 1. Built in functions
# 2. User defined functions

# TYOES OF FUNTIONS
# 1. PERFORM A TASK
# 2. CALCULATE AND RETURN A VALUE

# 1. PERFORM A TASK
# EXAMPLE 1

def testing(first_name, last_name):
    print(f"testing name : {first_name} {last_name}")


testing("John", "Doe")

testing("Aditya", "Kumar")


def testing2(first_name, last_name):
    return f"testing name : {first_name} {last_name}"


message = testing2("Aditya", "Kumar")
print(message)
print(message.lower())
print(message.upper())


print(testing2("Aditya", "Kumar"))
print(testing2("Aditya", "Kumar").lower())


# NONE IS A SPECIAL VALUE IN PYTHON WHICH INDICATES THE ABSENCE OF A VALUE
# IF A FUNCTION DOES NOT RETURN ANY VALUE THEN IT RETURNS NONE BY DEFAULT
def testing3(first_name, last_name):
    print(f"testing name : {first_name} {last_name}")
    return "..."


print(testing3("Aditya", "Kumar"))


# EXAMPLE 2
def add(a, b):
    return a + b


result = add(10, 20)
print(result)


def add_and_substract(a, b):
    return a + b, a - b


add_result, substract_result = add_and_substract(10, 20)
print(f"Addition: {add_result}, Subtraction: {substract_result}")

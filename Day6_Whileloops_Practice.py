# In this session we will Learn abput while loops in python

# Syntax of while loop
# while condition:
#     # code to be executed

count = 1
while count <= 5:
    print("Count is :", count)
    count += 1

# Example 2: Print numbers from 1 to 10
num = 1
while num <= 10:
    print("Number is :", num)
    num += 1

# Example 3: Calculate the sum of first n natural numbers
n = 5
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("The sum of first", n, "natural numbers is:", sum)


while True:
    command = input(">>>>")
    print(command)

    if command == "exit":
        print("Exiting the program...")
        break


while True:
    command = input(">>>>")
    print(command)

    if command.lower() == "quit":
        print("Exiting the program...")
        break


# lets creat a simple calculator using while loop

while True:
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting the calculator...")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = num1 + num2
        print("Result:", result)
    elif choice == '2':
        result = num1 - num2
        print("Result:", result)
    elif choice == '3':
        result = num1 * num2
        print("Result:", result)
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid choice. Please try again.")

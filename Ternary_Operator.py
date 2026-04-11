# age = 14
# if age >= 18:
#    status = "WELCOME TO THE PARTY! ENJOY!"
# else:
#    status = "SORRY, YOU ARE NOT ALLOWED TO ENTER THE PARTY."
# print(status)


# USING TERNARY OPERATOR
Age = 21
Status = "Welcome to the Party Enjoy!" if Age >= 18 else "Sorry, you are not allowed to enter the party."
print(Status)


# Basic Party Form for a Candidate using Ternary Operator
name = input("Enter candidate's name: ")
status_input = input("Are they single or a couple? ").lower()
# Using ternary to standardize status
status = "single" if status_input in ["single", "s"] else "couple"
print(f"Name: {name}, Status: {status}")

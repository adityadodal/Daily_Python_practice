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

# Party Form for Candidates
candidates = []

while True:
    name = input("Enter candidate's name (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    status = input("Are they single or a couple? ").lower()
    # Using ternary to standardize status
    status = "single" if status in ["single", "s"] else "couple"
    candidates.append({"name": name, "status": status})

print("\nParty Candidates:")
for candidate in candidates:
    print(f"Name: {candidate['name']}, Status: {candidate['status']}")



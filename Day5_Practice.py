# In this file we will learn about nested for loops and how to use them in Python.

# A nested for loop is a for loop that is inside another for loop.
# The inner for loop will be executed for each iteration of the outer for loop.

for i in range(5):
    for j in range(3):
        print(f"{i}, {j}")
# In this example, the outer for loop will iterate 5 times (i = 0 to 4)
# and for each iteration of the outer loop, the inner loop will iterate 3 times (j = 0 to 2).
# The output of this code will be:
# 0, 0
# 0, 1
# 0, 2
# 1, 0
# 1, 1
# 1, 2
# 2, 0
# 2, 1
# 2, 2
# 3, 0
# 3, 1
# 3, 2
# 4, 0
# 4, 1
# 4, 2
# We can also use nested for loops to create patterns. For example, we can create a pattern of stars:
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()
# In this example, the outer for loop will iterate 5 times (i = 0 to 4)
# and for each iteration of the outer loop, the inner loop will iterate i + 1 times (j = 0 to i).
# The output of this code will be:
# *
# **
# ***
# ****
# *****

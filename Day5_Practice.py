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


for i in range(n):
    for j in range(i + 1):
        print("*", end="")
    print()
# In this code, we can replace n with any positive integer to create a pattern of stars
# For example, if we set n = 3, the output will be:
# *
# **
# ***
# We can also use nested for loops to create a multiplication table:
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()
# In this example, the outer for loop will iterate from 1 to 10 (i = 1 to 10)
# and for each iteration of the outer loop, the inner loop will iterate from 1 to 10 (j = 1 to 10).
# The output of this code will be a multiplication table from 1 to 10.
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# ...
# 10 x 8 = 80
# 10 x 9 = 90
# 10 x 10 = 100
# Nested for loops are a powerful tool in Python and can be used to solve a variety of problems.
# They allow us to iterate through multiple levels of data and create complex patterns and structures.
# In the next section, we will learn about list comprehensions and how to use them in Python.

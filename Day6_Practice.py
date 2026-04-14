# In this Ecersise we will Learn about Iterables in python
# Iterables are objects that can be looped over, such as lists, tuples, strings, and dictionaries.
# We can use a for loop to iterate over an iterable and perform some action on each element

# Range is a built-in function that generates a sequence of numbers.
for i in range(5):
    # Range function is iterable, which means we can use a for loop to iterate over it.
    print(i)
   # The range function takes three arguments: start, stop, and step.
   # The start argument is the number at which the sequence starts (default is 0),
   # #the stop argument is the number at which the sequence ends (exclusive),
   #  and the step argument is the difference between each number in the sequence (default is 1).
   # In this case, it generates the numbers 0 to 4.


# We can also use a for loop to iterate over a list of items
fruits = ["apple", "banana", "Cherry", "date", "elderberry"]
for fruit in fruits:
    print(fruit)


for i in range(1, 11):
    print(i)

for i in "Aditya":
    '''Strings are also iterable, which means we can use a for loop to iterate over each character in the string.'''
    print(i)

# We can also use a for loop to iterate over a dictionary
person = {"name": "Aditya", "age": 25, "city": "New York"}
for key in person:
    print(key, person[key])


for i in [1, 2, 3, 4, 5]:  # We can also use a for loop to iterate over a list of numbers
    print(i)

for i in (1, 2, 3, 4, 5):  # We can also use a for loop to iterate over a tuple of numbers
    print(i)

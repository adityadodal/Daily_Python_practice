def add(first, second, third, fourth=0):
    return first + second + third + fourth


print(add(1, 2, 3))
print(add(1, 2, 3, 4))


def add(first, second, third=0, fourth=0):
    return first + second + third + fourth


print(add(1, 2))  # 3
print(add(1, 2, 3))  # 6
print(add(1, 2, 3, 4))  # 10


def add(first, second, third=0, fourth=0):
    return first + second + third + fourth

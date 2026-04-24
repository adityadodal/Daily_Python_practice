# in this session we learn about polymorphism and inheritance

# plymorphism ek #object oriented programming concept hai jisme ek function ya method ka
#  behavior alag alag #class ke objects ke liye alag hota hai.
# Iska matlab hai ki aap ek hi function ya method ko different classes ke
# objects ke liye use kar sakte hain, aur har class apne hisab se us
# function ya method ko implement kar sakti hai.

# inheritance ek aur object oriented programming concept hai jisme ek class
# dusri class se properties aur behaviors inherit kar sakti hai.
# Iska matlab hai ki aap ek class ko parent class bana sakte hain, aur
# dusri class ko child class bana sakte hain. Child class parent class ke
# properties aur behaviors ko inherit kar sakti hai, aur apne hisab se
# unhe modify kar sakti hai.

# types of polymorphism:

# static polymorphism: isme function overloading hota hai, jisme ek hi function
# ka naam hota hai, lekin uske parameters alag hote hain.
# Iska matlab hai ki aap ek hi function ko different parameters ke saath call kar sakte hain,
#  aur har call ke liye function apne hisab se behave karega.

# dynamic polymorphism: isme function overriding hota hai, jisme ek child class
# parent class ke function ko override kar sakti hai. Iska matlab hai ki aap
# ek child class ke object ke liye parent class ke function ko call kar sakte hain,
#  aur child class ke function ko call kar sakte hain, aur dono functions apne hisab se behave karenge.

# static polymorphism mein function overloading hota hai, jisme ek hi function ka naam hota hai, lekin uske parameters alag hote hain.
# dynamic polymorphism mein function overriding hota hai, jisme ek child class parent class ke function ko override kar sakti hai.

# example of static polymorphism:

class Calculator:
    def add(seldf, a, b):
        return a + b

    def add(seldf, a, b, c):
        return a + b + c


calc = Calculator()
# This will give an error because the second add method is overriding the first one

print(calc.add(2, 3, 4))  # This will work and return 9

# This will give an error because the first add method is overridden by the second one
print(calc.add(0, 2, 3))

# example of dynamic polymorphism:


class Parent:
    def greet(self):
        return "Hello from Parent"


class Child(Parent):
    def greet(self):
        return "Hello from Child"


parent = Parent()
child = Child()
print(parent.greet())  # This will print "Hello from Parent"
print(child.greet())   # This will print "Hello from Child"


# method overriding ka example:

# definition: method overriding ek concept hai jisme ek child class parent class ke method ko override kar sakti hai.
#  Iska matlab hai ki aap ek child class ke object ke liye parent class ke method ko call kar sakte hain,
#  aur child class ke method ko call kar sakte hain, aur dono methods apne hisab se behave karenge.

class Parent:
    def greet(self):
        return "Hello from Parent"


class Child(Parent):
    def greet(self):
        return "Hello from Child"


parent = Parent()
child = Child()
print(parent.greet())  # This will print "Hello from Parent"
print(child.greet())   # This will print "Hello from Child"

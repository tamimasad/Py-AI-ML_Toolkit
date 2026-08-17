import math  # Importing math module to do math realted complex calculations
import fibo  # Importing fibo.py module to use its functions
from collections import (
    deque,
)  # Importing deque from collections module to use it as a queue

print("Tamim Asad")
name = "Nabila Afzal"
print(len(name))
print(name[0:6])  # It will print the first 6 characters of the name String .

# String Methods

subject = " Computer science And engineering "
print(subject.upper())
print(subject.lower())
print(subject.title())
print(subject.strip())
print(subject.find("sc"))
print(subject.replace("Computer", "Computer And Elecetrical"))
print("and" in subject)
print("Computer" in subject)  # Python is case-sensitive

# Numbers

x = 2
y = 5
z = -7
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(y // x)  # To get an integer from a division
print(y**x)  # To get y to the power x

# Number Functions

print(round(5 / 2))
print(abs(x - y))
print(math.ceil(y / x))
print(math.copysign(x, z))
# More in Python 3 Math module

# Type Conversion

tool = "Code"
number = 10
num_in = input("Enter a number for type conversion: ")
a = int(num_in)
print(number + a)

# Comparison operators

print(ord("b"))  # To get the ASCII value of a character ord(), function used
print(5 > 10)
print(5 < 10)
print(5 == "Number")
print(5 == 5)

# Conditionals

# input(), always returns a string . So nedd to covert it to needed format
score = int(input("Enter the score : "))
if score >= 93:
    print("You got A .")
elif 80 <= score <= 83:  # Chaining operator, Like we do in Algebra
    print("You got B .")
else:
    print("The score isn't in range .")

# Loops

for number in range(1, 3, 2):  # in range(start, end, increment)
    print("Nabila")  # Nabila will be printed only once

# For without range() function

for i in range(1, 6):
    print(
        i
    )  # i will print from 1 to 5. In range() the first one is the starting number and end is ending number_1

# Nested Loops

for x in range(3):
    for y in range(2):
        print(f"{x}, {y}")

she = "Nabila"
for x in range(len(she)):
    print(she[x].upper())

# To display even numbers from 1 to 10

print("Even numbers from 1 to 10 : ")
number = 1
while number <= 10:
    if number % 2 is 0:
        print(number)
    number += 1

# Functions

name_1 = "Tamim"
name_2 = "Nabila"


def passname(name1, name2):
    print(f"{name1} Loves 🤍 {name2}")


passname(name_1, name_2)

# Using the import from fibo

x = int(input("Enter a number to get Fibonacci series up to that number : "))
fibo.fib(x)  # Calling the fib() function from fibo.py module
fibo.fib2(x)  # Calling the fib2() function from fibo.py module

# The match statement


def error_type(error):
    match error:
        case 404:
            print("Not Found")
        case 101:
            print("Not responding")
        case _:
            print("Unknown error")


error = input("Enter an error code : ")
error_type(int(error))

# List as Stack

fruit = []
f_n = int(input("Enter the number of fruit varities: "))
for i in range(f_n):
    fruit_name = input("Enter the name of fruits: ")
    fruit.append(fruit_name)  # Adding fruit names to the list
for i in range(f_n):
    print(fruit.pop())  # Removing fruit names from the list in LIFO order

# List as Queue

st_name = deque([])  # Using deque in a list to use it as a queue
s_n = int(input("Enter the number of students: "))
for i in range(s_n):
    student_name = input("Enter the name of students: ")
    st_name.append(student_name)  # Adding student names to the list
for i in range(s_n):
    print(st_name.popleft())  # Printing students names from the list in FIFO order

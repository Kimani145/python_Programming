## Control flows in Python
# If...else ,if... elif...else
"""
if isinstance(1, int):
    print("1 is an integer")
    if 1 > 0:
        print("1 is positive")
        if 1 == 0:
            print("1 is indeed zero")
            # This block is skipped
        else:
            print("1 is not zero")
    else:
        print("1 is negative")
else:
    print("1 is not an integer")

temperature = 20
"""

# Single line if statement
#elif is used to check multiple conditions
"""
if temperature > 30:# Full collon means that the block of code is starting
    print("It's hot")
elif temperature >= 20:
    print("It's warm")
else:
    print("It's cold")

student_Score = 90
if student_Score >= 80:
    print("A")
elif student_Score >= 70:
    print("A-")
elif student_Score >= 60:
    print("B")
elif student_Score >= 50:
    print("C+")
elif student_Score >= 40:
    print("C-")
elif student_Score >= 30:
    print("D+")
elif student_Score >= 20:
    print("D-")
else:
    print("E")
# Nested if statement
    if temperature > 30:
    print("It's hot")
    if temperature > 35:
        print("It's really hot")
    else:
        print("It's not that hot")
else:
    print("It's not hot")
"""
#LOOPING
# For loop
#Definate and indefinate iteration
# Definate iteration

"""
for i in range(5):# This will loop/iterate from 0 to 4
    print(i)# This will print all the numbers from 0 to 4
    if i == 3:
        break# This will stop the loop when i is equal to 3
# Indefinate iteration

while True:
    user_input = input("Enter a number: ")
    if user_input.isdigit():
        break
    else:
        print("Invalid input")
# Looping through a list

numbers = [1, 2, 3, 4, 5]
for number in numbers:# This will loop/iterate through the list
    print(number)# This will print all the numbers in the list

# Looping through a dictionary
person = {
    "name": "John",
    "age": 36,
    "country": "Kenya"
}
for key, value in person.items():
    print(key, value)
"""
# While loop
"""
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        continue
    if i == 4:
        break
"""
# Break and Continue
# list comprehension
#Functions
# A function is a block of code that only runs when it is called
# Functions are used to perform specific tasks
# Functions are reusable
# Functions can be called multiple times
# Functions can take arguments
# Functions can return data

#Built-in functions are pre-defied functions in Python, e.g print(), input(), len()
# User-defined functions are defined by the users themselves
# User-defined Functions are defined using the def keyword
def greet(name):
    print("Hello", name)

greet(input("Enter your name: "))
# Default arguments
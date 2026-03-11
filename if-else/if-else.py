# Python If
age = 20

if age > 18:
    print("You can vote")

# Example 2
num = 10

if num > 5:
    print("Number is greater than 5")

# Example 3
marks = 80

if marks >= 50:
    print("You passed the exam")

# Example 4
temperature = 35

if temperature > 30:
    print("It is a hot day")

# Ex 5 
salary = 50000

if salary > 30000:
    print("You have a good salary")

# Python Else (5 Examples)
# Example 1
age = 15

if age > 18:
    print("You can vote")
else:
    print("You cannot vote")
#Example 2
num = 4

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
# Example 3
marks = 40

if marks >= 50:
    print("Pass")
else:
    print("Fail")
# Example 4
temperature = 20

if temperature > 30:
    print("Hot")
else:
    print("Normal weather")
# Example 5
balance = 1000

if balance >= 2000:
    print("Enough balance")
else:
    print("Low balance")

#Python Elif (5 Examples)
#Example 1
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")

#Example 2
number = 0

if number > 0:
    print("Positive")
elif number == 0:
    print("Zero")
else:
    print("Negative")
# Example 3
age = 30

if age < 18:
    print("Child")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")
#Example 4
day = 3

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
else:
    print("Other day")
#Example 5
temperature = 15

if temperature > 30:
    print("Hot")
elif temperature > 20:
    print("Warm")
else:
    print("Cold")
#Shorthand If (5 Examples)
#Example 1
a = 10
b = 5

if a > b: print("a is greater")
#Example 2
x = 20
y = 30

print("x is greater") if x > y else print("y is greater")

#Example 3
num = 8

print("Even") if num % 2 == 0 else print("Odd")

#Example 4
age = 22

print("Adult") if age >= 18 else print("Minor")
#Example 5
marks = 60

print("Pass") if marks >= 50 else print("Fail")

#Logical Operators (5 Examples)
#Example 1 – AND
age = 25
salary = 50000

if age > 18 and salary > 30000:
    print("Eligible for loan")
#Example 2 – OR
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
#Example 3 – NOT
is_logged_in = False

if not is_logged_in:
    print("Please login")
#Example 4
age = 20

if age > 18 and age < 60:
    print("Working age group")
#Example 5
marks = 40

if marks < 50 or marks == 50:
    print("Needs improvement")
#Nested If (5 Examples)
#Example 1
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
#Example 2
num = 10

if num > 0:
    if num % 2 == 0:
        print("Positive even number")
#Example 3
marks = 80

if marks >= 50:
    if marks >= 75:
        print("Distinction")
#Example 4
age = 25
salary = 60000

if age > 18:
    if salary > 50000:
        print("Eligible for premium card")
# Example 5
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
#Python Arithmetic Operators
x= 27
y = 8
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

sum1 = 100 + 250   
sum2 = sum1 + 250    
sum3 = sum2 + sum2   

print(sum1)
print(sum2)
print(sum3)

x = 12
y = 8

print(x / y)

#Floor division always returns an integer.
x = 12
y = 5

print(x // y)

#Comparision operators
x = 20
y = 14

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#Chaining Comparison Operators
#Python allows you to chain comparison operators:
x = 5

print(1 < x < 10)

print(1 < x and x < 10)



x = 5

print(x > 0 and x < 10)

#Test if a number is less than 5 or greater than 10:

x = 5

print(x < 5 or x > 10)

#Reverse the result with not:

x = 5

print(not(x > 3 and x < 10))

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

# Membership operators
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)


fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)

# Arithmetic operators example 
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

# Comparision operators
x = 10
y = 5

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Logical Operators
age = 25
salary = 30000

print(age > 18 and salary > 20000)
print(age > 18 or salary > 50000)
print(not(age > 18))

# Assignment operator
x = 10

x += 5
print(x)

x -= 3
print(x)

x *= 2
print(x)

# Identity operators 
a = [1,2,3]
b = a

print(a is b)
print(a is not b)

# Membership Operators
fruits = ["apple", "banana", "mango"]

print("apple" in fruits)
print("grape" not in fruits)

# Access list Item
fruits = ["apple", "banana", "mango"]

print(fruits[0])
print(fruits[1])
print(fruits[2])

# Change List Items
fruits = ["apple", "banana", "mango"]

fruits[1] = "orange"

print(fruits)

# Add List Items
fruits = ["apple", "banana"]

fruits.append("mango")

print(fruits)


# Remove list Item

fruits = ["apple", "banana", "mango"]

fruits.remove("banana")

print(fruits)

# Loop list 
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

# List Comprehension
numbers = [x for x in range(5)]

print(numbers)

# Sort list 
numbers = [5, 2, 8, 1]

numbers.sort()

print(numbers)

# Copy list 
fruits = ["apple", "banana"]

new_list = fruits.copy()

print(new_list)

# Join List 
list1 = ["a", "b"]
list2 = [1, 2]

list3 = list1 + list2

print(list3)

# List method 
numbers = [3, 1, 5]

numbers.sort()
numbers.reverse()

print(numbers)
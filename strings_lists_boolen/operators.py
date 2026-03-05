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


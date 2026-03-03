#positive and negative strings
a = "Gate Smashers"
print(a[5:10])
print(a[:10])
print(a[5:])
print(a[:])
print(a[-8:-3])
print(a[5::2])
print(a[::-1])
print(a[5:12])

# upper and lower case 
a = "Python is intresting!"
print(a.upper())

a = "Python is intresting!"
print(a.lower())

# Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)

#To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# format string
age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

#Perform a math operation in the placeholder, and return the result:

txt = f"The price is {20 * 59} dollars"
print(txt)

txt = f"The price is {20 * 112} dollars"
print(txt)

#ecsape caractre
txt = 'Im working in Techjar as "Jr devops operating" from last 8 months.'
print(txt)

#boolen value 
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 20
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#List Length
#To determine how many items a list has, use the len() function:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#List Items - Data Types
#List items can be of any data type:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

#A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]
print(list1)
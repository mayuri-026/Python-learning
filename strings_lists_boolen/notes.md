strings:----
slicing string
Modify string
concatnate string
Format string 
Escape string

## Slice To the End:-
By leaving out the end index, the range will go to the end:
b = "Hello, World!"
print(b[2:])
output-- llo, World!

string1 = "Gate Smashers"
 -12-11-10-9-8-7-6-5-4-3 -2 -1
G a  t   e   S m a s h e  r  s
0  1 2   3 4 5 6 7 8 9 10 11 12

substr1 = string1[5:10]
Smash

subbstr2 = string1[:10]
Gate smash

substr3 = string1[5:]
Smashers

substr4 = string1[:]
Gate Smashers

substr5 = string1[-8:-3]
Smash

substr6 = string1[5::2]
sahr

substr7 = string1[::-1]
shrhsams

substr8 = string1[5:12].upper()
SMASHER

Modify STring
Upper Case:--
The upper() method returns the string in upper case:

a = "Magna data"
print(a.upper())
ANS- MAGNA DATA

Lower Case
a = "Hello, World!"
print(a.lower())

String Concatenation
To concatenate, or combine, two strings you can use the + operator.

 Format string 
 To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
 Create an f-string:

age = 36
txt = f"My name is John, I am {age}"
print(txt)
My name is John, I am 36

Placeholders and Modifiers
A placeholder can contain variables, operations, functions, and modifiers to format the value.

Example
Add a placeholder for the price variable:

price = 59
txt = f"The price is {price} dollars"
print(txt)

Perform a math operation in the placeholder, and return the result:

txt = f"The price is {20 * 59} dollars"
print(txt)

Escape Character
To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to insert.
An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
txt = "We are the stxt = "We are the so-called \"Vikings\" from the north."o-called "Vikings" from the north."


# string method 
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning

## Boolean Values
In programming you often need to know if an expression is True or False.
You can evaluate any expression in Python, and get one of two answers, True or False.
When you compare two values, the expression is evaluated and Python returns the Boolean answer:
print(10 > 9)
print(10 == 9)
print(10 < 9)


print(10 > 9)
print(10 == 9)
print(10 < 9)

print(10 > 9)
print(10 == 9)
print(10 < 9)
​
True
False
False

## Python Lists
mylist = ["apple", "banana", "cherry"]

List
Lists are used to store multiple items in a single variable.

## Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.

## Arithmetic Operators
Arithmetic operators are used with numeric values to perform common mathematical operations:
Operator	    Name	       Example	
+	            Addition	     x + y	
-	            Subtraction	     x - y	
*	            Multiplication	 x * y	
/	            Division	     x / y	
%	            Modulus	         x % y	
**	            Exponentiation	 x ** y	
//	            Floor division	 x // y	

Division in Python
Python has two division operators:

/ - Division (returns a float)
// - Floor division (returns an integer)
x = 12
y = 5

print(x / y)
x = 12
y = 8

print(x / y)

Floor division always returns an integer.

It rounds DOWN to the nearest integer:

x = 12
y = 5

print(x // y)

# Assignment Operators
Assignment operators are used to assign values to variables:
Operator	Example	   Same As
-=	        x -= 3	   x = x - 3	
*=	        x *= 3	   x = x * 3	
/=	        x /= 3	   x = x / 3	
%=	        x %= 3	   x = x % 3	
//=	        x //= 3	   x = x // 3	
**=	        x **= 3	   x = x ** 3	
&=	        x &= 3	   x = x & 3	
|=	        x |= 3	   x = x | 3	
^=	        x ^= 3	   x = x ^ 3	
>>=       	x >>= 3	   x = x >> 3	
<<=	        x <<= 3	   x = x << 3	
:=	     print(x := 3)	x = 3 print(x)


# Comparison Operators
Comparison operators are used to compare two values:
operator    name                       Example
==	       Equal	                   x == y	
!=	       Not equal	               x != y	
>	       Greater than	               x > y	
<	       Less than	               x < y	
>=	       Greater than or equal to	   x >= y	
<=	       Less than or equal to	   x <= y

# Logical Operators
Logical operators are used to combine conditional statements:

Operator	    Description	                                    Example
and 	        Returns True if both statements are true	    x < 5 and  x < 10
or	            Returns True if one of the statements is true	x < 5 or x < 4
not	            Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

ExampleGet your own Python Server
Test if a number is greater than 0 and less than 10:

x = 5
print(x > 0 and x < 10)

# Identity Operators
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

# Difference Between is and ==
is - Checks if both variables point to the same object in memory
== - Checks if the values of both variables are equal

# Membership Operators
Membership operators are used to test if a sequence is presented in an object:

Operator	Description	            
in 	        Returns True if a sequence with the specified value is present in the object	        EX- x in y	
not in	    Returns True if a sequence with the specified value is not present in the object	        ex- x not in y

# Bitwise Operators
Bitwise operators are used to compare (binary) numbers:

Operator	Name	     Description	                                   Example
& 	        AND	         Sets each bit to 1 if both bits are                x & y	
|	        OR	         Sets each bit to 1 if one of two bits is 1	        x | y	
^	        XOR	         Sets each bit to 1 if only one of two bits is 1    x ^ y	
~	        NOT	         Inverts all the bits	                             ~x	
<<	        Zero fill left shift	Shift left by pushing zeros in from the right and let         the leftmost bits fall off	                                   x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2	


# operators with understanding
# Comparison Operators

हे True / False return करतात.


# Logical Operators

Conditions combine करण्यासाठी.

# Assignment Operators

Value assign करण्यासाठी.

# Identity Operators

Object same आहे का check करतात.

# Membership Operators

List / string मध्ये value आहे का check.

# What is a List?

A list is a collection of multiple values stored in one variable.

Example:

fruits = ["apple", "banana", "mango"]
print(fruits)

# Access List Items

List मधील items index number वापरून access करता येतात.
List मध्ये indexing 0 पासून सुरू होते.

Example
fruits = ["apple", "banana", "mango"]

print(fruits[0])
print(fruits[1])
print(fruits[2])

Output

apple
banana
mango
# Change List Items

Index वापरून list मधील item बदलता (modify) येतो.

Example
fruits = ["apple", "banana", "mango"]

fruits[1] = "orange"

print(fruits)

Output

['apple', 'orange', 'mango']

# Add List Items
List मध्ये नवीन item add करण्यासाठी append() किंवा insert() वापरतो.

Example
fruits = ["apple", "banana"]

fruits.append("mango")

print(fruits)

Output

['apple', 'banana', 'mango']


# Remove List Items

List मधील item delete करण्यासाठी remove(), pop(), किंवा del वापरतो.

Example
fruits = ["apple", "banana", "mango"]

fruits.remove("banana")

print(fruits)

Output

['apple', 'mango']


# Loop Lists
List मधील सर्व items print करण्यासाठी for loop वापरतो.

Example
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

Output

apple
banana
mango


# List Comprehension
List comprehension म्हणजे short method वापरून list तयार करणे.

Example
numbers = [x for x in range(5)]

print(numbers)

Output

[0, 1, 2, 3, 4]

# Sort Lists

List मधील items sort() method वापरून ascending order मध्ये arrange करता येतात.

Example
numbers = [5, 2, 8, 1]

numbers.sort()

print(numbers)

Output

[1, 2, 5, 8]


# Copy Lists
List ची duplicate copy बनवण्यासाठी copy() method वापरतो.

Example
fruits = ["apple", "banana"]

new_list = fruits.copy()

print(new_list)

Output

['apple', 'banana']


# Join Lists
दोन lists + operator वापरून join करता येतात.

Example
list1 = ["a", "b"]
list2 = [1, 2]

list3 = list1 + list2

print(list3)

Output

['a', 'b', 1, 2]


# List Methods

List मध्ये अनेक built-in methods असतात.

Common methods:

Method	     Use
append()	add item
insert()	add item at position
remove()	remove item
pop()	    remove by index
sort()	    sort list
reverse()	reverse list
copy()	    copy list

Example

numbers = [3, 1, 5]

numbers.sort()
numbers.reverse()

print(numbers)
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
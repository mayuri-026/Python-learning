Python is an interpreted programming language, this means that as a developer you write Python (.py) files in a text editor and then put those files into the python interpreter to be executed.

you can use the print() function to display text or output values

If you want to print multiple words on the same line, you can use the end parameter:

Print Numbers:- You can also use the print() function to display numbers
You can also do math inside the print() function.

you can combine text and numbers in one output by separating them with a comma.

Python Comments:-- 

Comments can be used to explain Python code.
Comments can be used to make the code more readable.
Comments can be used to prevent execution when testing code.

Comment = code madhla explanation text

Python comment execute kart nahi.
To fakta developer sathi explanation asto.
Comment = code madhla explanation text

# This is a comment
print("Hello, World!")

output - Hello, world!

Creating Variables--
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.

Variable - Variables are containers for storing data values.

You can get the data type of a variable with the type() function.
x = 5
y = "Jony"
print(type(x))
print(type(y))


String variables can be declared either by using single or double quotes:
x = "John"
print(x)
#double quotes are the same as single quotes:
x = 'John'
print(x)

Case-Sensitive
Variable names are case-sensitive.
a = 4
A = "techjar"

print(a)
print(A)

Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

Rules for Python variables:--

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.

Multi Words Variable Names
Variable names with more than one word can be difficult to read.

There are several techniques you can use to make them more readable:

Camel Case
Each word, except the first, starts with a capital letter:

myVariableName = "John"
Pascal Case
Each word starts with a capital letter:

MyVariableName = "John"
Snake Case
Each word is separated by an underscore character:

my_variable_name = "John"
 
Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:- x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
Learn

Data Types
intergers- +ve, -ve, 0
string- ' ' , " ", ''' '''
Float- 9.0, 34.9, 8.9
Booleans- Trues, false
None-a = none

Example	Data Type	Try it
x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType	

Python Numbers---
There are three numeric types in Python:

int
float
complex
x = 1    # int
y = 2.8  # float
z = 1j   # complex
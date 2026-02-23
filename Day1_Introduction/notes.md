What is Programming?
Programming is the process of writing instructions that tell a computer what to do.

Computers cannot understand human languages like English or Marathi.
They understand only binary numbers (0 and 1).

To communicate with a computer, we use programming languages such as Python.

Python is a high-level, interpreted programming language.
It converts human-readable code into machine code using an interpreter.

Key Features of Python...
Easy to understand and write
High-level language
Interpreted (executes line by line)
Cross-platform (Windows, Mac, Linux)
Free and open source
Rich standard library support

First Python Program
print("Hello World")

What is a .py File?
.py is the file extension used for Python programs.
Examples of file extensions:
movie.mp4
game.exe
program.py

Python Interpreter
Python uses an interpreter to execute code.

Variables in Python
A variable is a name used to store data in memory.

name = "Mayuri"
age = 23
price = 99.99
name → String
age → Integer
price → Float

Operators in Python
Arithmetic Operators
+   Addition
-   Subtraction
*   Multiplication
/   Division
%   Modulus (Remainder)
**  Exponent (Power)

Comparison Operators
==   Equal
!=   Not Equal
>    Greater than
<    Less than
>=   Greater than or equal to
<=   Less than or equal to
<<<<<<< HEAD


Rule for identifiers..
1. Identifier can be combination of uppercase and lowercase lettr, digits or an underscrore(_) so myvariable, variable_1, variable_for_print all are valid python identifiers. 
2. an identifier can not start with digit, so while variable1 is valid 1variable is not valid. 
3. Identifier can be of any length.
4. We cant use special symblo like !,#,@,%,$ etc in our identifier.


DAY 2 Notes 
Data Types in Python
String (str)

Used to store text.

Written inside single (' ') or double (" ") quotes.

Integer (int)

Used to store whole numbers.

No decimal point.

Integer (int)

Used to store whole numbers.

No decimal point.

Boolean (bool)

Stores only two values:

True

False
Boolean (bool)

Stores only two values:

True

False

is_student = True
is_logged_in = False


Implicit Type Conversion
Python automatically converts data types.
Happens when combining different numeric types.
ex:
a = 5       # int
b = 2.0     # float
result = a + b
print(result)   # 7.0

Explicit Type Conversion (Type Casting)
Done manually using functions.
Common type casting functions:
int()
float()
str()
bool()

Convert String to Integer
num = "10"
num = int(num)
print(num)

Convert Integer to String
age = 25
age_str = str(age)
print(age_str)

Convert Integer to Float
number = 10
number_float = float(number)
print(number_float)

Input Handling in Python
input()
name = input("Enter your name: ")
print(name)
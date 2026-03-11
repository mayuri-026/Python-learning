What is Conditional Statement
 Conditional statements are used to execute code based on a condition.
 Example

age = 20

if age > 18:
    print("You can apply for license")

Output

You can apply for license

# Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

# Types of Conditional Statements in Python
Simple if
if-else
if-elif-else
Nested if

# Simple if
Condition true असेल तर code execute होतो.

# if – else
Condition true → if block
Condition false → else block

# if – elif – else
Multiple conditions check करण्यासाठी वापरतात.

# Nested if

एका if मध्ये दुसरा if असतो.

# Multiple Elif Statements
You can have as many elif statements as you need. Python will check each condition in order and execute the first one that is true.

# How Elif Works
When you use elif, Python evaluates the conditions from top to bottom. As soon as it finds a condition that is true, it executes that block and skips all remaining conditions.

# The Else Keyword
The else keyword catches anything which isn't caught by the preceding conditions.

The else statement is executed when the if condition (and any elif conditions) evaluate to False.
You can also have an else without the elif:
You can combine if, elif, and else to create a comprehensive decision-making structure.

# Short Hand If
If you have only one statement to execute, you can put it on the same line as the if statement.
If you have one statement for if and one for else, you can put them on the same line using a conditional expression:
When to Use Shorthand If
Shorthand if statements and ternary operators should be used when:

The condition and actions are simple
It improves code readability
You want to make a quick assignment based on a condition

# Python Logical Operators
Logical operators are used to combine conditional statements. Python has three logical operators:

and - Returns True if both statements are true
or - Returns True if one of the statements is true
not - Reverses the result, returns False if the result is true

The not keyword is a logical operator, and is used to reverse the result of the conditional statement.

# and Operator Truth Table
Condition1	            Condition 2	           Result
True	                 True	                True
True	                 False	                False
False	                 True	                False
False	                 False	                False

or Operator Truth Table
Condition 1	            Condition 2	   Result
True	                True	       True
True	                False	       True
False	                True	       True
False	                False	       False

# Nested If Statements
You can have if statements inside if statements. This is called nested if statements.
How Nested If Works
Each level of nesting creates a deeper level of decision-making. The code evaluates from the outermost condition inward.

Multiple Levels of Nesting
You can nest as many levels deep as needed, but keep in mind that too many levels can make code harder to read.

# The pass Statement
if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
The pass statement is a null operation - nothing happens when it executes. It serves as a placeholder.

# Why Use pass?
The pass statement is useful in several situations:

When you're creating code structure but haven't implemented the logic yet
When a statement is required syntactically but no action is needed
As a placeholder for future code during development
In empty functions or classes that you plan to implement later


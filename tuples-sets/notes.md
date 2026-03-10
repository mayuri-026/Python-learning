# What is a Tuple?
Tuples are used to store multiple items in a single variable.
Tuple म्हणजे multiple values store करण्यासाठी वापरला जाणारा collection type आहे.
List सारखाच असतो पण Tuple immutable असतो म्हणजे once create केल्यावर values change करता येत नाहीत.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuple Items
Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
Allow Duplicates
Since tuples are indexed, they can have items with the same value:

Example
Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
('apple', 'banana', 'cherry', 'apple', 'cherry')

Tuple Length
To determine how many items a tuple has, use the len() function:

Example
Print the number of items in the tuple:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Access Tuple Items
You can access tuple items by referring to the index number, inside square brackets:
fruits = ("apple", "banana", "mango")
starts from 0 
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Negative Index

Negative indexing म्हणजे end पासून access करणे.
starts from -1 

# Update Tuples
Tuple immutable असतो म्हणजे direct value change करता येत नाही.
पण tuple → list convert करून change करू शकतो.

# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

But there are some workarounds.
Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

# Unpacking a Tuple
When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
out put - apple
banana
cherry

# Loop Through a Tuple
You can loop through the tuple items by using a for loop.
# Loop Through the Index Numbers
You can also loop through the tuple items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.

# Using a While Loop
You can loop through the tuple items by using a while loop.

# Join Two Tuples
To join two or more tuples you can use the + operator:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
output- 
('a', 'b', 'c', 1, 2, 3)

# Multiply Tuples
If you want to multiply the content of a tuple a given number of times, you can use the * operator:
# count() → tuple मध्ये एखादी value किती वेळा आहे ते सांगतो
2️⃣ index() → tuple मध्ये एखादी value पहिल्यांदा कोणत्या index वर आहे ते सांगतो

## Sets 
Set
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Note: the set list is unordered, meaning: the items will appear in a random order.

# Refresh this page to see the change in the result.

output- 
{'banana', 'apple', 'cherry'}
# Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.
Duplicates Not Allowed
Sets cannot have two items with the same value.
# Get the Length of a Set
To determine how many items a set has, use the len() function.

Set Items - Data Types
Set items can be of any data type:
ex- set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
# The set() Constructor
It is also possible to use the set() constructor to make a set.

# Access Set Items
Access Items
You cannot access items in a set by referring to an index or a key.
Access Set Items
Access Items
You cannot access items in a set by referring to an index or a key.
Set unordered असल्यामुळे index वापरून access करता येत नाही.

पण loop वापरून items access करता येतात.

# Add Items
Once a set is created, you cannot change its items, but you can add new items.

Add Sets
To add items from another set into the current set, use the update() method.

Add Any Iterable
The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

# Remove Item
To remove an item in a set, use the remove(), or the discard() method.

# Loop Items
You can loop through the set items by using a for loop:
Set मधील values loop वापरून print करता येतात.

# Join Sets
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.

# The union() method returns a new set with all items from both sets.

# When using the | operator, separate the sets with more | operators:


# Python frozenset
frozenset is an immutable version of a set.

Like sets, it contains unique, unordered, unchangeable elements.

Unlike sets, elements cannot be added or removed from a frozenset.

Creating a frozenset
Use the frozenset() constructor to create a frozenset from any iterable.

Method	            Shortcut	             Description
copy()	 	                             Returns a shallow copy	
difference()	    -	                 Returns a new frozenset with the difference	
intersection()	    &	                 Returns a new frozenset with the intersection	
isdisjoint()	 	                     Returns whether two frozensets have an intersection	
issubset()	        <= / <	                      Returns True if this frozenset is a (proper) subset of another	
issuperset()	    >= / >	             Returns True if this frozenset is a (proper) superset of another	
symmetric_difference()	^	              Returns a new frozenset with the symmetric differences	
union()	             |	                Returns a new frozenset containing the union


# Set Methods
Python has a set of built-in methods that you can use on sets.

# count() → एखादी value tuple मध्ये किती वेळा आहे ते सांगतो

# index() → एखादी value tuple मध्ये पहिल्यांदा कोणत्या index वर आहे ते सांगतो


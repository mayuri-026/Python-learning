# Dictionary
Dictionaries are used to store data values in key:value pairs.

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Dictionary Items
Dictionary items are ordered, changeable, and do not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

# Accessing Items
You can access the items of a dictionary by referring to its key name, inside square brackets:
student = {
    "name": "Mayuri",
    "age": 22
}

print(student["name"])
output - mayuri 

get() method वापरून value safely access करता येते.
Key exist नसेल तर get() error देत नाही, None return करतो.
Key exist नसेल तर get() error देत नाही, None return करतो.
values() method वापरून dictionary मधील सर्व values मिळतात.
# Change Values
You can change the value of a specific item by referring to its key name:

# Adding Items
Adding an item to the dictionary is done by using a new index key and assigning a value to it:

# Removing Items
There are several methods to remove items from a dictionary:

# Loop Through a Dictionary
You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

# Copy a Dictionary
You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

# Nested Dictionaries
A dictionary can contain dictionaries, this is called nested dictionaries.
Access Items in Nested Dictionaries
To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:

Loop Through Nested Dictionaries
You can loop through a dictionary by using the items() method like this:

# Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.

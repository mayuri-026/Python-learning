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
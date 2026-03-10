# Access Set Items
#1
s = {1,2,3}
for i in s:
    print(i)

#2
s = {"apple","banana","cherry"}
for fruit in s:
    print(fruit)

#3
s = {10,20,30}
for i in s:
    print(i)

#4
s = {"red","blue"}
for color in s:
    print(color)

#5
s = {5,6,7}
for i in s:
    print(i)

#6
s = {"python","java"}
for lang in s:
    print(lang)

#7
s = {100,200}
for i in s:
    print(i)

#8
s = {"a","b","c"}
for i in s:
    print(i)

#9
s = {9,8,7}
for i in s:
    print(i)

#10
s = {"cat","dog"}
for animal in s:
    print(animal)

# Add Set Items
#1
s = {1,2,3}
s.add(4)
print(s)

#2
s = {"apple","banana"}
s.add("cherry")
print(s)

#3
s = {10,20}
s.add(30)
print(s)

#4
s = {"red","blue"}
s.add("green")
print(s)

#5
s = {5,6}
s.add(7)
print(s)

#6
s = {"python"}
s.add("java")
print(s)

#7
s = {100}
s.add(200)
print(s)

#8
s = {"a","b"}
s.add("c")
print(s)

#9
s = {9,8}
s.add(7)
print(s)

#10
s = {"dog"}
s.add("cat")
print(s)

# Remove Set Items
#1
s = {1,2,3}
s.remove(2)
print(s)

#2
s = {"apple","banana","cherry"}
s.remove("banana")
print(s)

#3
s = {10,20,30}
s.discard(20)
print(s)

#4
s = {"red","blue","green"}
s.remove("blue")
print(s)

#5
s = {5,6,7}
s.discard(6)
print(s)

#6
s = {"python","java"}
s.remove("java")
print(s)

#7
s = {100,200,300}
s.discard(200)
print(s)

#8
s = {"a","b","c"}
s.remove("b")
print(s)

#9
s = {9,8,7}
s.discard(8)
print(s)

#10
s = {"dog","cat"}
s.remove("dog")
print(s)

# Loop Sets
#1
s = {1,2,3}
for i in s:
    print(i)

#2
s = {"a","b","c"}
for i in s:
    print(i)

#3
s = {10,20,30}
for i in s:
    print(i*2)

#4
s = {5,6,7}
for i in s:
    print(i+1)

#5
s = {"red","blue"}
for color in s:
    print(color)

#6
s = {1,2,3,4}
for i in s:
    print(i)

#7
s = {"python","java"}
for lang in s:
    print(lang.upper())

#8
s = {9,8,7}
for i in s:
    print(i)

#9
s = {"apple","banana"}
for fruit in s:
    print(fruit)

#10
s = {100,200}
for i in s:
    print(i/10)

# Join Sets
#1
s1 = {1,2}
s2 = {3,4}
print(s1.union(s2))

#2
s1 = {"a","b"}
s2 = {"c","d"}
print(s1.union(s2))

#3
s1 = {10,20}
s2 = {30}
print(s1.union(s2))

#4
s1 = {1,2}
s2 = {2,3}
print(s1.union(s2))

#5
s1 = {"red"}
s2 = {"blue"}
print(s1.union(s2))

#6
s1 = {5,6}
s2 = {7,8}
print(s1.union(s2))

#7
s1 = {"python"}
s2 = {"java"}
print(s1.union(s2))

#8
s1 = {100}
s2 = {200}
print(s1.union(s2))

#9
s1 = {"dog"}
s2 = {"cat"}
print(s1.union(s2))

#10
s1 = {9}
s2 = {8}
print(s1.union(s2))

# FrozenSet
#1
s = frozenset([1,2,3])
print(s)

#2
s = frozenset(["a","b","c"])
print(s)

#3
s = frozenset([10,20])
print(s)

#4
s = frozenset(["red","blue"])
print(s)

#5
s = frozenset([100,200])
print(s)
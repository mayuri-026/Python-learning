# Access Tuple exaples 
#1
t = (10, 20, 30)
print(t[0])

#2
t = ("apple", "banana", "cherry")
print(t[1])

#3
t = (5, 6, 7, 8)
print(t[-1])

#4
t = (1,2,3,4,5)
print(t[2])

#5
t = ("a","b","c","d")
print(t[-2])

#6
t = (100,200,300,400)
print(t[3])

#7
t = ("red","blue","green")
print(t[0])

#8
t = (11,22,33,44)
print(t[-3])

#9
t = ("python","java","c++")
print(t[2])

#10
t = (9,8,7,6)
print(t[1])

#Update Tuples – 10 Examples

#(Tuple immutable असतो त्यामुळे list मध्ये convert करून update करतो)
#1
t = (1,2,3)
l = list(t)
l[0] = 10
t = tuple(l)
print(t)

#2
t = ("a","b","c")
l = list(t)
l[1] = "z"
t = tuple(l)
print(t)

#3
t = (5,6,7)
l = list(t)
l.append(8)
t = tuple(l)
print(t)

#4
t = (10,20)
l = list(t)
l.insert(1,15)
t = tuple(l)
print(t)

#5
t = ("apple","banana")
l = list(t)
l.append("cherry")
t = tuple(l)
print(t)

#6
t = (1,2,3)
t = t + (4,)
print(t)

#7
t = (5,6)
t = t + (7,8)
print(t)

#8
t = ("x","y")
l = list(t)
l.remove("x")
t = tuple(l)
print(t)

#9
t = (11,22,33)
t = t + (44,)
print(t)

#10
t = ("red","blue")
t = t + ("green",)
print(t)

# Unpack Tuples
#1
t = (10,20,30)
a,b,c = t
print(a,b,c)

#2
t = ("apple","banana")
x,y = t
print(x)

#3
t = (1,2,3)
a,*b = t
print(a,b)

#4
t = (5,6,7,8)
a,b,*c = t
print(c)

#5
t = (9,10,11)
a,b,c = t
print(b)

#6
t = ("red","green","blue")
x,y,z = t
print(z)

#7
t = (1,2,3,4)
a,*b,c = t
print(b)

#8
t = (10,20)
a,b = t
print(a+b)

#9
t = ("python","java","c++")
a,b,c = t
print(a)

#10
t = (100,200,300)
x,*y = t
print(y)

# Loop Tuples
#1
t = (1,2,3)
for i in t:
    print(i)

#2
t = ("a","b","c")
for i in t:
    print(i)

#3
t = (10,20,30)
for i in t:
    print(i*2)

#4
t = (5,6,7)
for i in t:
    print(i+1)

#5
t = ("red","blue")
for color in t:
    print(color)

#6
t = (1,2,3,4)
for i in range(len(t)):
    print(t[i])

#7
t = ("python","java")
for lang in t:
    print(lang.upper())

#8
t = (9,8,7)
for i in t:
    print(i)

#9
t = ("apple","banana")
for fruit in t:
    print(fruit)

#10
t = (100,200)
for i in t:
    print(i/10)

# Join Tuples
#1
t1 = (1,2)
t2 = (3,4)
print(t1 + t2)

#2
t1 = ("a","b")
t2 = ("c","d")
print(t1 + t2)

#3
t1 = (10,20)
t2 = (30,)
print(t1 + t2)

#4
t1 = (1,2)
print(t1 * 3)

#5
t1 = ("python",)
print(t1 * 2)

#6
t1 = (5,6)
t2 = (7,8)
t3 = t1 + t2
print(t3)

#7
t1 = ("red","blue")
t2 = ("green",)
print(t1 + t2)

#8
t1 = (1,)
print(t1 * 5)

#9
t1 = ("a","b")
print(t1 * 2)

#10
t1 = (10,)
print(t1 * 4)

# Tuple Methods
#1
t = (1,2,3,2)
print(t.count(2))

#2
t = ("a","b","a")
print(t.count("a"))

#3
t = (10,20,30)
print(t.index(20))

#4
t = ("apple","banana","cherry")
print(t.index("banana"))

#5
t = (5,6,7,6)
print(t.count(6))

#6
t = ("x","y","z")
print(t.index("z"))

#7
t = (1,1,1)
print(t.count(1))

#8
t = ("red","blue","green")
print(t.index("red"))

#9
t = (2,4,6,8)
print(t.index(6))

#10
t = ("python","java","python")
print(t.count("python"))
# Access Item 
#1
d = {"name":"Mayuri","age":22}
print(d["name"])

#2
d = {"city":"Pune","country":"India"}
print(d.get("city"))

#3
d = {"a":1,"b":2}
print(d["b"])

#4
d = {"x":10,"y":20}
print(d.get("x"))

#5
d = {"fruit":"apple","color":"red"}
print(d["fruit"])

#6
d = {"brand":"Dell","ram":"16GB"}
print(d.get("ram"))

#7
d = {"name":"Rahul","age":25}
print(d["age"])

#8
d = {"language":"Python","type":"Programming"}
print(d.get("language"))

#9
d = {"car":"BMW","year":2023}
print(d["car"])

#10
d = {"course":"DevOps","duration":"6 months"}
print(d.get("duration"))

# Change Items
#1
d = {"name":"Mayuri","age":22}
d["age"] = 23
print(d)

#2
d = {"city":"Pune"}
d["city"] = "Mumbai"
print(d)

#3
d = {"a":10}
d["a"] = 20
print(d)

#4
d = {"fruit":"apple"}
d["fruit"] = "mango"
print(d)

#5
d = {"color":"red"}
d["color"] = "blue"
print(d)

#6
d = {"brand":"HP"}
d["brand"] = "Dell"
print(d)

#7
d = {"name":"Rahul"}
d["name"] = "Amit"
print(d)

#8
d = {"course":"Python"}
d["course"] = "DevOps"
print(d)

#9
d = {"car":"BMW"}
d["car"] = "Audi"
print(d)

#10
d = {"city":"Delhi"}
d["city"] = "Pune"
print(d)

# Add Items
#1
d = {"name":"Mayuri"}
d["age"] = 22
print(d)

#2
d = {"city":"Pune"}
d["country"] = "India"
print(d)

#3
d = {"a":1}
d["b"] = 2
print(d)

#4
d = {"fruit":"apple"}
d["color"] = "red"
print(d)

#5
d = {"brand":"Dell"}
d["ram"] = "16GB"
print(d)

#6
d = {"name":"Rahul"}
d["city"] = "Mumbai"
print(d)

#7
d = {"course":"Python"}
d["duration"] = "3 months"
print(d)

#8
d = {"car":"BMW"}
d["year"] = 2023
print(d)

#9
d = {"book":"Python"}
d["price"] = 500
print(d)

#10
d = {"company":"Google"}
d["location"] = "USA"
print(d)

# Remove Items
#1
d = {"name":"Mayuri","age":22}
d.pop("age")
print(d)

#2
d = {"city":"Pune","country":"India"}
del d["city"]
print(d)

#3
d = {"a":1,"b":2}
d.pop("a")
print(d)

#4
d = {"fruit":"apple","color":"red"}
del d["color"]
print(d)

#5
d = {"brand":"Dell","ram":"16GB"}
d.pop("ram")
print(d)

#6
d = {"name":"Rahul","age":25}
del d["age"]
print(d)

#7
d = {"course":"Python","duration":"3 months"}
d.pop("course")
print(d)

#8
d = {"car":"BMW","year":2023}
del d["year"]
print(d)

#9
d = {"book":"Python","price":500}
d.pop("price")
print(d)

#10
d = {"company":"Google","location":"USA"}
del d["location"]
print(d)

# Loop Dictionaries
#1
d = {"name":"Mayuri","age":22}
for x in d:
    print(x)

#2
for x in d:
    print(d[x])

#3
d = {"a":1,"b":2}
for key,value in d.items():
    print(key,value)

#4
d = {"fruit":"apple","color":"red"}
for k in d:
    print(k)

#5
d = {"x":10,"y":20}
for v in d.values():
    print(v)

#6
d = {"city":"Pune","country":"India"}
for k,v in d.items():
    print(k,v)

#7
d = {"brand":"Dell","ram":"16GB"}
for x in d:
    print(x,d[x])

#8
d = {"name":"Rahul","age":25}
for v in d.values():
    print(v)

#9
d = {"car":"BMW","year":2023}
for k in d.keys():
    print(k)

#10
d = {"course":"Python","duration":"3 months"}
for k,v in d.items():
    print(k,v)


    # Copy Dictionaries
    #1
d1 = {"name":"Mayuri"}
d2 = d1.copy()
print(d2)

#2
d1 = {"city":"Pune"}
d2 = dict(d1)
print(d2)

#3
d1 = {"a":1}
d2 = d1.copy()
print(d2)

#4
d1 = {"fruit":"apple"}
d2 = d1.copy()
print(d2)

#5
d1 = {"brand":"Dell"}
d2 = dict(d1)
print(d2)

#6
d1 = {"name":"Rahul"}
d2 = d1.copy()
print(d2)

#7
d1 = {"course":"Python"}
d2 = dict(d1)
print(d2)

#8
d1 = {"car":"BMW"}
d2 = d1.copy()
print(d2)

#9
d1 = {"book":"Python"}
d2 = dict(d1)
print(d2)

#10
d1 = {"company":"Google"}
d2 = d1.copy()
print(d2)

# Nested Dictionaries
#1
d = {
"student1":{"name":"Mayuri","age":22},
"student2":{"name":"Rahul","age":23}
}
print(d)

#2
d = {"emp1":{"name":"Amit","salary":50000}}
print(d)

#3
d = {"car1":{"brand":"BMW","year":2023}}
print(d)

#4
d = {"book1":{"title":"Python","price":500}}
print(d)

#5
d = {"city1":{"name":"Pune","state":"MH"}}
print(d)

#6
d = {"course1":{"name":"DevOps","duration":"6 months"}}
print(d)

#7
d = {"student":{"name":"Neha","age":20}}
print(d)

#8
d = {"company":{"name":"Google","country":"USA"}}
print(d)

#9
d = {"phone":{"brand":"Apple","model":"iPhone"}}
print(d)

#10
d = {"laptop":{"brand":"Dell","ram":"16GB"}}
print(d)
print("STUDENT MANAGEMENT SYSTEM")

name = input("Enter student name: ")
marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))

total = marks1 + marks2 + marks3
average = total / 3

print("\n----- RESULT -----")
print("Name:", name)
print("Total:", total)
print("Average:", average)

if average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "Fail"

print("Grade:", grade)
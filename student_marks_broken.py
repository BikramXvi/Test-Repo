# Program to calculate total, average and grade

name = input("Enter student name: ")

marks1 = input("Enter marks for subject 1: ")
marks2 = input("Enter marks for subject 2: ")
marks3 = input("Enter marks for subject 3: ")

total = marks1 + marks2 + marks3

average = total / 3

print("Total marks:", total)
print("Average:", average)

if average >= 80:
    print("Grade: A")
elif average >= 60
    print("Grade: B")
elif average >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")

print("Thank you", name)

# Store numbers and find sum and largest

numbers = []

for i in range(5):
    num = input("Enter number: ")
    numbers.append(num)

sum = 0

for n in numbers:
    sum = sum + n

print("Sum:", sum)

largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print("Largest number:", largest)

print("All numbers:", numbers)
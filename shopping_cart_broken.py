# Simple shopping cart bill generator

total = 0

for i in range(3):
    item = input("Enter item name: ")
    price = input("Enter price: ")

    total = total + price

print("Total amount:", total)

discount = 0

if total > 1000:
    discount = total * 10 / 100

final_amount = total - discount

print("Discount:", discount)
print("Final amount:", final_amount)

if final_amount > 500:
print("You get free delivery")
else:
    print("Delivery charge applied")
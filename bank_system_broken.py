# Simple bank system

balance = 1000

print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")

choice = input("Enter choice: ")

if choice == 1:
    amount = input("Enter amount: ")
    balance = balance + amount
    print("New balance:", balance)

elif choice == 2:
    amount = input("Enter amount: ")

    if amount > balance:
        print("Insufficient balance")
    else:
        balance = balance - amount
        print("Remaining balance:", balance)

elif choice == 3:
    print("Balance is:", balance)

else:
    print("Invalid choice")

print("Thank you for using bank system")
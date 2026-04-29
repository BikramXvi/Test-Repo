# Simple login system

correct_username = "admin"
correct_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username = correct_username and password == correct_password:
    print("Login successful")
else:
    print("Invalid credentials")

attempts = 1

while attempts <= 3:
    if username == correct_username and password == correct_password:
        break
    else:
        print("Try again")
        username = input("Enter username: ")
        password = input("Enter password: ")
        attempts = attempts + 1

if attempts > 3:
    print("Account locked")
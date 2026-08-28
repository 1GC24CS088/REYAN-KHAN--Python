# Banking Program
balance = 1000

print("1. Show Balance")
print("2. Deposit")
print("3. Withdraw")

choice = input("Enter choice: ")

if choice == "1":
    print("Balance =", balance)

elif choice == "2":
    amount = int(input("Deposit amount: "))
    balance = balance + amount
    print("Balance =", balance)

elif choice == "3":
    amount = int(input("Withdraw amount: "))
    balance = balance - amount
    print("Balance =", balance)

else:
    print("Wrong choice")
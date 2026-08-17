
length = float(input("Enter the length:"))
width = float(input("Enter the width:"))
area = length * width

print(f"The Area is: {area}cm2")
print()

item = input("What item would you like to buy?:")
price = float(input("What is the price?:"))
quantity = int(input("How many items would you like?:"))
total = price * quantity

print(f"You have bought {quantity} * {item}/s")
print(f"Your total is:{total}")
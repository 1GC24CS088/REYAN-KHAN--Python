a = 20
b = 6

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

print()

import math
radius = float(input("Enter the radius of a circle:"))
circumference = 2 * math.pi * radius

print(f"The circumference of the circle is: {round(circumference, 2)}cm")

print()

import math
radius = float(input("Enter the radius of a circle:"))
area = math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(area)}cm^2")

print()

import math
x = float(input("Enter side x:"))
y = float(input("Enter side y:"))

z = math.sqrt(pow(x, 2) + pow(y, 2))
print(f"side z = {z}")
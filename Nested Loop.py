# Program to print a rectangle using stars

rows = 4
columns = 6

for i in range(rows):
    for j in range(columns):
        print("*", end=" ")
    print()

print()

for i in range(1, 6):
    for j in range(1, 6):
        print(i, end=" ")
    print()

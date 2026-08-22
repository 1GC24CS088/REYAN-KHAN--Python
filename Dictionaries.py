# Creating a dictionary
student = {
    "name": "Reyan",
    "age": 20,
    "course": "Computer Science"
}

# Adding a new key-value pair
student["grade"] = "A"

# Displaying all items
print("Student Details:")
for key, value in student.items():
    print(key, ":", value)

print()

print("Keys:", list(student.keys()))
print("Values:", list(student.values()))

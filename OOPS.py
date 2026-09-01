# Python Object Orienited Program

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


e1 = Employee("John", 25000)
e2 = Employee("Rahim", 30000)
e3 = Employee("Amit", 20000)
e4 = Employee("Aman", 35000)

e1.display()
e2.display()
e3.display()
e4.display()



# Variable scope
name = "Reyan Khan"

# Global variable
def outer():
    age = 19

 # Enclosed variable
    def inner():
        marks = 90
        # Local variable
        print("Local:", marks)
        print("Enclosed:", age)
        print("Global:", name)
        print("Built-in:", len("Hello World"))

    inner()

outer()
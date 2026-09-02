# Static Method
class Mobile:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    # Instance method
    def display(self):
        print("Mobile Brand:", self.brand)
        print("Price:", self.price)

    # Static method
    @staticmethod
    def operating_system():
        print("Operating System: Android")


m1 = Mobile("Samsung", 50000)
m2 = Mobile("Oppo", 30000)
m3 = Mobile("Vivo", 28000)
m4 = Mobile("Oneplus", 25000)

m1.display()
m2.display()
m3.display()
m4.display()
Mobile.operating_system()
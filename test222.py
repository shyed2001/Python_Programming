

## Classes and Objects
## Classes and Objects
# Define a class

class Employ:
    pass




empt1 = Employ()
empt2 = Employ()

print(empt2)
print(empt2)


empt1.name = "TEst"
empt1.lastname = "halt"
empt1.age = 45
empt1.pay = 70000
empt1.email = "TEst.halt@company"
empt2.name = "test"
empt2.lastname = "stop"
empt2.age = 45
empt2.pay = 70000
empt2.email = "test.stop@company"

print(empt2.name)
print(empt2.age)


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company'

    def fullname(self):
        print("From Method Full name is", f"{self.first} {self.last}")
        print("From Method Full name format ",'{} {}'.format(self.first,self.last))

emp1 = Employee('Name', "lastname", 70000)
emp2 = Employee('name', "last2name", 77000)

emp1.fullname()
emp2.fullname()

print(emp1.fullname())
print(emp2.fullname())


print("Full name is", f"{emp1.first} {emp1.last}")

print("Full name is",'{} {}'.format(emp2.first,emp2.last))

print(emp1.email , emp1.pay)

print(emp2.email ,  emp2.pay)

class Phone:
    def __init__(self, brand, price, version):  # this is a constructer # Properties
        self.brand = brand # instant variable or attributes
        self.price = price
        self.version = version
        #does not print anything
    def call (self, phone_number): # Behaviour # functionalities # functions # methods
        print(f"My phone is {self.brand} , the price is {self.price} and version is {self.version} calling {phone_number}")
        #it prints


iphone = Phone("Apple", 100000, 11)  # Objects # collections of properties and functions # instences
android = Phone("Samsung", 50000, 25) # Objects # instences have unique data

print(iphone)
print(android)

print(iphone.brand) #properties
print(iphone.price) #properties
print(iphone.version) #properties
iphone.call(999) # Behaviour
print(android.brand) #properties
print(android.price) #properties
print(android.version) #properties
android.call(123) # Behaviour


# Print Objects  # Print Objects

# Print Objects by overwriting
class Phone:
    def __init__(self, brand, price, version):  # this is a constructer
        self.brand = brand
        self.price = price
        self.version = version
        #does not print anything
    def call (self, phone_number): # Behaviour
        print(f"My phone is {self.brand} , the price is {self.price} and version is {self.version} calling {phone_number}")
        #it prints


    # press Ctrl+o to bring up the overwrite option bar
    def __str__(self) -> str:   # -> str return a string
        return f"My phone is {self.brand} , the price is {self.price} and version is {self.version}"


iphone = Phone("Apple", 100000, 11)  # Objects
android = Phone("Samsung", 50000, 25) # Objects

print(iphone)
print(android)

print(iphone.brand) #properties
print(iphone.price) #properties
print(iphone.version) #properties
iphone.call(999) # Behaviour
print(android.brand) #properties
print(android.price) #properties
print(android.version) #properties
android.call(123) # Behaviour



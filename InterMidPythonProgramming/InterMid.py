'''
Top 14 MOST famous Python libraries & frameworks

Libraries covered:

1. requests  (http://docs.python-requests.org/en/ma...)
2. tqdm (https://github.com/tqdm/tqdm)
3. pillow (http://pillow.readthedocs.io/)
4. scrapy (https://scrapy.org/)
5. numpy (http://www.numpy.org/)
6. pandas (https://pandas.pydata.org/)
7. scapy (https://scapy.net/)
8. matplotlib (https://matplotlib.org/)
9. kivy (https://kivy.org/)
10. nltk (http://www.nltk.org/)
11. keras  (https://keras.io/)
12. SQLAlchemy (http://www.sqlalchemy.org/)
13. Django (https://www.djangoproject.com/)
14. Twisted (https://twistedmatrix.com/)

Extra/Bonus libraries:

1. flask (http://flask.pocoo.org/)
2. scipy (https://www.scipy.org/)
3. pytorch (https://pytorch.org/)
4. DjangoCMS (https://www.django-cms.org/en/)
5. click (http://click.pocoo.org/5/)
6. astropy (http://www.astropy.org/)
7. scikit-learn (http://scikit-learn.org/)
8. opencv (https://docs.opencv.org/3.0-beta/doc/...)
9. PyQt (https://riverbankcomputing.com/softwa...)
10. tensorflow (https://www.tensorflow.org/)
11. wagtail (https://wagtail.io/)

'''

# Python OOP

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

    num_ofEmployees = 0
    bonous_amount = 1.04   # class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company'
        Employee.num_ofEmployees+=1
        # num_ofEmployees increases at every occurence of class object instence creation
    def fullname(self):
        print("From Method Full name is", f"{self.first} {self.last}")
        print("From Method Full name format ",'{} {}'.format(self.first,self.last))


    def apply_raise(self):   #method
        self.pay = int(self.pay * 1.4)

    def Bonous_amount(self): #method
        self.pay = int((self.pay * self.bonous_amount))

    def incentives(self): #method
        self.pay = int(self.pay * 2 * Employee.bonous_amount)

    @classmethod # this is classmethod decorator


print(Employee.num_ofEmployees)
emp1 = Employee('Name', "lastname", 70000)
emp2 = Employee('name', "last2name", 77000)
print(Employee.num_ofEmployees)
print(emp1.__dict__ ,  emp2.__dict__)

print(Employee.__dict__)

print(emp1.pay)
print(emp2.pay)
emp1.apply_raise()
emp2.apply_raise()
print("Extended pay" , emp1.pay)
print("Extended pay" , emp2.pay)
emp1.Bonous_amount()
emp2.Bonous_amount()
print("Extra Extended pay" , emp1.pay)

print("Extra Extended pay" , emp2.pay)

emp1.incentives()
emp2.incentives()
print("Extra Incentive Extended pay" , emp1.pay)
print("Extra Incentive Extended pay" , emp2.pay)

Employee.bonous_amount = 1.5  # class variable
print(emp1.__dict__ ,  emp2.__dict__)

print(Employee.__dict__)
print(emp1.pay)
print(emp2.pay)
emp1.apply_raise()
emp2.apply_raise()
print("Extended pay" , emp1.pay)
print("Extended pay" , emp2.pay)
emp1.Bonous_amount()
emp2.Bonous_amount()
print("Extra Extended pay" , emp1.pay)

print("Extra Extended pay" , emp2.pay)

emp1.incentives()
emp2.incentives()
print("Extra Incentive Extended pay" , emp1.pay)
print("Extra Incentive Extended pay" , emp2.pay)

emp1.bonous_amount = 2 # Method Variable
print(emp1.__dict__ ,  emp2.__dict__)

print(Employee.__dict__)
print(emp1.pay)
print(emp2.pay)
emp1.apply_raise()
emp2.apply_raise()
print("Extended pay" , emp1.pay)
print("Extended pay" , emp2.pay)
emp1.Bonous_amount()
emp2.Bonous_amount()
print("Extra Extended pay" , emp1.pay)

print("Extra Extended pay" , emp2.pay)

emp1.incentives()
emp2.incentives()
print("Extra Incentive Extended pay" , emp1.pay)
print("Extra Incentive Extended pay" , emp2.pay)


emp1.fullname()
print("#")
emp2.fullname()
print("#")
print("#")
Employee.fullname(emp1)
print("#")
Employee.fullname(emp2)
print(Employee.fullname(emp2))
print("#")
print("#")
print(emp1.fullname())
print("#")
print(emp2.fullname())
print("#")
print("#")

print("Full name is", f"{emp1.first} {emp1.last}")

print("Full name is",'{} {}'.format(emp2.first,emp2.last))

print(emp1.email , emp1.pay)

print(emp2.email ,  emp2.pay)

print(emp1.__dict__ ,  emp2.__dict__)

print(Employee.__dict__)

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





# Optional Parameters

def func(x):
    return x**2

call = func(5)
print(call)

def func(x = 1): # x = 1 defauly or optional parameter
    return x**2

call = func(3)
print(call)

call = func() # gives no error without an argument
print(call)

def func2(name, freq = 1):
    print(name*freq)
call = func2('tim ', 3)
func2('tim ')
func2(5)

def func2(name, add =5, freq = 1):
    print(name*(freq+add))

call = func2('tim ', 3)
func2('tim ')
func2(5)
func2(5,0,1)
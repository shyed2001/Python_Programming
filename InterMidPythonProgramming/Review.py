##!/usr/bin/env python3
# # https://stackoverflow.com/questions/7670303/purpose-of-usr-bin-python3-shebang

# https://en.wikipedia.org/wiki/Shebang_(Unix)
# # Python Reference  https://www.w3schools.com/python/python_reference.asp
# #-----------------------------------------------------------------------------
# Name:        Python Intro
# Purpose:     Started in Py
#
# Author:      User/Shyed
#
# Created:     30/03/2019
# Copyright:   (c) User 2019
# Licence:     <User/Shyed/your licence>
#------------------------------------------------------------------------------
print("The Start The Start The Start The Start ?\n")
# \n introduces a new line
print("The Start The Start The Start The Start ?")

print("5+8")

print(5+8)
age = 17
if (age<18):
  print("5+8")
  
# This is a comment lines

'''
This is a multi line comment
'''
import cv2 
import math

print(math.gcd(3,6))
print(math.gcd(3,6,9,15))

a = 341
b = "Shyed"
Shyed = 55
c = Shyed
d = 45.90

print(a+3)
print(a+d)
print(a+c)
print(a*3)
print(a-d)
print(a/c)
print(a//3)
print(a%d)
print("a**c = ", a**c)
print("a^c = ", a^c)
print(5^7)

A = type(a)
B = type(b)
C = type(c)
D = type(d)

print(A)
print(B)
print(C)
print(D)

e = "31"
f = "44.0"
F = type(f)
print(F)
e = int(e)
print(e)
f = int(44.0)
g = int(99.5)
print(e+2)
print(f,g)

name = "Shyed, Shahriar "
var = name.lower()
print (var)
var=name.upper()
print (var)
var = name.replace("ye","t")
print (var)
var = name.replace(",",'\n')
print (var)

stri = "This is a "
name1 ="Harry" 
name2 = "Rohan"
stri2 = "This is not a "
print (stri2 + name)
temp = "This is a {} and he is a good boy named {}".format(name1, name2)
print (temp)
temp = "This is a {1} and he is a good boy named {0}, friend to {2}".format(name1, name2, name)
print (temp)
temp=  f"this is a {name1} and he is a good boy {name2}"

print (temp)
print(f"this is a {name1} and he is a good boy {name2}")

'''
Python Collections:
1. List
2. Tuple
3. Set
4. Dictionary
'''
# Lists
'''
Lists :
A List in Python represents a list of comma-separated values of any data type between square brackets.
'''
lst = [61,2,3,4,6,41]
var = type(lst)
print (var)

lst[2] = 45
print (var)
var = lst[2]
print (var)

var = lst
lst.append (100)
print (var)

lst.insert(1, 100)
print (var)

lst.remove (61)
print (var)

lst.pop()
print (var)

lst.clear()
print(lst)
print (var)

lst = [61,2,3,4,6,41]
var = lst
print (var)

var1 = len(lst)
print (var1)

var2 = lst[1:4]
print (var2)


del lst[3]
var = lst
print (var)

# del lst
# The previous line deletes the list lst
a = ("Shyed", "Shahriar", "Housaini")
## Tuples 
# Tuples are unchangeable
'''
Tuples:
These are those lists which cannot be changed i.e., are not modifiable. Tuples are represented as list of comma-separated values of any date type within parentheses.
'''

## Set Sets :
'''
Sets in python are a data type equivalent to sets in mathematics. It may consist various elements and the order is undefined.

Sets elements are enclosed in {} Curly Braces.

In sets repeated elements does not get printed.
'''
print("\t\tSets\n")

set1 = {1,2,3,4,5,1,2,3}
print(set1)
print(type(set1))
set1.add(99)
print(set1)

my_fav = {"red", "green", "blue", "black", "purple"}

her_fav = {"blue","orange", "purple", "green"}

all_favsUnions = my_fav | her_fav
# union
print(all_favsUnions)
all_favsUnions2 =my_fav.union(her_fav) 
print(all_favsUnions2)
Intersection_fav = my_fav & her_fav
print(Intersection_fav)
Intersection_fav2 = my_fav.intersection(her_fav)
print(Intersection_fav2)

#Difference
all_favsdiff = my_fav-her_fav
all_favsdiff2 = her_fav-my_fav
print(all_favsdiff)
print(all_favsdiff2)

#symmetric Difference
all_favssymdiff = my_fav^her_fav
all_favssymdiff2 = her_fav^my_fav
print(all_favssymdiff)
print(all_favssymdiff2)

'''
Dictionary :
Dictionary data type is another feature in Python's hat. The dictionary is an unordered set of comma-separated key: value pairs, within {},with the requirement that within a dictionary, no two keys can be the same (i.e., there are unique keys within a dictionary).

print("\t\tDictionary\n")
'''

print("\t\tDictionary\n")

dictionary1 = {
    "Play" : "Doing some activity",
    "Food" : "Something eatable",
    "Python" : "Language",
}

print(dictionary1)
print(len(dictionary1))


print("\t Input statement \n")

a = int(input("Enter any number: "))
name = input("Enter any name: ")

print(type(a))
print(a)
print(type(name))
print(name)

print("\t Conditional Statements \n")

age2 = int(input("Enter your age: "))

if (age2>=18):
    print("You are eligible to vote")

else:
    print("You are not eligible to vote")
    

print("\t Conditional Statements \n")

x = int(input("Enter any number: "))

if (x>50):
    print("Number is greater than 50")
elif (x>25):
    print("No. entered is b/w 25-50")
elif (x>0):
    print("Number entered is between 0-25")
else:
    print("Enter valid number")


print("\t Loops \n")

num = 5
for a in range(1, 11 ):
    print(num, 'x ', a, '=', num* a)

x = [7, 8, 3]

for index, item in enumerate (x):
    print (index,item)

print("\t Loops \n")

x = 1
while(x<=100):      #while loop
    print(x)
    x = x+1


'''
def function_name () :

         statement 1,

         statement 2,

         ….
'''
print("\t Functions \n")

def demo():     #Derining a runction
    print("Hlo Guys")
    print("It's my First Function")
    print(" : )")

demo()      # Calling a runction
print("\t Functions \n")

def add(a,b):        #Derining Function
    c = a+b
    return c

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

z = add(x,y)        #Calling Function
print("The Sum is", z)

  
class Employee:
    def __init__(self, gname, gsalary):
        self.name = gname
        self.salary = gsalary

harry = Employee("harry", 34)
print(harry.name)
print(harry.salary)
     
    
'''

# DIFFERENCE BETWEEN
# LIST - square braces
# TUPLE - rounded braces
# SET - The set keyword
# DICTIONARY - curly braces: made up of key-value pairs

list1 = ["Computer", "Printer", "TV", "Camera", 89, 30.8]

tuple1 = ("Computer", "Printer", "TV", "Camera", 89, 30.8)

set1 = set(["Computer", "Printer", "TV", "Camera", 89, 30.8])
dict1 = {
     1: "Monday",
     2: "Tuesday",
     3: "Wednesday"
}

1. Python List

A list in python is a collection of various items  which may be either of the same or of different data types.  The items in a list are separated by commas and enclosed in square braces. Listing 1.0 shows how to create a list in python

assets = ["Computer", "Printer", "TV", "Camera"]

scores = [56, 45.9, 89.5, 70, 32.9, 67.4]

letters = ['k', 'i', 'n', 'd', 's', 'o', 'n']

things = ["chair", 45, 'A', "house"]
Listing 1.0: Examples of Lists in Python

 

2. Python Tuple

A tuple in python is also a collection of items just like list. Take note of the two key difference:

A tuple is immutable (you can’t change the elements once created)
A tuple is created with rounded braces
Listing 1.1 show example of Tuple

assets = ("Computer", "Printer", "TV", "Camera")

scores = (56, 45.9, 89.5, 70, 32.9, 67.4)

letters = ('k', 'i', 'n', 'd', 's', 'o', 'n')

things = ("chair", 45, 'A', "house")
Listing 1.1: Example of Tuple in Python

 

3. Python Dictionary

A dictionary in python is a collections of key-value pairs of item. For each entry, there are two items: a key and a value. Note the following about Python dictionaries

keys in a dictionary must be unique (no two same keys)
keys are immutable
keys and values can be of any data types
the keys() function returns list of keys in a dictionary
the values() function returns list of values in dictionary
Example of dictionaries are given in Listing 1.3.

months = {
    "Jan": "January",
    "Feb": "Febraury",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September"
}

weekdays = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}
Listing 1.2: Examples of Dictionaries in Python

 

4. Python Set

A set in python is a collection of items just like Lists and Tuples.  Note the following about sets:

A set is created using the set keyword
A set cannot be an element of a set (but a list can be an element of a list)
Also note: As pointed out by Luka Jeličić Lux, Sets cannot have same element multiple times. Example: When you have set([1,2,2,2,3,3,4,4,5,5]) and print it you get [1,2,3,4,5] as output.

Examples of sets is given in Listing 1.3

assets = set(["Computer", "Printer", "TV", "Camera"])

scores = set([56, 45.9, 89.5, 70, 32.9, 67.4])

letters = set(['k', 'i', 'n', 'd', 's', 'o', 'n'])

things = set(["chair", 45, 'A', "house"])
Listing 1.3: Example of Set in Python



'''

'''
DIFFERENCE BETWEEN
LIST - square braces
TUPLE - rounded braces
SET - The set keyword
DICTIONARY - curly braces: made up of key-value pairs


'''

list1 = ["Computer", "Printer", "TV", "Camera", 89, 30.8]
list1 [0] = "PC"
print(list1)
tuple1 = ("Computer", "Printer", "TV",
"Camera", 89, 30.8)
print (tuple1)

set1 = set( ["Computer", "Printer", "TV",
"Camera", 89, 30.8])
print (set1)

set1 = {"Computer", "Printer", "TV",
"Camera", 89, 30.8}
print (set1)

dict1 = {
1: "Monday",
2 :"Tuesday",
3: "Wednesday"
}
print (dict1)
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


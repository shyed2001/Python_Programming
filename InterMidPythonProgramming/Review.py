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

lst = [61,2,3,4,6,41]
var = type(lst)

print (var)
lst[2] = 45
var = lst[2]
print (var)
lst.append (100)
print (var)
lst.insert(1, 100)
print (var)
lst.remove (61)

print (var)
lst.pop()

print (var)
lst.lst[3]

print (var)
lst.lst

print (var)
lst.clear()
var = lst
var = len(lst)

print (var)

print (var)
var = lst[1:4]


print (var)

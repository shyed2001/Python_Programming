#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     29/03/2019
# Copyright:   (c) User 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------


print("""Tuples, tuples are like lists but their values/data
can not be changed, immutable, ROM, Read Only
, now lets assume, tup1=("Maths", 23 , 3.3) """)


print("""Tuples, tuples are like lists but their values/data can not be
 changed,
 now lets assume, tup1=("Maths", 23 , 3.3, 9/3)""")

tup1=("Maths", 23 , 3.3, 9/3)

print("""
print(tup1[2]) =
 """)
print(tup1[2])

print("print(tup1[0:4]) = ")
print(tup1[0:4])
print("print(tup1[0:5]) = " , (tup1[0:5]))
print("print(tup1[0:15]) = " , (tup1[0:15]))

print("""
coordinates=(4,5) --- this is a tupple, can not be changed
coordinates=[4,5] --- this is a list, items can be changed,
coordinates=[(4,5), (5,6), (6,7)] - this is a list of tupples
coordinates=[(4,5), (5,6), (6,7)]
coordinates.pop()
print(coordinates)""")
coordinates=[(4,5), (5,6), (6,7)]
coordinates.pop()
print(coordinates)


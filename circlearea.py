#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     12/03/2019
# Copyright:   (c) user 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
print("Area calculation program")
print('Area is A=πr^2 or A=πr*r or A=πr**2')

π=22/7
print(π)
r=3.3
print('value of r is 3 and π=22/7')
print('A is the area')
print('A is =', π*r**2)
#
print(" The user have to give input of the value of radious r")
#
#
π=22/7
print(π)

r=float(input('please input rhe value of radious r:  '))
print(r)
print('A is =' , str(π*r**2))
##
##
print("Do the previous calculation in one line")

print('''A or \n The area is
=''', π*float(input('please input rhe value of radious r: '))**2)
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

print('''
def cube1(num):
    print(num*num*num)
cube1(3)
''')
def cube1(num):
    print(num*num*num)
cube1(3)
print('''
def cube2(num):
    return(num*num*num)
print(cube2(2))
''')
def cube2(num):
    return(num*num*num)
print(cube2(2))
print('''
def cube3(num):
    return num*num*num
print(cube3(2))
''')
def cube3(num):
    return num*num*num
print(cube3(2))
print('''
def cube4(num):
    return num*num*num
result=cube4(5)
print(result)
''')
def cube4(num):
    return num*num*num
result=cube4(5)
print(result)

# Created:     01/05/2019
# Copyright:   (c) User 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def absolute_value(x):
 if x < 0:
    return -x
 else:
  return x

print(absolute_value(-3))

def absolute_value(x):
 if x < 0:
    return -x
 return x

print(absolute_value(-7))

def find_first_2_letter_word(words):
 for word in words:
     if len(word) == 2:
        return word
 return " "


print(find_first_2_letter_word(["I", "like", "cheese"]))

print(find_first_2_letter_word(["This", "is", "a", "dead", "parrot"]))

#import math
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx*dx + dy*dy
    #result = dsquared**0.5
    result = pow(dsquared,0.5)
    return result
print(distance(1, 2, 4, 6))

import math

def distance(x1, y1, x2, y2):
 return math.sqrt( (x2-x1)**2 + (y2-y1)**2 )

print(distance(1, 2, 4, 6))
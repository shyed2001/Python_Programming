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

# Created:     01/05/2019
# Copyright:   (c) User 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def is_divisible(x, y):
 """ Test if x is exactly divisible by y """
 if x % y == 0:
   #return True
   print(True)
 else:
   #return False
   print(False)
print(is_divisible(4, 2))
print(is_divisible(5, 2))

def is_divisible(x, y):
 """ Test if x is exactly divisible by y """
 if x % y == 0:
   return "return ok2"
   print("print ok2")
 else:
   return "return not ok2"
   print("print not ok2")
print(is_divisible(4, 2))
print(is_divisible(5, 2))

def is_divisible(x, y):
   b= x % y == 0
   return b      # Test if x is exactly divisible by y
   if is_divisible(x, y) == True:   # excess lines
    return "return ok 3"       # excess lines dead code
    print("print ok 3")        ## excess lines dead code
   else:
    return "return not ok 3"   # # excess lines dead code
    print("print not ok 3")    # # excess lines dead code
print(is_divisible(4, 2))
print(is_divisible(5, 2))

def is_divisible(x, y):
   b= x % y == 0
   return b      # Test if x is exactly divisible by y

print(is_divisible(4, 2))
print(is_divisible(5, 2))

def is_divisible(x, y):
  return x % y == 0    # Test if x is exactly divisible by y

print(is_divisible(4, 2))
print(is_divisible(5, 2))

#++++++++++++++++++++++++============================================
def area_of_circle(xc, yc, xp, yp):
     radius = distance(xc, yc, xp, yp)
     a= (22/7)*(radius)**2
     return a

def distance(xc, yc, xp, yp):
 return math.sqrt( (xp-xc)**2 + (yp-yc)**2 )

print(area_of_circle(1, 2, 4, 6))

##########################################################

def area_of_circle(xc, yc, xp, yp):
     radius = math.sqrt( (xp-xc)**2 + (yp-yc)**2 )
     a= (22/7)*(radius)**2
     return a

#def distance(xc, yc, xp, yp):
 #return math.sqrt( (xp-xc)**2 + (yp-yc)**2 )

print(area_of_circle(1, 2, 4, 6))

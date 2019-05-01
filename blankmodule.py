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
   if is_divisible(x, y) == True:
    return "return ok 3"
    print("print ok 3")
   else:
    return "return not ok 3"
    print("print not ok 3")
print(is_divisible(4, 2))
print(is_divisible(5, 2))

def is_divisible(x, y):
   b= x % y == 0
   return b      # Test if x is exactly divisible by y

print(is_divisible(4, 2))
print(is_divisible(5, 2))

def is_divisible(x, y):
  return x % y == 0

print(is_divisible(4, 2))
print(is_divisible(5, 2))

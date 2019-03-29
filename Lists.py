#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      user
#
# Created:     28/03/2019
# Copyright:   (c) user 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

print("LISTS")
print("Working with LISTS")

print('''
lists=[], this is an epty list
''')
list=["kevin", 5, 7.9, True]
# list values are indexed

friend=["kevin", "KAren", "Jim", "Toddy", "Frog"]
#          0        1        2      3        4

print('''
list=["kevin", 5, 7.9, True]
# list values are indexed

friend=["kevin", "KAren", "Jim", "Toddy", "Frog"]
#          0        1        2      3        4

''')

print(''' print(friend[0])

=''')
print(friend[0])
print('''
print(friend[-1])
''')
print(friend[-1])
print('''
print(friend[-3])
''')

print(friend[-3])
print('''
print(friend[1:2])
''')

print(friend[1:2])
print('''
print(friend[1:3])
''')

print(friend[1:3])
print('''
print(friend[1:4])
=''')
print(friend[1:4])

print('''
update or modify list values
friend[0]= "000"
print(friend[0])
=''')
friend[0]= "000"
print(friend[0])

print(''' update or modify list values
friend[0:1]= ["000", "ttt"]
print(friend[0:2])
=''')
friend[0:1]= ["000", "ttt"]
print(friend[0:2])

print('''
List Functions
print('
List Functions
')
''')


print('''
Items=["car", "chair", "table", "mat"]
num=[8.8, 7.7,9.9,5.5,25,34,35,43,45,50,52,53,55,61,70,71,77,91,92,93,99,105,115,
122,125,133,151,155,160,170,171,177,181,192,205,250,322,331]
numbers=[4,8,15,16,23,42]
FRINDS=["kevin", "KAren", "Jim", "Toddy", "Frog", "Todd", "Jorge", "Lang"]
#          0        1        2      3        4       5      7        8
''')
Items=["car", "chair", "table", "mat"]
num=[8.8, 7.7,9.9,5.5,25,34,35,43,45,50,52,53,55,61,70,71,77,91,92,93,99,105,115,
122,125,133,151,155,160,170,171,177,181,192,205,250,322,331]
numbers=[4,8,15,16,23,42]
FRINDS=["kevin", "KAren", "Jim", "Toddy", "Frog", "Todd", "Jorge", "Lang"]
#          0        1        2      3        4       5      7        8

print('''
FRINDS.extend(numbers)
print(FRINDS)
=''')
FRINDS.extend(numbers)
print(FRINDS)

print('''
FRINDS.append(num)
print(FRINDS)
=''')
FRINDS.append(num)
print(FRINDS)

print('''
FRINDS.extend(Items)
FRINDS.extend("77777777777")
print(FRINDS)
=''')
FRINDS.extend(Items)
FRINDS.extend("77777777777")
print(FRINDS)

print('''
FRINDS.append(Items)
FRINDS.append("55555555555")
print(FRINDS)
=''')
FRINDS.append(Items)
FRINDS.append("55555555555")
print(FRINDS)

print('''
FRINDS.insert(1,"00000000000000")
# index       1, replace with
print(FRINDS)
=''')

FRINDS.insert(1,"00000000000000")
# index       1, replace with this
print(FRINDS)
print('''

=''')
print('''
FRINDS.insert(7,Items*3)
print(FRINDS)
=''')
FRINDS.insert(7,Items*3)
print(FRINDS)
print(''' remove one item
FRINDS.remove("00000000000000")
print(FRINDS)
=''')
FRINDS.remove("00000000000000" )
print(FRINDS)

print(''' clear or remove last element\item of the list
FRINDS.pop()
print(FRINDS)
=''')
FRINDS.pop()
print(FRINDS)

print(''' find element\item of the list
FRINDS.index('Toddy')
FRINDS.index("car")
print(FRINDS.index("car"))
=''')

print(''' count number of a value
print(FRINDS.count("car"))
print(FRINDS.count("7"))
=''')
print(FRINDS.index("car"))
print(FRINDS.index('Toddy'))

print(FRINDS.count("car"))
print(FRINDS.count("7"))



print(''' clear all items
FRINDS.clear()
print(FRINDS)
=''')
FRINDS.clear()
print(FRINDS)

FRINDS=["You","HE", "he", "WE", "we","We", "wE"]
math=[3, 33, 4.4, 9.0, 9, .1, 0.1, 0, 0.0, .0, .00, 00, 00.00, 00.000, 0000]
print(''' sort/arrange all items alphabetically in assending order
FRINDS=["You","HE", "he", "WE", "we","We", "wE"]
math=[3, 33, 4.4, 9.0, 9, .1, 0.1, 0, 0.0, .0, .00, 00, 00.00, 00.000, 0000]
FRINDS.sort()
math.sort()
print(FRINDS)
print(math)
=''')

FRINDS.sort()
math.sort()
print(FRINDS)
print(math)

print(""" reverse the list items
FRINDS.reverse()
math.reverse()
print(FRINDS)
print(math)
""")
FRINDS.reverse()
math.reverse()
print(FRINDS)
print(math)

print(""" copy the list items to another list
FRINDS3=math
FRINDS2=math.copy()
FRINDS3=math
print(FRINDS2)
print(FRINDS3)
""")
FRINDS3=math
FRINDS2=math.copy()
FRINDS3=math
print(FRINDS2)
print(FRINDS3)

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



#-------------------------------------------------------------------------------
# Name:        Print Book pages module1
# Purpose:     Get printed missing pages / numbers
#
# Author:      user/shyed
#
# Created:     27/03/2019
# Copyright:   (c) user 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

a=225 # start at 225
b=226 # start at 226
l=599 # stop at 599
list1=[] # initialize an empty list
for i in range(a,l+1,4): list1.append(i)
for j in range(b,l, 4): list1.append(j)
list1.sort()
print(list1)
print('''
a=225
b=226
l=599
list1=[]
for i in range(a,l+1,4): list1.append(i)
for j in range(b,l, 4): list1.append(j)
list1.sort()
print(list1)
''')
print(""" That code will result this list,
[225, 226, 229, 230, 233, 234, 237, 238, 241, 242, 245, 246,
 249, 250, 253, 254, 257, 258, 261, 262, 265, 266, 269, 270, 273, 274,
  277, 278, 281, 282, 285, 286, 289, 290, 293, 294, 297, 298, 301, 302,
   305, 306, 309, 310, 313, 314, 317, 318, 321, 322, 325, 326, 329,
   330, 333, 334, 337, 338, 341, 342, 345, 346, 349, 350, 353, 354,
   357, 358, 361, 362, 365, 366, 369, 370, 373, 374, 377, 378, 381,
382, 385, 386, 389, 390, 393, 394, 397, 398, 401, 402, 405, 406,
     409, 410, 413, 414, 417, 418, 421, 422, 425, 426, 429, 430, 433,
      434, 437, 438, 441, 442, 445, 446, 449, 450, 453, 454, 457, 458,
      461, 462, 465, 466, 469, 470, 473, 474, 477, 478, 481, 482, 485,
 486, 489, 490, 493, 494, 497, 498, 501, 502, 505, 506, 509, 510,
        513, 514, 517, 518, 521, 522, 525, 526, 529, 530, 533, 534,
         537, 538, 541, 542, 545, 546, 549, 550, 553, 554, 557, 558,
         561, 562, 565, 566, 569, 570, 573, 574, 577, 578, 581, 582,
585, 586, 589, 590, 593, 594, 597, 598]""")


#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     01/05/2019
# Copyright:   (c) User 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# Name:       ExerciseModule
# Purpose:    exercise
#
# Author:      Shyed Shahriar Housaini
#
# Created:     01/05/2019
# Copyright:   (c) User 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Created:     01/05/2019
# Copyright:   (c) User 2019
# Licence:     <your licence>
#d=="N" or d=="E" or d== "S" or d== "W"
#for d in d:

def day_name (d):
    if d == 0 : # or "n"
             print( "Friday")
    elif d== 1 : # or "e"
             print( "Saturday")
    elif d== "2" : # or "s"
             print( "Sunday")
    elif d== "3" : # or "w"
             print("Monday")
    elif d== "4" : # or "w"
             print("Tuesday")
    elif d== "5" : # or "w"
             print("Wednesday")
    elif d== "6" : # or "w"
             print("Thursday")
    else:
     # pass
     print("None")
    #break => creates error
    #return d #==> shows the entered value
    return " "  # when we don,t want the value to be returned

print(day_name (0))

print(day_name ("3"))

print(day_name (" "))

print(day_name ("9"))

print(day_name (7))

"""
    d={ 0:"Friday",
        1 :"Saturday",
        2 :"Sunday",
       "3" :"Monday",
       "4" :"Tuesday",
       "5" : "Wednesday",
        6 : "Thursday"  }

"""

def day_num (dn):
 d=["Friday--","Saturday--","Sunday--","Monday--","Tuesday--","Wednesday--","Thursday--" ]
 return (d[dn])

print(day_num (0))
print(day_num(6))

"""    if d == 0 : # or "n"
             print( "Friday")
    elif d== 1 : # or "e"
             print( "Saturday")
    elif d== "2" : # or "s"
             print( "Sunday")
    elif d== "3" : # or "w"
             print("Monday")
    elif d== "4" : # or "w"
             print("Tuesday")
    elif d== "5" : # or "w"
             print("Wednesday")
    elif d== "6" : # or "w"
             print("Thursday")
    else:
     # pass
     print("None")
    #break => creates error
    #return d #==> shows the entered value
    return " "  # when we don,t want the value to be returned
"""
print(day_name (0))

print(day_name ("3"))

print(day_name (" "))

print(day_name ("9"))

print(day_name (7))
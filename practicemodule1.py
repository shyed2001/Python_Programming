# Created:     01/05/2019
# Copyright:   (c) User 2019
# Licence:     <your licence>
#d=="N" or d=="E" or d== "S" or d== "W"
#for d in d:

def turn_clockwise(d):
    if d == "N" : # or "n"
             print( "E")
    elif d== "E" : # or "e"
             print( "S")
    elif d== "S" : # or "s"
             print( "W")
    elif d== "W" : # or "w"
             print("N")
    else:
     # pass
     print("None")
    #break => creates error
    #return d #==> shows the entered value
    return " "  # when we don,t want the value to be returned


print(turn_clockwise("s"))

print(turn_clockwise("N"))


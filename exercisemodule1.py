#-------------------------------------------------------------------------------
# Name:        Return Function
# Purpose:     Exercise
#
# Author:      Shyed Shahriar Housaini
#
# Created:     01/05/2019
# Copyright:   (c) User 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------


monthConv={
"jan": "January",
"feb": "February",
"mar": "March",
"apr": "April",
"may": "May",
"jun": "June",
"jul": "July",
"aug": "August",
"sep":"September",
"oct":"October",
"nov":"November",
"dec":"December"
}
print("""
Assigned key value pairs are -
monthConv={
"jan": "January",
"feb": "February",
"mar": "March",
"apr": "April",
"may": "May",
"jun": "June",
"jul": "July",
"aug": "August",
"sep":"September",
"oct":"October",
"nov":"November",
"dec":"December"
}
""")
print("""
print(monthConv["nov"])
print(monthConv.get("mar"))
print(monthConv.get("ma"," Not a valid key"))
""")
print(monthConv["nov"])
print(monthConv.get("mar"))
print(monthConv.get("mov"))
print(monthConv.get("ma"))
print(monthConv.get("ma"," Not a valid key"))

monthConv2={
1: "january",
2: "february",
3: "march",
4: "april",
5: "may",
6: "june"
}
print("""
monthConv2={
1: "january",
2: "february",
3: "march",
4: "april",
5: "may",
6: "june"
}
""")
print("""
print(monthConv2[6])
print(monthConv2.get(3))
print(monthConv2.get(7))
print(monthConv2.get(9," Not a valid key"))
""")
print(monthConv2[6])
print(monthConv2.get("january"))
print(monthConv2.get(3))
print(monthConv2.get(7))
print(monthConv2.get(9," Not a valid key"))
print(monthConv2.get["january"])
print(monthConv["mov"])
print("""

""")




#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     30/03/2019
# Copyright:   (c) User 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
print("""dictionaries in python are list and/or with keys, key value pairs,
it is like a map tool""")

print("""dictionaries in python are list and keys, it is like a map too,
key value pairs, they are created by { }""")
students1={"Eric":14, "Bob":12, "Cris":15, "Todd":16}
print(""" students1={"Eric":14, "Bob":12, "Cris":15, "Todd":16} """)
print("""len(students1) = """, len(students1))

print(len(students1))

print("""students1.keys(), # which will show the keys of the dictionary
 = """, students1.keys())
print("""students1.values(), # which will show the values of the dictionary
 = """, students1.values())

students2={"Bric":24, "sob":32, "Cristen":25, "Lodd":26}
print(""" students2={"Bric":24, "sob":32, "Cristen":25, "Lodd":26} """)
print(''' print("""students1.update(students2) = """ , students1)
print(students1.update(students2))
print(students1) ''')
students1.update(students2)
print("""students1.update(students2) = """ , students1)
print(students1.update(students2))
print("""print(students1) = """, students1 )
print(students1)

print("""dictionaries in python are list and keys,
it is like a map tool""")

print("""dictionaries in python are list and keys, it is like a map too,
they are created by { }""")

students1={"Eric":14, "Bob":12, "Cris":15, "Todd":16}
print("""print(students1["Bob"]) will show bob's age  """ )
print(students1["Bob"])
print("""update the dictionary or change or deleate  a value of dictionary,
 so if we inpute,  students1["Bob"]= 13, then print(students1["Bob"])
 will show  bob's new age """)
students1["Bob"]= 13
print(students1["Bob"])

print(""" del students1["Bob"] will deleate the key Bob fro list ,
so print(students1["Bob"]) will show error """)
del students1["Bob"]
print("""print(students1) will show the value of the dictionary
 """ , students1)
print("""print(students1["eric"]) wil produce error because python is case sencitive,
it should be print(students1["Eric"])""" )
print(students1["Eric"])
print(students1)
print("Basic functiuonds used in dictionaries len, del keys etc")
print("""to clear all the values in the dictionaty we have to type
dictionaryname.clear(). so, for this exaple , students1.clear() ,
now if we print(students1)  , it will show blank/empty dictionary {},
and del students1, will delete the dictionary, now print(students1)
will produce error  """)
students1.clear()
print(students1)


del students1
students1={"Eric":14, "Bob":12, "Cris":15, "Todd":16}
print(""" students1={"Eric":14, "Bob":12, "Cris":15, "Todd":16} """)
print("""len(students1) = """, len(students1))

print(len(students1))

print("""students1.keys(), # which will show the keys of the dictionary
 = """, students1.keys())
print("""students1.values(), # which will show the values of the dictionary
 = """, students1.values())


students2={"Bric":24, "sob":32, "Cristen":25, "Lodd":26}
print(""" students2={"Bric":24, "sob":32, "Cristen":25, "Lodd":26} """)

print(""" update a dictionary by writing students1.update(students2), here the
students1 dictionary has been updated by adding students2 dictionary keys &
values""")
students1.update(students2)
print("""students1.update(students2) = """ , )
print("""print(students1) = """, students1 )
print(students1)
print(students2.get("sob"))
print("""print(students2.get("sob") is uded to not to produce error message
if there is no  or incorrect value input sought from get()
""")
print(students2.get("jj"))
print(""" print(students2.get("jj")) will produce a result = none,
because there is no key named jj
""")

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
print(monthConv2.get(3))
print(monthConv2.get(7))
print(monthConv2.get(9," Not a valid key"))
print("""

""")
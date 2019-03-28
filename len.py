#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     28/03/2019
# Copyright:   (c) user 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

print(''' for length of variable values
use len function''')

x=len('hello')
print(x)

print("print(len('hello')) = " + str(len('hello')) )

print("print(len('hello')) = " , len('hello'))
print(''' for length of variable values
use len function''')

x=len('hello')
print(x)

print("print(len('hello')) = " + str(len('hello')) )

print("print(len('hello')) = " , len('hello'))

shoppinglist2=['eggs', 'carrots', 'milk', 'cherries', 'apples']

print('print(shoppinglist2) =', len(shoppinglist2))

print("Basic functiuonds used in dictionaries len, del keys etc")

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
it shouls be print(students1["Eric"])""" )
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

value= "NAME yahoo"
print(value.upper().isupper())

print(""" tro find out length of the string-
print(len(value))
""")
print(len(value))
shoppinglist1="eggs, corrots, milk, apples"

print("shoppinglist1= eggs, corrots, milk, cherried, apples")

print('the above one is not a list data type of python')

shoppinglist2=['eggs', 'carrots', 'milk', 'cherries', 'apples']

print(" the list named - shoppinglist2=['eggs', 'carrots', 'milk', 'cherries', 'apples'] is created")

print('print(shoppinglist2[3]) =', shoppinglist2[3])
print('print(shoppinglist2[0]) =', shoppinglist2[0])

print(" can update all or can also update only one item in the list ")

shoppinglist2[3]= "mango milk"
print('print(shoppinglist2[3]) =', shoppinglist2[3])
print('print(shoppinglist2) =', len(shoppinglist2))

print('''print(len(shoppinglist2)) = ''', shoppinglist2 )
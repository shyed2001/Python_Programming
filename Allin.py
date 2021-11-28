##!/usr/bin/env python3
# # https://stackoverflow.com/questions/7670303/purpose-of-usr-bin-python3-shebang

# https://en.wikipedia.org/wiki/Shebang_(Unix)
# # Python Reference  https://www.w3schools.com/python/python_reference.asp
# #-----------------------------------------------------------------------------
# Name:        Python Intro
# Purpose:     Started in Py
#
# Author:      User/Shyed
#
# Created:     30/03/2019
# Copyright:   (c) User 2019
# Licence:     <User/Shyed/your licence>
#------------------------------------------------------------------------------
print("The Start The Start The Start The Start ?\n")

print("The Start The Start The Start The Start ?")
#\n introduces a new line

print("Python Review Revisit Relearn Project")

print("Minimum time project")

name = "Shyed Shahriar Housaini"
country = 'Bangladesh'
age = 36
discipline, grade = "Engineering", 3.00
PI = 3.14
numbersList = [1, 2, 3, 4]
listComprihension1 = [x for x in range(0, 100, 3)]
listComprihension2 = [x for x in range(0, 100)]
listComprihension3 = [x for x in range(100)]
print("In python Comments starts with #")
print("In python \\n will add a new line #")  # put a \ in front of \n to print string |n
print("In python multi line Comments starts with ''' and ends with '''")
'''this
is a
multi line
comment
'''
print("Variables")

x = 7
print(x)
print(x + 5)
y = 4
z = 5
print(x + y + z)
x = "This is a string"
print(x + "!")
x = 'This is a string'
print("x" + "!")

lastname = 3
Lastname = 4
print(lastname + Lastname)

print("In place operators")
x = 7
x += 2
print(x)
x -= 3
print(x)
x *= 4
print(x)
x /= 2
print(x)

print("Booleans")

"Bruce" == "bruce"
print("Bruce" == "bruce") # Output False
print("Bruce" == "Bruce") # Output True
print(numbersList)
print(country.upper())

isGood = True
# get the type of variables
# get the type of variables Data Type

print(type(numbersList))
print(type(listComprihension1))
print(type(grade))
print(type(discipline))
print(type(age))
print(type(PI))
print(type(isGood))

# array #list
# .len
# .append
# .insert
# Tuples
# Dictionaries
# .format
# .items
# class
# object
# methods
# replace
# upper
# lower
# BUILTIN python methods and functions
#builtin functions
#builtin methods
# import modules
# Functions
# Parameters and Arguments





print(listComprihension1)
print(listComprihension2)
print(listComprihension3)

# Dynamically typed language
age = 36
brand: str = "digitalbd"
isLow: bool = False
yearsofstarting: int = 2021
email = f"""
hello {brand}
age is {3 + 6}
started at {yearsofstarting + age}"""
# Defining function data type

print(email)
print(f"hello {brand}age is {3 + 6}started at {yearsofstarting + age}")


def hello() -> str:
    return "hello"


print(country.upper())
print(len(country))
print(country.replace('B', 'b'))

print('Ban' in country)

print('Ban' not in country)

# python string manipulation
# python string manipulation


'''
Method #1: using String concatenation
In the first method, we'll concentrate a variable with a string by using +.

Let's see the following example.


# variable
variable = "Python"

# insert a variable into string using String concatenation
print("Hello " + variable + " I'm Pytutorial")

Output:

Hello Python I'm Pytutorial

If your variable type is an integer, you must convert it to string before concertante.
To converting we'll use the str() function.


# variable
variable = 33

# insert a variable into string using concatenation
print("Hello " + str(variable) + " I'm Pytutorial")

Output:

Hello 33 I'm Pytutorial

Method #2: using the "%" operator
By using the "%" operator, we can insert a variable wherever we want into a string.
%s: for string
%d: for integer

Let's see how to use this method?


# variable
variable = "Python"

# insert a variable into string using "%" operator
insert_var = "Hello %s I'm Pytutorial"%variable

#print
print(insert_var)

Output:

Hello Python I'm Pytutorial

Inserting multi variables.


# variable
variable_1 = "Python"
variable_2 = "Django"

# insert multi variables into string using "%" operator
insert_var = "Hello %s and %s I'm Pytutorial"%(variable_1, variable_2)

#print
print(insert_var)

Output:

Hello Python and Django I'm Pytutorial

Insert integer variable into string using %d:


# variable
age = 20

# insert multi variables int into a string
insert_var = "Hello Python and Django I'm Pytutorial I'm %d years old"%age

#print
print(insert_var)

Output:

Hello Python and Django I'm Pytutorial I'm 20 years old

Method #3: using the format() function
Another method to insert a variable into a string is by using the format() function.


variable_1 = "Python"
variable_2 = "Django"
age = 20

# insert variables into string using format()
insert_var = "Hello {} and {} I'm Pytutorial I'm {} years old".format(variable_1, variable_2, age)

#print
print(insert_var)

Output:

Hello Python and Django I'm Pytutorial I'm 20 years old

Method #4: using f-string
F-string is my favorite method to insert a variable in a string.
Let's see how to use it.

Note: this method works on Python >= 3.6.


variable_1 = "Python"
variable_2 = "Django"
age = 20

# insert variables into string using f-string
insert_var = f"Hello {variable_1} and {variable_2} I'm Pytutorial I'm {age} years old"

#print
print(insert_var)

Output:

Hello Python and Django I'm Pytutorial I'm 20 years old

Conclusion
Today, we learned about inserting a variable in a string by using many methods, and the question arises is:
What is the best method for that?
Method #4 is the best for me.

String Manipulation in Python
Author: PFB Staff Writer
Last Updated: August 28, 2020

Overview
A string is a list of characters in order.

A character is anything you can type on the keyboard in one keystroke,
like a letter, a number, or a backslash.

Strings can have spaces:

"hello world".
An empty string is a string that has 0 characters.

Python strings are immutable

Python recognize as strings everything that is delimited by quotation marks
(” ” or ‘ ‘).

String Manipulation
To manipulate strings, we can use some of Pythons built-in methods.

Creation
word = "Hello World"

>>> print word
Hello World
Accessing
Use [ ] to access characters in a string

word = "Hello World"
letter=word[0]

>>> print letter
H
Length
word = "Hello World"

>>> len(word)
11
Finding
word = "Hello World">>> print word.count('l') # count how many times l is in the string
3

>>> print word.find("H") # find the word H in the string
0

>>> print word.index("World") # find the letters World in the string
6
Count
s = "Count, the number of spaces"

>>> print s.count(' ')
8
Slicing
Use [ # : # ] to get set of letter

Keep in mind that python, as many other languages, starts to count from 0!!

word = "Hello World"

print word[0] #get one char of the word
print word[0:1] #get one char of the word (same as above)
print word[0:3] #get the first three char
print word[:3] #get the first three char
print word[-3:] #get the last three char
print word[3:] #get all but the three first char
print word[:-3] #get all but the three last character

word = "Hello World"

word[start:end] # items start through end-1
word[start:] # items start through the rest of the list
word[:end] # items from the beginning through end-1
word[:] # a copy of the whole list
Split Strings
word = "Hello World"

>>> word.split(' ') # Split on whitespace
['Hello', 'World']
Startswith / Endswith
word = "hello world"

>>> word.startswith("H")
True

>>> word.endswith("d")
True

>>> word.endswith("w")
False
Repeat Strings
print "."* 10 # prints ten dots

>>> print "." * 10
..........
Replacing
word = "Hello World"

>>> word.replace("Hello", "Goodbye")
'Goodbye World'
Changing Upper and Lower Case Strings
string = "Hello World"

>>> print string.upper()
HELLO WORLD

>>> print string.lower()
hello world

>>> print string.title()
Hello World

>>> print string.capitalize()
Hello world

>>> print string.swapcase()
hELLO wORLD
Reversing
string = "Hello World"

>>> print ' '.join(reversed(string))
d l r o W o l l e H
Strip
Python strings have the strip(), lstrip(), rstrip() methods for removing
any character from both ends of a string.

If the characters to be removed are not specified then white-space will be removed

word = "Hello World"
Strip off newline characters from end of the string

>>> print word.strip('
')
Hello World

strip() #removes from both ends
lstrip() #removes leading characters (Left-strip)
rstrip() #removes trailing characters (Right-strip)

>>> word = " xyz "

>>> print word
xyz

>>> print word.strip()
xyz

>>> print word.lstrip()
xyz

>>> print word.rstrip()
xyz
Concatenation
To concatenate strings in Python use the “+” operator.

"Hello " + "World" # = "Hello World"
"Hello " + "World" + "!"# = "Hello World!"
Join
>>> print ":".join(word) # #add a : between every char
H:e:l:l:o: :W:o:r:l:d

>>> print " ".join(word) # add a whitespace between every char
H e l l o W o r l d

Testing
A string in Python can be tested for truth value.

Recommended Python Training
For Python training, our top recommendation is DataCamp.

Free Trial
The return type will be in Boolean value (True or False)

word = "Hello World"

word.isalnum() #check if all char are alphanumeric
word.isalpha() #check if all char in the string are alphabetic
word.isdigit() #test if string contains digits
word.istitle() #test if string contains title words
word.isupper() #test if string contains upper case
word.islower() #test if string contains lower case
word.isspace() #test if string contains spaces
word.endswith('d') #test if string endswith a d
word.startswith('H') #test if string startswith H
If you liked this article, please share it with your friends.

'''

# indentation
import keyword

# Reserved  Keywords
print("Python Reserved  Keywords")
print(keyword.kwlist)

# Reserved  Keywords
'''
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async',
'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with',
  'yield']
'''

print("File destination is - cd c://python372 ")
print("File name is - py Allin.py")

print("""print("Hallow  world") will show =
""", "Hallow  world")

print(" strings are \n just plain texts")
kotha = "kotha = strings are just plain texts"
kotha2 = """kotha2  = strings are
just plain texts"""

print(kotha)
print(kotha2)

print(" strings are " \
      "just plain texts")

print("strings are just plain texts")
print("work with us")

print(" strings are \n just plain texts")
print(""" to change to lower case letters -
phrase= "NAME"
print(phrase.lower())
 """)
phrase = "NAME"
print(phrase.lower())

print("""  to check if they are all lower case letters  -
phrase= "NAME"
print(phrase.islower()) = """)
phrase = "NAME"
print(phrase.islower())

print("""
 to change to upper case letters -
Val= "yahoo"
print(val.upper())= """)
val = "yahoo"
print(val.upper())

print("""
 to check if they are all upper case letters -
Val= "yahoo"
print(val.isupper())= """)
val = "yahoo"
print(val.isupper())

print(""" use combination of change & check-
value= "NAME yahoo"
print(value.upper().isupper())= """)
value = "NAME yahoo"
print(value.upper().isupper())

print(""" to find out length of the string-
print(len(value))
""")
print(len(value))

print(''' get specific characters from strings using their index
print(value[0])
print(value[0:7])
print(value[0], value[0:5]) =
''')
print(value[0])
print(value[0:7])
print(value[0], value[0:5])

print(''' get index number of a character by
print(value.index("E")) = ''')
print(value.index("E"))

print(''' get index starting number of a word by
print(value.index("yah")) = ''')
print(value.index("yah"))

print(''' replace word or letter by
print(value.replace("yahoo", "john")) = ''')
print(value.replace("yahoo", "john"))

name = input('Please enter your anme:   ')
age = input(' Please enter your age:    ')
print(" Hello", name, "you are ", age)

print("""print(" Hallow  "  "  world.") will show =
""", " Hallow  "  "  world.")

print("""print('what are u doing. don\'t go') -
The above code line will produce error message.""")
print("""print('what are u doing. don\'t go') will show
""", ('what are u doing. don\'t go', """
have to put \'  in a line with in ('') ."""))

print("""Mathematical operator order is - BEDMAS
or PEDMAS""")

print("""print("BEDMAS" "=") will show  , ("BEDMAS" "=") """)
print("BEDMAS" "=" """"Brackets, Exponents, Division,
 Multiplication, Addition, Subtraction""")

print("""PEDMAS = Parenthecis (), Exponents **, Division /,
 Multiplication *, Addition + , Subtraction - """)

print("""left to right or left associative rule
 for * / - + operators""")
print("""# Arithmetic Operators
#+ - * / are operators
#Digits are operands. """)

# Arithmetic Operators
# Arithmetic Operators
# Arithmetic Operators
# + - * / are operators
# Digits are operands.


print(2 + (3 - 1))
print(("print(6-3+2) =") + str(6 - 3 + 2))
print(("print(6-3+2) =") + str(6 - 3 + 2))

print(("print(6-3+2) =") + str(6 - 3 + 2))

print(("print(6/3*2) =") + str(6 / 3 * 2))
print("left to right or left associative rule for * / - + operators")
# ----------------------
print("but for ** right to left or right associative rule for * / - + operators")
print(("print(2**3**2) =") + str(2 ** 3 ** 2))

print(("2+3") + "=" + str(2 + 3))

print(2 + (3 - 1))
print("(2+(3-1))" + "=" + str(2 + (3 - 1)))

print(9 / 3)
print(("9/3") + "=" + str(9 / 3))
print(9 / 3.0)
print(("9/3.0") + "=" + str(9 / 3.0))
print(9.0 / 3)
print(("9.0/3") + "=" + str(9.0 / 3))

print(9 * 3)
print(("9*3") + "=" + str(9 * 3))
print(9.0 * 3)

print(9 * 3.0)
print(("9*3.0") + "=" + str(9 * 3.0))

print((9 - 1 + 2) + (9 / 3 * 3))
print(("((9-1+2)+(9/3*3))") + "=" + str((9 - 1 + 2) + (9 / 3 * 3)))
print(("(((-9)-1+2)+(9/3*(-3)))") + "=" + str(((-9) - 1 + 2) + (9 / 3 * (-3))))

print((-9) * (-3))
print(("(-9)*(-3)") + "=" + str((-9) * (-3)))
print(("(-9)/(-3)") + "=" + str((-9) / (-3)))
print(("-9/-3") + "=" + str(-9 / -3))
print(("-9*-3") + "=" + str(-9 * -3))

print("idleAllin2.py")
print(
    "================03-03-2019=====================04-03-2019=========\n==========================\n=====================")
print(("10/3") + "=" + str(10 / 3))

print(("-10/3") + "=" + str(-10 / 3))
print(("10/-3") + "=" + str(10 / -3))

print(9.73800000000)
print(("9.73800000000") + "=" + str(9.73800000000))
print(("9.738043625475237500") + "=" + str(9.738043625475237500))
print(("9.73804362547523750082364862865821") + "=" + str(9.73804362547523750082364862865821))

print(("10**3") + "=" + str(10 ** 3))

print((" Quotient of ") + (" 10//3 ") + " = " + str(10 // 3))

print((" Remainder of ") + (" 10%3 ") + " = " + str(10 % 3))

A = 14
B = 40
print(""" IF input is A=14 and B=40 then,
 modolous // and remainder % is """)
print("print(A//B) = ", A // B)
print("print(A%B) = ", (A % B))

print(("\"") + "=" + str("\""))

print(("\""))
print("\"")
print(("Hallow  world"))

print('Don\'t go there')

print("Don\'t go there")
print("Don't go there")
print('Don"t go there')
print("Don\"t go there")

print("Don\	t go there")
print("Don\t go there")

print(("Hallow\nworld"))
print(("Hallow  \n  world"))
print(("Hallow world"))
print(("Hallow""world"))
print(("Hallow"
       "world"))
print("""Hallow"+
	   world""")
print("""Hallow"""
      """world""")
print("""Hallow
world""")

print("Hallow, world")
print("Concatenation")
print("2" + "3")
print("2.0" + "3.0")
print("Fun" * 3)
print("2" * 3)

print(("(\"Fun\" * 0)") + "=" + str(("Fun" * 0)))
print("Fun" * 0)
print(("(\"9\" * 0)") + "=" + str("9" * 0))
print("9" * 0)
print("New Start")
print("New Start at office on 04-03-2019 ============================================")

print(3 * 2)
print(3 ** 2)
print(3 + 2)

print(("print(-12//12) =") + str(-12 // 12))
print(("print(12%11) =") + str(12 % 11))
print(("print(-12%11) =") + str(-12 % 11))
print(12 % 11)
print(-12 % 11)

print(''' for length of variable values
use len function''')

x = len('hello')
print(x)

print("print(len('hello')) = " + str(len('hello')))

print("print(len('hello')) = ", len('hello'))

print(" spam " + " egg ")
print("spam," + " egg")
print("spam'" + " egg")
print("spam and egg")

print("start at home 04-03-2019========================")

print(3 ** 2)
print(3.0 ** 2)
print("(3**2)" + "=" + str(3 ** 2))
print("(3.0**2)" + "=" + str(3.0 ** 2))
print("(OK * 2)" + "=" + str("OK" * 2))
print("(OK * 2 )" + "=" + ("OK" * 2))
print("(OK * 2.0 )" + "=" + ("Error"))

print("""print("(3**2)", "=" , str(3**2))""")
print("and / or")
print("""print("(3**2)"+ "=" + str(3**2))""")
print("will show")
print("(3**2)", "=", str(3 ** 2))

print(("(\"Fun\" * 0)") + "=" + str(("Fun" * 0)))
print("Fun" * 0)
print(("(\"9\" * 0)") + "=" + str("9" * 0))
print("9" * 0)

# Arithmetic Operators
'''
Python Arithmetic Operators
Difficulty Level : Medium
Last Updated : 29 Aug, 2020
Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication and division.

There are 7 arithmetic operators in Python :

Addition
Subtraction
Multiplication
Division
Modulus
Exponentiation
Floor division
1. Addition Operator : In Python, + is the addition operator. It is used to add 2 values.
Example :


val1 = 2
val2 = 3

# using the addition operator
res = val1 + val2
print(res)
Output :

5
2. Subtraction Operator : In Python, – is the subtraction operator. It is used to subtract the second value from the first value.
Example :




val1 = 2
val2 = 3

# using the subtraction operator
res = val1 - val2
print(res)
Output :

-1
3. Multiplication Operator : In Python, * is the multiplication operator. It is used to find the product of 2 values.
Example :


val1 = 2
val2 = 3

# using the multiplication operator
res = val1 * val2
print(res)
Output :

6
4. Division Operator : In Python, / is the division operator. It is used to find the quotient when first operand is divided by the second.
Example :


val1 = 3
val2 = 2

# using the division operator
res = val1 / val2
print(res)
Output :

1.5
5. Modulus Operator : In Python, % is the modulus operator. It is used to find the remainder when first operand is divided by the second.
Example :


val1 = 3
val2 = 2

# using the modulus operator
res = val1 % val2
print(res)
Output :

1
6. Exponentiation Operator : In Python, ** is the exponentiation operator. It is used to raise the first operand to power of second.
Example :


val1 = 2
val2 = 3

# using the exponentiation operator
res = val1 ** val2
print(res)
Output :

8
7. Floor division : In Python, // is used to conduct the floor division. It is used to find the floorof the quotient when first operand is divided by the second.
Example :


val1 = 3
val2 = 2

# using the floor division
res = val1 // val2
print(res)
Output :

1
Below is the summary of all the 7 operators :

Operator	Description	Syntax
+	Addition: adds two operands	x + y
–	Subtraction: subtracts two operands	x – y
*	Multiplication: multiplies two operands	x * y
/	Division (float): divides the first operand by the second	x / y
//	Division (floor): divides the first operand by the second	x // y
%	Modulus: returns the remainder when first operand is divided by the second	x % y
**	Power : Returns first raised to power second	x ** y
# Arithmetic Operators

'''

# if statement # if statement
# if statement # if statement


print("if & else statement, conditional statements")
print("if & else statement, conditional statements")
print("if statement")
print("if statement")

print('''if 6 > 4:
    print("true, 6 is greater than 4 ")
print('n=12')
n = 12
if n > 5:
    print("n is greater than 5 ")
    if n <= 15:
        print("n is less than 15 ")''')

if 6 > 4:
    print("true, 6 is greater than 4 ")
print('n=12')
n = 12
if n > 5:
    print("n is greater than 5 ")
    if n <= 15:
        print("n is less than 15 ")
print(''' a = 15
if a == 11:
    print('a!=11')
else:
    print('a=15')
if 1 + 1 == 2:
    if 2 * 2 == 8:
        print('if')
    else:
        print('else')
print('out of the loop')''')
a = 15
if a == 11:
    print('a!=11')
else:
    print('a=15')
if 1 + 1 == 2:
    if 2 * 2 == 8:
        print('if')
    else:
        print('else')
print('out of the loop')
num = 7
if num > 3:
    print('>3')
else:
    print('else')
if num == 7:
    print('==7')
print('out of the loop')
print('in the loop')

print('''
num = 7
if num > 3:
    print('>3')
else:
    print('else')
    if num == 7:
        print('==7')
print('in the loop')
''')
num = 7
if num > 3:
    print('>3')
else:
    print('else')
    if num == 7:
        print('==7')
print('in the loop')


print('''

''')
print('''

''')
print('''

''')
print('''

''')
print('''
esnum = 7
if esnum == 2:
    print('esnum == 2')
else:
    if esnum == 12:
        print('esnum == 12')
    else:
        if esnum == 22:
            print('esnum == 12')
        else:
            if esnum == 7:
                print('esnum == 7')


''')
esnum = 7
if esnum == 2:
    print('esnum == 2')
else:
    if esnum == 12:
        print('esnum == 12')
    else:
        if esnum == 22:
            print('esnum == 12')
        else:
            if esnum == 7:
                print('esnum == 7')



print("elif statements")
print("elif")
elifsnum = 7
if elifsnum == 2:
    print('esnum == 2')
elif elifsnum == 12:
    print('esnum == 12')
elif elifsnum == 22:
    print('elifsnum == 12')
elif elifsnum == 7:
    print('elifsnum == 7')

print("Nested if and else statements")
print(""" esnum = 22
if esnum == 22:
   if esnum>22:
            print('esnum == 22')
   else:
            print('esnum == unknown') """)
esnum = 22
if esnum == 22:
    if esnum > 22:
        print('esnum == 22')
    else:
        print('esnum == unknown')
print("""A=3
B=5
C=7
if A==3:
   if B==5 and C<=7:
      if not A == 5:
         print("Nested if statements")
      else:
           print("Zero")
= """)

print("if & else statement, conditional statements")
print("if statement")
A = 3
B = 5
C = 7
if A == 3:
    if B == 5 and C <= 7:
        if not A == 5:
            print("Nested if statements")
        else:
            print("Zero")
print("Ternary If Statements if & else statement, conditional statements")
print(" Ternary If Statements if statement")

# Ternary If Statements
# Ternary If Statements
'''
Let's take a look at this example:

>>> age = 15
>>> # Conditions are evaluated from left to right
>>> print('kid' if age < 18 else 'adult') kid
Ternary operators can be chained:

 >>> age = 15
>>> print('kid' if age < 13 else 'teenager' if age < 18 else 'adult')
teenager
Which is the same as:


if age < 18:
if age < 12:
print('kid')
else:
print('teenager')
else:
print('adult')


'''



print('''
age = 15
# Conditions are evaluated from left to right
print('kid' if age < 18 else 'adult') kid
''')
age = 15
# Conditions are evaluated from left to right
print('kid' if age < 18 else 'adult')
#Ternary operators can be chained:
print(''' #Ternary operators can be chained:
age = 15
print('kid' if age < 13 else 'teenager' if age < 18 else 'adult')
''')

age = 15
print('kid' if age < 13 else 'teenager' if age < 18 else 'adult')

#Lists

print('''
#Lists
#Lists


print(type[])
''')
print(type[1,2])

print('''
NUMBERS = [1, 2, 2, 3, 4, -1, 0, ['A','B']]

print(NUMBERS)
print(NUMBERS[0])
print(NUMBERS)
print(NUMBERS[3])
print(NUMBERS[6][1])
print(NUMBERS[6][2])
# print(NUMBERS[7]) this will give errors
''')
NUMBERS = [0, 0, 1, 1, 2, 3, 4, 6,7, -1, 0, ['A','B']]

print(NUMBERS)
print(NUMBERS[0])
print(NUMBERS)
print(NUMBERS[3])
print(NUMBERS[11][1])
print(NUMBERS[11][2])
# print(NUMBERS[17]) this will give errors
print('''
NUMBERS = [0, 0, 1, 1, 2, 3, 4, 6,7, -1, 0, ['A','B']]
In lists Duplicates are allowed
print(NUMBERS)
print(NUMBERS[0])
print(NUMBERS)
print(NUMBERS[3])
print(NUMBERS[11][1])
print(NUMBERS[11][2])
# print(NUMBERS[17]) this will give errors
''')



print('''
List Methods
List Methods

NUMBERS.sort()
print(NUMBERS)


NUMBERS.reverse()
print(NUMBERS)

NUMBERS.append(100)
print(NUMBERS)

NUMBERS.remove(2)
print(NUMBERS)

print(2000 in numbers)
print(100 in numbers)
print(100 not in numbers)

NUMBERS.pop()
print(NUMBERS)

NUMBERS.pop()
NUMBERS.pop()
print(NUMBERS)
NUMBERS = [0, 0, 1, 1, 2, 3, 4, 6,7, -1, 0, ['A','B']]
del NUMBERS[0]
print(NUMBERS)
NUMBERS = [0, 0, 1, 1, 2, 3, 4, 6,7, -1, 0, ['A','B']]
del NUMBERS[0:7]
print(NUMBERS)
NUMBERS.clear()
print(NUMBERS)
print(len(NUMBERS))
''')
NUMBERS.sort()
print(NUMBERS)


NUMBERS.reverse()
print(NUMBERS)

NUMBERS.append(100)
print(NUMBERS)

NUMBERS.remove(2)
print(NUMBERS)

print(2000 in numbers)
print(100 in numbers)
print(100 not in numbers)

NUMBERS.pop()
print(NUMBERS)

NUMBERS.pop()
NUMBERS.pop()
print(NUMBERS)
NUMBERS = [0, 0, 1, 1, 2, 3, 4, 6,7, -1, 0, ['A','B']]
del NUMBERS[0]
print(NUMBERS)
NUMBERS = [0, 0, 1, 1, 2, 3, 4, 6,7, -1, 0, ['A','B']]
del NUMBERS[0:7]
print(NUMBERS)
NUMBERS.clear()
print(NUMBERS)
print(len(NUMBERS))


print(''' SETS vSETS
In lists Duplicates are allowed
sets sets  # Duplicates are not allowed
''')
print('''
NUMBERSLIST= [0, 0, 1, 1, 2, 3, 'a', 4, 6,7, -1, 0, ['A','B']]
print(NUMBERSLIST)
NUMBERSET= {0, 0, 1, 1, 2, 3, 4, 6,7, -1, 0, ['A','B']}
print(NUMBERSET)
''')
NUMBERSLIST= [0, 0, 1, 1, 2, 3, 'a', 4, 6,7, -1, 0, ['A','B']]
print(NUMBERSLIST)
NUMBERSET= {0, 0, 1, 1, 2, 3, 4, 6,7, -1, 0, ['A','B']}
print(NUMBERSET)

print('''
All the methods in lists works in sets,
 but in sets duplicates are not allowed and order is not gurranteed.
''')


print('''
Set Union Intersection & Difference
Set Union Intersection & Difference
''')
'''

Python set operations (union, intersection, difference and symmetric difference)
Python Set | difference()
Python program to find common elements in three lists using sets
Python | Print all the common elements of two lists
Python | Intersection of two lists
Python | Union of two or more Lists
Union() function in Python
round() function in Python
floor() and ceil() function Python
Python math function | sqrt()
numpy.sqrt() in Python
numpy.square() in Python
numpy.sum() in Python
numpy.add() in Python
numpy.subtract() in Python
Python | Difference between two lists
Python | Check if two lists are identical
Python | Check if all elements in a list are identical
Python | Check if all elements in a List are same
Class method vs Static method in Python
Class or Static Variables in Python
Changing Class Members in Python
Constructors in Python
Destructors in Python
Inheritance in Python
Adding new column to existing DataFrame in Pandas
Python map() function
Taking input in Python
How to get column names in Pandas dataframe
Iterate over a list in Python

Python set operations (union, intersection, difference and symmetric difference)
Last Updated : 18 Dec, 2017
This article demonstrates different operations on Python sets.
Examples:

Input :
A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}

Output :
 Union : [0, 1, 2, 3, 4, 5, 6, 8]
 Intersection : [2, 4]
 Difference : [8, 0, 6]
 Symmetric difference : [0, 1, 3, 5, 6, 8]
In Python, below quick operands can be used for different operations.

| for union.
& for intersection.
– for difference
^ for symmetric difference


# Program to perform different set operations
# as we do in  mathematics

# sets are define
A = {0, 2, 4, 6, 8};
B = {1, 2, 3, 4, 5};

# union
print("Union :", A | B)

# intersection
print("Intersection :", A & B)

# difference
print("Difference :", A - B)

# symmetric difference
print("Symmetric difference :", A ^ B)
Output:

('Union :', set([0, 1, 2, 3, 4, 5, 6, 8]))
('Intersection :', set([2, 4]))
('Difference :', set([8, 0, 6]))
('Symmetric difference :', set([0, 1, 3, 5, 6, 8]))
'''

# sets are define
A = {0, 2, 4, 6, 8};
B = {1, 2, 3, 4, 5};

# union
print("Union :", A | B)

# intersection
print("Intersection :", A & B)

# difference
print("Difference :", A - B)

# symmetric difference
print("Symmetric difference :", A ^ B)


print('''

''')
print('''

''')
print('''

''')

print('''

''')
print('''

''')

print('''

''')
print('''

''')
print('''

''')






print(" The slice operators of strings")

print(" The slice operators of strings")

print(""" The slice operators, or indexing in python
 starts from  0 """)

name = "12345 67890"
print(""" in name ='12345 67890' the blank space is also a character""")
print(name[0])
print(name[1])
print(name[3])
print(name[5])
print("print(name[0]) = ", (name[0]))
print("print(name[1]) = ", (name[1]))
print("print(name[3]) = ", (name[3]))
print("print(name[5]) = ", (name[5]))
print("print(name[4:9]) = ", (name[4:9]))
print("print(name[4:]) = ", (name[4:]))
print(""" The slice operators, or indexing in python
 starts from  0
 and the last index nuberd one is ignored """)
print(''' for printing a charecter to the
ignored ''')
print(""" to printing a charecter, (5th to last) last
character [4:] is used """)

random = 'abc def ghi jklm'

print(""" in the random = 'abc def ghi jklm' blank spaces
are also characters and are also indexed""")
print(random[0])
print(random[1])
print(random[3])
print(random[5])
print("print(random[0]) = ", (random[0]))
print("print(random[1]) = ", (random[1]))
print("print(random[3]) = ", (random[3]))
print("print(random[5]) = ", (random[5]))

print("print(random[0:5]) = ", (random[0:5]))
print("print(random[3:7]) = ", (random[3:7]))
print("print(random[3:]) = ", (random[3:]))
print(""" The slice operators, or indexing in python starts from
 0 and the last index nuberd one is ignored """)
print(""" to printing a charecter, from 4th to last to the  last
character [3:] is used """)






# ----------

print("python loops")

print("""python loops or iterator with range():
                loops are codes those are done again and again checkin
                conditions until the cindition becomes false.
                """)

for i in range(0, 5):
    print(i)
print("python loops")

print("""python loops or iterator with range():
                loops are codes those are done again and again checking
                conditions until the cindition becomes false.
shoppinglist2=['eggs', 'carrots', 'milk', 'cherries', 'apples']
""")

shoppinglist2 = ['eggs', 'carrots', 'milk', 'cherries', 'apples']
for i in shoppinglist2:
    print(i)

for i in range(5):
    print(i)
for i in range(3):
    print(i)
    print("end of loop in loops")
print(" out of end of all loop ")

for i in range(1, 4):
    print(i)
    print("end of loop in loops")
for i in range(1, 2):
    print(i)
print(" out of end of all loop ")

print("python loops or iterator")
print("python loops - for loop, and while loop")

name = "shyed"

for x in name:
    print("Looping")
for x in name:
    print(x)
for a in name:
    print(x, a)
for z in name:
    print(z, x, a)
for z in name:
    print(x)
for x in name:
    print(z)
name = "sssh"

for x in name:
    print("Looping")

for x in name:
    print(x)

for x in name:
    print(" For the letter in the variable x is : " + x)

name = "3333"

for x in name:
    print("22222")

for x in name:
    print(x)
    print(" For the letter in the variable x is : " + x)
print("Out of Loop For the letter in the variable x is : " + x)

name = "abcdefg"

for x in name:
    print("12345 ")

for x in name:
    print(x)
    print(" For the letter in the variable x is : " + x)
print('end from outside of loop')

print("python loops")

print("""python loops or iterator with range():
                loops are codes those are done again and again checking
                conditions until the condition becomes false.
shoppinglist2=['eggs', 'carrots', 'milk', 'cherries', 'apples']
""")
shoppinglist2 = ['eggs', 'carrots', 'milk', 'cherries', 'apples']
for i in shoppinglist2:
    print(i)

print(""" range() can have 3 values, range(sarting , ending , incrientation)
like range (0, 21, 2)
so if we type the codes
for i in range (0, 21, 2):
    print(i)
""")
print("for loop with range and incremenr")
print(""" for i in range (0, 21, 2):
     print(i)
""")
for i in range(0, 21, 2):
    print(i)

print("""for i in range (34, 0, -2):
    print(i)
    count backwords with - ve incremets""")
for i in range(34, 0, -2):
    print(i)

print("""nested for loops
for i in range(0,5):
    for a in range(0,5):
        print(a)
will produce 0 to 4 , 5 times
""")
for i in range(0, 5):
    for a in range(0, 5):
        print(a)


print(""" students1 = {"Eric": 14, "Bob": 12, "Cris": 15, "Todd": 16}
print(students1.items())
for key in students1:
    print(f"key:{key} value:{students1[key]}")
for key, value in students1.items():
    print(f"key:{key} value:{value}")""")
students1 = {"Eric": 14, "Bob": 12, "Cris": 15, "Todd": 16}
print(students1.items())
for key in students1:
    print(f"key:{key} value:{students1[key]}") # if we had the keys only

for key, value in students1.items():
    print(f"key:{key} value:{value}")


print("python while loops")
print("while loops")

print("""while loop are codes those are run again and again checking for a
                conditions until the condition becomes false. then the code ends
                """)

print("""c=5
while c<10:
 c=c+1
 print(c)
 =  """)
c = 5
print("python While loops or iterator")
print("python while loops -  while loop")
while c < 10:
    c = c + 1 # c +=1
    print(c)
    print("   print (c) = ", c)
print("print (c) = ", c)
print(""" c=5
while c<10:
 print(c)
 c=c+1 """)
c = 5
while c < 10:
    print(c)
    c = c + 1 # c +=1
    print("   print (c) = ", c)
print("print (c) = ", c)

print(""" The code stops printing when
 value of c becomes, c=10 and not c<10.
""")

# ------------

my_bollean = True

print(my_bollean)
print("(2==3)" + "=" + str(2 == 3))
print(2 == 3)
print("(\"Hellow\" == \"Hellow\")" + "=" + str("Hellow" == "Hellow"))
print("Hellow" == "Hellow")
print("(\"Hellow\" == \"hellow\")" + "=" + str("Hellow" == "hellow"))
print("Hellow" == "hellow")
print("(\"Hellow\" == \"Hollaw\")" + "=" + str("Hellow" == "Hollaw"))
print("Hellow" == "Hollaw")

print(""" there are 6 comparison relational operators are >, <, <=, >=, ==, !=.

. Those relational comparison operators helps us to get buollean value true/false.
 """)

print(1 != 3)
print(5 != 5)
print("(5!=5)" + "=" + str(5 != 5))
print("(1!=3)" + "=" + str(1 != 3))
print("(5<=5)" + "=" + str(5 <= 5))
print("(7>=5)" + "=" + str(7 >= 5))
print("(1>3)" + "=" + str(1 > 3))
print("(1<3)" + "=" + str(1 < 3))
print(""" there are 6 comparison relational operators are >, <, <=, >=, ==, !=.

. Those relational comparison operators helps us to get buollean value true/false.
 """)
print(""" there are 6 relational operators are >, <, <=, >=, ==, !=.
. Those relational operators helps us to get buollean value true/false. """)


print("(num /=2) == (num = num/2)")
print("(num +=1) == (num = num+1)")
print("(num -+1) == (num = num-1)")
print("(num *= 3) == (num = num * 3)")
print("(num **= 2) == (num = num ** 2)")

# (num +=1) == (num = num+1)

# (num -+1) == (num = num-1)

# (num *= 3) == (num = num * 3)

# (num /=2) == (num = num/2)



print('Bollean logic')
print('Bollean logic')

print("2 == 2 and 3 == 3")
print("2 == 2 and 3 == 4")
print("2 == 2 or 3 == 4")
print("2 == 2 or 3 == 3")
print("not 2 == 2")
print("not 2 != 2")

print(2 == 2 and 3 == 3)
print(2 == 2 and 3 == 4)
print(2 == 2 or 3 == 4)
print(2 == 2 or 3 == 3)
print(not 2 == 2)
print(not 2 != 2)

print("with 'del' of the variable")
message = "what"
print(message)
del message
message = 'ff'
print(message)
print("with 'del' of the variable")

print("# print is a function")
print("# mixing data types")

print("data types int float string")

print("leave comments regularly and seriously")

print("There must not be spaces and dash - in the variable names")

name = " steafan "
age = 40
month = 4
print('print is a function')
print('mixing data types')
print(name)
print(name + "loves pizza")

print(age + month)

print("python loops or iterator")
print("python loops - for loop")
print(''' For the detail of  for loop please go to -
 forloop.py file''')

print('''declearing multiple variable \n values at a time and
 multiple assignments of
  same value to many variables in one line.''')

x1, x2, x3 = 'r', 'y', 'b'
print(""" When x1,x2,x3='r','y','b' , then""")

print('print(x1, x2 ,x3) =', x1, x2, x3)
print('print(x1+x2+x3) =', x1 + x2 + x3)

x1, x2, x3 = 'r' + 'y' + 'b'

print(""" When x1,x2,x3='r' +'y'+'b' , then""")

print('print(x1, x2 ,x3) =', x1, x2, x3)
print('print(x1+x2+x3) =', x1 + x2 + x3)

print(""" When y1,y2,y3=1 + 3 + 5,  then this line will produce error, because
those values can not be assigned""")

y1, y2, y3 = 1, 3, 5

print(""" When y1,y2,y3=1,3,5 , then""")
print('print (y1+ y2+y3 )=', y1 + y2 + y3)
print('print( y1, y2,y3) =', y1, y2, y3)

z1, z2, z3 = 'a', 3.3, 5
print(""" When z1,z2,z3='a',3.3,5 , then""")
print('print( z1,z2, z3) =', z1, z2, z3)
print('print( z1,z2+ z3) =', z1, z2 + z3)
print('print( z1+z2+ z3) =', '''' will produce error,
because strings can not be concatenate to int or floats''')

print(x1, x2, x3, y1, y2, y3, z1, z2, z3)

print('print(x1,x2,x3,y1,y2,y3,z1,z2,z3) =', x1, x2, x3, y1, y2, y3, z1, z2, z3)

print('print(x1+x2+x3+y1+ y2+y3+z1+z2+ z3) =', '''' will produce error,
because strings can not be concatenate to int or floats''')
print('print(x1,x2,x3, y1+y2+y3, z1,z2+z3) =', x1, x2, x3, y1 + y2 + y3, z1, z2 + z3)

X = Y = Z = 'Apple'
print(''' When X=Y=Z= "Apple" , then''')
print('print(X,Y,Z) =', X, Y, Z)
print('print(X+Y+Z) =', X + Y + Z)

print("without 'del' of the variable")
message = "wwwww"
print(message)
message = 'ffff'
print(message)
print("without 'del' of the variable")

print("with 'del' of the variable")
message = "what"
print(message)
del message
message = 'ff'
print(message)
print("with 'del' of the variable")

print("without 'del' of the variable")
message = "wwwww"
print(message)
message = 'ffff'
print(message)
print("without 'del' of the variable")

print("python loops or iterator with range():")

for i in range(5):
    print(i)
for i in range(3):
    print(i)
    print("end of loop in loops")
print(" out of end of all loop ")

for i in range(1, 4):
    print(i)
    print("end of loop in loops")
for i in range(1, 2):
    print(i)
print(" out of end of all loop ")

n = input("please input your age")

print(float(n) / 2)

print("""entered value inside input function will
always get out as string""")

print("list or arrayes, arrayes are created by using []")

shoppinglist1 = "eggs, corrots, milk, apples"

print("shoppinglist1= eggs, corrots, milk, cherried, apples")

print('the above one is not a list data type of python')

shoppinglist2 = ['eggs', 'carrots', 'milk', 'cherries', 'apples']

print(" the list named - shoppinglist2=['eggs', 'carrots', 'milk', 'cherries', 'apples'] is created")

print('print(shoppinglist2[3]) =', shoppinglist2[3])
print('print(shoppinglist2[0]) =', shoppinglist2[0])

print(" can update all or can also update only one item in the list ")

shoppinglist2[3] = "mango milk"
print('print(shoppinglist2[3]) =', shoppinglist2[3])
print('print(shoppinglist2) =', len(shoppinglist2))

print('''print(len(shoppinglist2)) = ''', shoppinglist2)

numarray1 = [7, 25, 34, 43, -52, -77]
numarray2 = [.77777, .777777777, -777, -7777]
print(""" when numarray1=[7, 25, 34, 43, -52, -77] and
numarray2= [.77777, .777777777, -777, -7777] then""")
print("""print(numarray1, numarray2)  will produce
""", (numarray1), (numarray2))
print("""print(max(numarray1) will produce
""", max(numarray1))
print("""print(min(numarray1) will produce
""", min(numarray1))

print("""print(max(numarray1, numarray2))  will produce
""", max((numarray1), (numarray2)))
print("""print(min(numarray1, numarray2))  will produce
""", min((numarray1), (numarray2)))
print("""print(min(numarray1), min(numarray2))  will produce
""", min(numarray1), min(numarray2))
print("""print(max(numarray1), max(numarray2))  will produce
""", max(numarray1), max(numarray2))

print("add another object to the list or arrey by .append")
shoppinglist2.append("Books")
print(shoppinglist2)

print("""count a list item, how many times is
was repeated inthe list by arrey.count(item)""")

shoppinglist2.count("carrots")
print(""" print (shoppinglist2.count("carrots")) will show ,
 =  1 """)
print(shoppinglist2.count("carrots"))
#
#
#
#

# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     30/03/2019
# Copyright:   (c) User 2019
# Licence:     <your licence>
# -------------------------------------------------------------------------------
print("""dictionaries in python are list and/or with keys, key value pairs,
it is like a map tool""")
print("""dictionaries in python are list and/or with keys, key value pairs,
it is like a map tool""")

print("""dictionaries in python are list and keys, it is like a map too,
key value pairs, they are created by { }""")
students1 = {"Eric": 14, "Bob": 12, "Cris": 15, "Todd": 16}
print(""" students1={"Eric":14, "Bob":12, "Cris":15, "Todd":16} """)
print("""len(students1) = """, len(students1))

print(len(students1))

print("""students1.keys(), # which will show the keys of the dictionary
 = """, students1.keys())
print("""students1.values(), # which will show the values of the dictionary
 = """, students1.values())

students2 = {"Bric": 24, "sob": 32, "Cristen": 25, "Lodd": 26}
print(""" students2={"Bric":24, "sob":32, "Cristen":25, "Lodd":26} """)
print(''' print("""students1.update(students2) = """ , students1)
print(students1.update(students2))
print(students1) ''')
students1.update(students2)
print("""students1.update(students2) = """, students1)
print(students1.update(students2))
print("""print(students1) = """, students1)
print(students1)

print("""dictionaries in python are list and keys,
it is like a map tool""")

print("""dictionaries in python are list and keys, it is like a map too,
they are created by { }""")
print(""" Keys have to be unique,
Values can be any data type
Repeated keys are not allowed""")
print("""Repeated keys are not allowed Keys have to be unique, Values can be any data type""")
students1 = {"Eric": 14, "Bob": 12, "Cris": 15, "Todd": 16}
print("""print(students1["Bob"]) will show bob's age  """)
print(students1["Bob"])
print("""update the dictionary or change or deleate  a value of dictionary,
 so if we inpute,  students1["Bob"]= 13, then print(students1["Bob"])
 will show  bob's new age """)
students1["Bob"] = 13
print(students1["Bob"])

print(""" del students1["Bob"] will deleate the key Bob fro list ,
so print(students1["Bob"]) will show error """)
del students1["Bob"]
print("""print(students1) will show the value of the dictionary
 """, students1)
print("""print(students1["eric"]) wil produce error because python is case sencitive,
it should be print(students1["Eric"])""")
print(students1["Eric"])
print(students1)
print("Basic functiuonds used in dictionaries len, del keys etc")
print("""to clear all the values in the dictionaty we have to type
dictionaryname.clear(). so, for this exaple , students1.clear() ,
now if we print(students1)  , it will show blank/empty dictionary {},
and del students1, will delete the dictionary, now print(students1)
will produce error
 print(students1.keys())
print(students1.values())""")
print(students1.keys())
print(students1.values())
students1["Eric"]=24  # Update a value
print(students1)
students1.clear()
print(students1)

students1 = {"Eric": 14, "Bob": 12, "Cris": 15, "Todd": 16}
print(students1.items())
for key in students1:
    print(f"key:{key} value:{students1[key]}")

print(len(students1))

for key, value in students1.items():
    print(f"key:{key} value:{value}")

print(""" students1 = {"Eric": 14, "Bob": 12, "Cris": 15, "Todd": 16}
print(students1.items())
for key in students1:
    print(f"key:{key} value:{students1[key]}")
for key, value in students1.items():
    print(f"key:{key} value:{value}")""")

del students1
students1 = {"Eric": 14, "Bob": 12, "Cris": 15, "Todd": 16}
print(""" students1={"Eric":14, "Bob":12, "Cris":15, "Todd":16} """)
print("""len(students1) = """, len(students1))

print(len(students1))

print("""students1.keys(), # which will show the keys of the dictionary
 = """, students1.keys())
print("""students1.values(), # which will show the values of the dictionary
 = """, students1.values())

students2 = {"Bric": 24, "sob": 32, "Cristen": 25, "Lodd": 26}
print(""" students2={"Bric":24, "sob":32, "Cristen":25, "Lodd":26} """)

print(""" update a dictionary by writing students1.update(students2), here the
students1 dictionary has been updated by adding students2 dictionary keys &
values""")
students1.update(students2)
print("""students1.update(students2) = """, )
print("""print(students1) = """, students1)
print(students1)
print(students2.get("sob"))
print("""print(students2.get("sob") is uded to not to produce error message
if there is no  or incorrect value input sought from get()
""")
print(students2.get("jj"))
print(""" print(students2.get("jj")) will produce a result = none,
because there is no key named jj
""")

monthConv = {
    "jan": "January",
    "feb": "February",
    "mar": "March",
    "apr": "April",
    "may": "May",
    "jun": "June",
    "jul": "July",
    "aug": "August",
    "sep": "September",
    "oct": "October",
    "nov": "November",
    "dec": "December"
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
print(monthConv.get("ma", " Not a valid key"))

monthConv2 = {
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
print(monthConv2.get(9, " Not a valid key"))
print("""

""")

# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     29/03/2019
# Copyright:   (c) User 2019
# Licence:     <your licence>
# -------------------------------------------------------------------------------


print("""Tuples, tuples are like lists but their values/data
can not be changed, immutable, ROM, Read Only
, now lets assume, tup1=("Maths", 23 , 3.3) """)

print("""Tuples, tuples are like lists but their values/data can not be
 changed,
 now lets assume, tup1=("Maths", 23 , 3.3, 9/3)""")

tup1 = ("Maths", 23, 3.3, 9 / 3)

print("""
print(tup1[2]) =
 """)
print(tup1[2])

print("print(tup1[0:4]) = ")
print(tup1[0:4])
print("print(tup1[0:5]) = ", (tup1[0:5]))
print("print(tup1[0:15]) = ", (tup1[0:15]))

print("""
coordinates=(4,5) --- this is a tupple, can not be changed
coordinates=[4,5] --- this is a list, items can be changed,
coordinates=[(4,5), (5,6), (6,7)] - this is a list of tupples
coordinates=[(4,5), (5,6), (6,7)]
coordinates.pop()
print(coordinates)""")
coordinates = [(4, 5), (5, 6), (6, 7)]
coordinates.pop()
print(coordinates)

print('Prime number generator in three types of code')

print('''for x in range (2, 2222):
 isPrime=True
 for y in range (2,x):
    if x%y==0:
       isPrime=False
       break # break
 if isPrime:
  print(x)
this without " break in for loop" code will produce = ''')
for x in range(2, 2222):
    isPrime = True
    for y in range(2, x):
        if x % y == 0:
            isPrime = False
    if isPrime:
        print(x)

print('''primelist1=[]
for x in range (2, 10000):
 isPrime=True
 for y in range (2,x):
    if x%y==0:
       isPrime=False
       break
 if isPrime:
    primelist.append(x)
 print(primelist1)
 Those codes with " break in for loop" will show   prime nuber list between 2 to 10000''')

primelist1 = []
for x in range(2, 10000):
    isPrime = True
    for y in range(2, x):
        if x % y == 0:
            isPrime = False
            break
    if isPrime:
        primelist1.append(x)
print('''primelist1=[]
for x in range (2, 10000):
 isPrime=True
 for y in range (2,x):
    if x%y==0:
       isPrime=False
       break
 if isPrime:
    primelist.append(x)
 print(primelist1)
 Those codes will show   prime nuber list between 2 to 10000''')
print(primelist1)

print("""primelist2=[]
lower=int(input("please enter the 'lower' or first value: " ))
upper=int(input("please enter the 'upper' or last value: " ))
for num in range (lower, upper+1):
    if num>1:
       for i in range (2,num):
           if num%i==0:
            break
       else:
        primelist.append(num)
print(primelist2)""")
primelist2 = []
lower = int(input("please enter the 'lower' or first value: "))
upper = int(input("please enter the 'upper' or last value: "))
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primelist2.append(num)
print("""After entering the values those codes will show prime number
list between """,
      lower, "and", upper, ''' numbers''')
print(primelist2)

print(''' But we can reduce the output time by setting range of the diviser to
square root of a number''')
primelist3 = []
lower2 = int(input("please enter the 'lower2' or first value: "))
upper2 = int(input("please enter the 'upper2' or last value: "))
for num in range(lower2, upper2 + 1):
    if num > 1:
        for i in range(2, int(num ** .5) + 1):
            if num % i == 0:
                break
        else:
            primelist3.append(num)
print("""After entering the values those codes will show prime number
list between """,
      lower2, "and", upper2, ''' numbers''')
print(primelist3)

print('''
cox=0
while cox<100:
      print(cox)
      cox=cox+2
''')
cox = 0
while cox < 100:
    print(cox)
    cox = cox + 2

print('''
#cox value is 98 now
cox=0  # chnage cox to 0 again
while cox<100:
 if cox==8:
    break
 print(cox)
 cox=cox+1
''')
# cox value is 98 now
cox = 0  # chnage cox to 0 again
while cox < 100:
    if cox == 8:
        break
    print(cox)
    cox = cox + 1

print('''
cox=0  # chnage cox to 0 again
while cox<100:
 if cox==8:
    break # will get out of the loop.
 else:
  pass # will not do anything for else statemrnt.
 print(cox)
 cox=cox+1 ''')

print('''
cox=0  # chnage cox to 0 again
while cox<100:
 if cox==8:
    break # will get out of the loop.
 else:
  pass # will not do anything for else statemrnt.
 print(cox)
 cox=cox+1
''')

cox = 0  # chnage cox to 0 again
while cox < 100:
    if cox == 8:
        break  # will get out of the loop.
    else:
        pass  # will not do anything for else statemrnt.
    print(cox)
    cox = cox + 1

    print('''
 for i in range (3,33):
    if i<15:
       continue # will ignore the values in the if statement.
    print(i) ''')

for i in range(3, 33):
    if i < 15:
        continue  # will ignore the values in the if statement.
    print(i)

print("Visit this  - https://www.guru99.com/python-break-continue-pass.html#:~:text=The%20main%20difference%20between%20break%20and%20continue%20statement,implemented%20later.%20Python%20pass%20is%20a%20null%20statement.")

'''
break, continue and pass in Python
Difficulty Level : Hard
Last Updated : 25 Nov, 2019
Using loops in Python automates and repeats the tasks in an efficient manner. But sometimes, there may arise a condition where you want to exit the loop completely, skip an iteration or ignore that condition. These can be done by loop control statements. Loop control statements change execution from its normal sequence. When execution leaves a scope, all automatic objects that were created in that scope are destroyed. Python supports the following control statements.

Break statement
Continue statement
Pass statement
Break statement
The break statement is used to terminate the loop or statement in which it is present. After that, the control will pass to the statements that are present after the break statement, if available. If the break statement is present in the nested loop, then it terminates only those loops which contains break statement.

Syntax:

break
python break statement

Example:
Consider a situation where you want to iterate over a string and want to print all the characters until a letter ‘e’ or ‘s’ is encountered. It is specified that you have to do this using loop and only one loop is allowed to use.
Here comes the usage of break statement. What we can do is iterate over a string using either a while loop or for loop and every time we have to compare the value of iterator with ‘e’ or ‘s’. If it is ‘e’ or ‘s’ we will use the break statement to exit the loop.



Below is the implementation.


# Python program to demonstrate
# break statement

# Python program to
# demonstrate break statement

s = 'geeksforgeeks'
# Using for loop
for letter in s:

    print(letter)
    # break the loop as soon it sees 'e'
    # or 's'
    if letter == 'e' or letter == 's':
        break

print("Out of for loop")
print()

i = 0

# Using while loop
while True:
    print(s[i])

    # break the loop as soon it sees 'e'
    # or 's'
    if s[i] == 'e' or s[i] == 's':
        break
    i += 1

print("Out of while loop")
Output:

g
e
Out of for loop

g
e
Out of while loop
Continue statement
Continue is also a loop control statement just like the break statement. continue statement is opposite to that of break statement, instead of terminating the loop, it forces to execute the next iteration of the loop.
As the name suggests the continue statement forces the loop to continue or execute the next iteration. When the continue statement is executed in the loop, the code inside the loop following the continue statement will be skipped and the next iteration of the loop will begin.

Syntax:

continue
python continue statement

Example:
Consider the situation when you need to write a program which prints the number from 1 to 10 and but not 6. It is specified that you have to do this using loop and only one loop is allowed to use.
Here comes the usage of continue statement. What we can do here is we can run a loop from 1 to 10 and every time we have to compare the value of iterator with 6. If it is equal to 6 we will use the continue statement to continue to next iteration without printing anything otherwise we will print the value.

Below is the implementation of the above idea:


# Python program to
# demonstrate continue
# statement

# loop from 1 to 10
for i in range(1, 11):

    # If i is equals to 6,
    # continue to next iteration
    # without printing
    if i == 6:
        continue
    else:
        # otherwise print the value
        # of i
        print(i, end = " ")
Output:



1 2 3 4 5 7 8 9 10
Pass statement
As the name suggests pass statement simply does nothing. The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute. It is like null operation, as nothing will happen is it is executed. Pass statement can also be used for writing empty loops. Pass is also used for empty control statement, function and classes.

Syntax:

pass
Example:


# Python program to demonstrate
# pass statement


s = "geeks"

# Empty loop
for i in s:
    # No error will be raised
    pass

# Empty function
def fun():
    pass

# No error will be raised
fun()

# Pass statement
for i in s:
    if i == 'k':
        print('Pass executed')
        pass
    print(i)
Output:

g
e
e
Pass executed
k
s


Python break, continue and pass Statements
Advertisements

 Previous PageNext Page
You might face a situation in which you need to exit a loop completely when an external condition is triggered or there may also be a situation when you want to skip a part of the loop and start next execution.

Python provides break and continue statements to handle such situations and to have good control on your loop.

This tutorial will discuss the break, continue and pass statements available in Python.

The break Statement:
The break statement in Python terminates the current loop and resumes execution at the next statement, just like the traditional break found in C.

The most common use for break is when some external condition is triggered requiring a hasty exit from a loop. The break statement can be used in both while and for loops.

Example:
#!/usr/bin/python

for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print 'Current Letter :', letter

var = 10                    # Second Example
while var > 0:
   print 'Current variable value :', var
   var = var -1
   if var == 5:
      break

print "Good bye!"
This will produce the following result:

Current Letter : P
Current Letter : y
Current Letter : t
Current variable value : 10
Current variable value : 9
Current variable value : 8
Current variable value : 7
Current variable value : 6
Good bye!
The continue Statement:
The continue statement in Python returns the control to the beginning of the while loop. The continue statement rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop.

The continue statement can be used in both while and for loops.

Example:
#!/usr/bin/python

for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print 'Current Letter :', letter

var = 10                    # Second Example
while var > 0:
   var = var -1
   if var == 5:
      continue
   print 'Current variable value :', var
print "Good bye!"
This will produce following result:

Current Letter : P
Current Letter : y
Current Letter : t
Current Letter : o
Current Letter : n
Current variable value : 10
Current variable value : 9
Current variable value : 8
Current variable value : 7
Current variable value : 6
Current variable value : 4
Current variable value : 3
Current variable value : 2
Current variable value : 1
Good bye!
The else Statement Used with Loops
Python supports to have an else statement associated with a loop statements.

If the else statement is used with a for loop, the else statement is executed when the loop has exhausted iterating the list.

If the else statement is used with a while loop, the else statement is executed when the condition becomes false.

Example:
The following example illustrates the combination of an else statement with a for statement that searches for prime numbers from 10 through 20.

#!/usr/bin/python

for num in range(10,20):  #to iterate between 10 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
         j=num/i #to calculate the second factor
         print '%d equals %d * %d' % (num,i,j)
         break #to move to the next number, the #first FOR
   else:        # else part of the loop
      print num, 'is a prime number'
This will produce following result:

10 equals 2 * 5
11 is a prime number
12 equals 2 * 6
13 is a prime number
14 equals 2 * 7
15 equals 3 * 5
16 equals 2 * 8
17 is a prime number
18 equals 2 * 9
19 is a prime number
Similar way you can use else statement with while loop.

The pass Statement:
The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.

The pass statement is a null operation; nothing happens when it executes. The pass is also useful in places where your code will eventually go, but has not been written yet (e.g., in stubs for example):

Example:
#!/usr/bin/python

for letter in 'Python':
   if letter == 'h':
      pass
      print 'This is pass block'
   print 'Current Letter :', letter

print "Good bye!"
This will produce following result:

Current Letter : P
Current Letter : y
Current Letter : t
This is pass block
Current Letter : h
Current Letter : o
Current Letter : n
Good bye!
The preceding code does not execute any statement or code if the value of letter is 'h'. The pass statement is helpful when you have created a code block but it is no longer required.

You can then remove the statements inside the block but let the block remain with a pass statement so that it doesn't interfere with other parts of the code.
'''


print("I")

print("I")
print("/")
print("I /")
print("I  /")
print("I   /")
print("   /")
print("  /  ")
print(" /    ")
print("/      ")
print("________  ")

print("""

     /\
    /  \
   /    \
  /______\___

     /
    /
   /
  /_________


 """)

print("""print absoloute value of a number
num1=-5
print(abs(num1))
""")
num1 = -5
print(abs(num1))

print("""give power to a value or a number
print(pow(3,2))
print(3**2)
""")
print(pow(3, 2))
print(3 ** 2)

print('''
print(max(4,7))

print(min(4,7))

print(round(4,7))
print(round(9,3))

print(round(4.7))
print(round(9.3))
print(round(9.6))
''')
print(max(4, 7))

print(min(4, 7))

print(round(4, 7))
print(round(9, 3))

print(round(4.7))
print(round(9.3))
print(round(9.6))

print(''' have to import from math modugle functions

from math import *

''')

from math import *

print('''
print(floor(4))
print(floor(9.0))

print(floor(4.7))
print(floor(9.3))
print(floor(9.6))

''')
print(floor(4))
print(floor(9.0))

print(floor(4.7))
print(floor(9.3))
print(floor(9.6))

print('''
print(ceil(4))
print(ceil(9.0))

print(ceil(4.7))
print(ceil(9.3))
print(ceil(9.6))

''')

print(ceil(4))
print(ceil(9.0))

print(ceil(4.7))
print(ceil(9.3))
print(ceil(9.6))

print('''
print(sqrt(4.7))

print(sqrt(9))

''')

print(sqrt(4.7))

print(sqrt(9))

print("""entered value inside input function will
always get out as string""")
print("""entered value inside input function will
always get out as string""")
codex = input('''     please input your code by typing
copy paste will not work till now     :


                 ''')

print("""entered value inside input function will
always get out as string""")
print("""entered value inside input function will
always get out as string""")
name = input('Please enter your anme:   ')
age = input(' Please enter your age:    ')
print(" Hello", name, "you are ", age)

print(codex)
print("The above code that you typed -  will give output")
exec(codex)

print("import command packages")
print("import turtle command drawing package, there are many pakages")

# -------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      user
#
# Created:     28/03/2019
# Copyright:   (c) user 2019
# Licence:     <your licence>
# -------------------------------------------------------------------------------

print("LISTS")
print("Working with LISTS")

print('''
lists=[], this is an epty list
''')
list = ["kevin", 5, 7.9, True]
# list values are indexed

friend = ["kevin", "KAren", "Jim", "Toddy", "Frog"]
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
friend[0] = "000"
print(friend[0])

print(''' update or modify list values
friend[0:1]= ["000", "ttt"]
print(friend[0:2])
=''')
friend[0:1] = ["000", "ttt"]
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
Items = ["car", "chair", "table", "mat"]
num = [8.8, 7.7, 9.9, 5.5, 25, 34, 35, 43, 45, 50, 52, 53, 55, 61, 70, 71, 77, 91, 92, 93, 99, 105, 115,
       122, 125, 133, 151, 155, 160, 170, 171, 177, 181, 192, 205, 250, 322, 331]
numbers = [4, 8, 15, 16, 23, 42]
FRINDS = ["kevin", "KAren", "Jim", "Toddy", "Frog", "Todd", "Jorge", "Lang"]
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

FRINDS.insert(1, "00000000000000")
# index       1, replace with this
print(FRINDS)
print('''

=''')
print('''
FRINDS.insert(7,Items*3)
print(FRINDS)
=''')
FRINDS.insert(7, Items * 3)
print(FRINDS)
print(''' remove one item
FRINDS.remove("00000000000000")
print(FRINDS)
=''')
FRINDS.remove("00000000000000")
print(FRINDS)

print(''' clear or remove last element\item of the list
FRINDS.pop()
print(FRINDS)
=''')
FRINDS.pop()
print(FRINDS)

print(''' find element , item of the list
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

FRINDS = ["You", "HE", "he", "WE", "we", "We", "wE"]
math = [3, 33, 4.4, 9.0, 9, .1, 0.1, 0, 0.0, .0, .00, 00, 00.00, 00.000, 0000]
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

print(''' reverse the list items
FRINDS.reverse()
math.reverse()
print(FRINDS)
print(math)
''')
FRINDS.reverse()
math.reverse()
print(FRINDS)
print(math)

print(''' copy the list items to another list
FRINDS3=math
FRINDS2=math.copy()
FRINDS3=math
print(FRINDS2)
print(FRINDS3)
''')

FRINDS3 = math
FRINDS2 = math.copy()
FRINDS3 = math
print(FRINDS2)
print(FRINDS3)

# Python Reference  https://www.w3schools.com/python/python_reference.asp

# Built in Functions and Import Statement
# Built in Functions and Import Statement
print(''' import math
print(math.pi)
print(math.sqrt(16))
print(math.isqrt(25)) ''')

import math
print(math.pi)
print(math.sqrt(16))

from math import isqrt

print(math.isqrt(25))

# Python Reference  https://www.w3schools.com/python/python_reference.asp
# https://www.w3schools.com/python/module_math.asp

print(''' 
# create a calculator.py file in the current folder. 

import calculator
print(calculator.add(3, 2))

print(calculator.divide(3, 2))

print(calculator.multiply(3, 2))
''')

# create a calculator.py file in the current folder.

import calculator
print(calculator.add(3, 2))

print(calculator.divide(3, 2))

print(calculator.multiply(3, 2))





#-----------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     29/03/2019
# Copyright:   (c) User 2019
# Licence:     <your licence>
#------------------------------------------------------------------------------

print(''' Create FUNCTIONS -
Create FUNCTIONS -
 #define the function by def ....:
def say_hi():
    #tell the function what to do
    print("Hello User")
#call the functio to do
say_hi()
''')


# define the function by def ....:
def say_hi():
    # tell the function what to do
    print("Hello User")


# call the functio to do
say_hi()

print('''
print(" Start")
say_hi()
print(" The End")
''')
print(" Start")
say_hi()
print(" The End")

print('''
#We can give parameters or information to functions
 #define the function by def ....:
def say_hi(name):
    #tell the function what to do
    print("Hello ", name)
#call the functio to do
say_hi("mike")
say_hi("DON")
''')


# We can give parameters or information to functions
# define the function by def ....:
def say_hi(name):
    # tell the function what to do
    print("Hello ", name)


# call the functio to do
say_hi("mike")
say_hi("DON")

print('''
#We can give parameters or information to functions
 #define the function by def ....:
def say_hi(name, age):
    #tell the function what to do
    print("Hello ", name, "you are" , str(age))
    #str() is to convert int or float to str#
#call the functio to do#
say_hi("mike", "33")
say_hi("DON", 55.5)
''')


# We can give parameters or information to functions
# define the function by def ....:
def say_hi(name, age):
    # tell the function what to do
    print("Hello ", name, "you are", str(age))
    # str() is to convert int or float to str#


# call the functio to do#
say_hi("mike", "33")
say_hi("DON", 55.5)

# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     29/03/2019
# Copyright:   (c) User 2019
# Licence:     <your licence>
# -------------------------------------------------------------------------------

print('''
def cube1(num):
    print(num*num*num)
cube1(3)
''')


def cube1(num):
    print(num * num * num)


cube1(3)
print('''
def cube2(num):
    return(num*num*num)
print(cube2(2))
''')


def cube2(num):
    return (num * num * num)


print(cube2(2))
print('''
def cube3(num):
    return num*num*num
print(cube3(2))
''')


def cube3(num):
    return num * num * num


print(cube3(2))
print('''
def cube4(num):
    return num*num*num
result=cube4(4)
print(result)
''')


def cube4(num):
    return num * num * num


result = cube4(4)
print(result)


#Classes and Objects
#Classes and Objects

#Creating Classes and Objects
#Creating Classes and Objects

'''
Python Classes/Objects
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

Create a Class
To create a class, use the keyword class:

Example
Create a class named MyClass, with a property named x:

class MyClass:
  x = 5
Create Object
Now we can use the class named MyClass to create objects:

Example
Create an object named p1, and print the value of x:

p1 = MyClass()
print(p1.x)
The __init__() Function
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

Example
Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
Note: The __init__() function is called automatically every time the class is being used to create a new object.

Object Methods
Objects can also contain methods. Methods in objects are functions that belong to the object.

Let us create a method in the Person class:

Example
Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

The self Parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

Example
Use the words mysillyobject and abc instead of self:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
Modify Object Properties
You can modify properties on objects like this:

Example
Set the age of p1 to 40:

p1.age = 40
Delete Object Properties
You can delete properties on objects by using the del keyword:

Example
Delete the age property from the p1 object:

del p1.age
Delete Objects
You can delete objects by using the del keyword:

Example
Delete the p1 object:

del p1
The pass Statement
class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

Example
class Person:
  pass
Test Yourself With Exercises
Exercise:
Create a class named MyClass:

class
 MyClass:
  x = 5
# def __str__(self) -> str:
'''


## Classes and Objects
## Classes and Objects
# Define a class

class Employ:
    pass
empt1 = Employ()
empt2 = Employ()

empt1.name = "TEst"
empt1.age = 45
empt1.pay = 70000

empt2.name = "TEst"
empt2.age = 45
empt2.pay = 70000

print(empt2.name)
print(empt2.age)


class Phone:
    def __init__(self, brand, price, version):  # this is a constructer # Properties
        self.brand = brand # instant variable or attributes
        self.price = price
        self.version = version
        #does not print anything
    def call (self, phone_number): # Behaviour # functionalities # functions # methods
        print(f"My phone is {self.brand} , the price is {self.price} and version is {self.version} calling {phone_number}")
        #it prints


iphone = Phone("Apple", 100000, 11)  # Objects # collections of properties and functions # instences
android = Phone("Samsung", 50000, 25) # Objects # instences have unique data

print(iphone)
print(android)

print(iphone.brand) #properties
print(iphone.price) #properties
print(iphone.version) #properties
iphone.call(999) # Behaviour
print(android.brand) #properties
print(android.price) #properties
print(android.version) #properties
android.call(123) # Behaviour


# Print Objects  # Print Objects

# Print Objects by overwriting
class Phone:
    def __init__(self, brand, price, version):  # this is a constructer
        self.brand = brand
        self.price = price
        self.version = version
        #does not print anything
    def call (self, phone_number): # Behaviour
        print(f"My phone is {self.brand} , the price is {self.price} and version is {self.version} calling {phone_number}")
        #it prints


    # press Ctrl+o to bring up the overwrite option bar
    def __str__(self) -> str:   # -> str return a string
        return f"My phone is {self.brand} , the price is {self.price} and version is {self.version}"


iphone = Phone("Apple", 100000, 11)  # Objects
android = Phone("Samsung", 50000, 25) # Objects

print(iphone)
print(android)

print(iphone.brand) #properties
print(iphone.price) #properties
print(iphone.version) #properties
iphone.call(999) # Behaviour
print(android.brand) #properties
print(android.price) #properties
print(android.version) #properties
android.call(123) # Behaviour



#########################################################################


#########################################################################
# date
#datetime

import datetime
print(datetime.datetime.now())
print(datetime.datetime.now().month)
print(datetime.datetime.now().year)
print(datetime.date.today())
print(datetime.datetime.now().time())
# datetime
# date

# formatting date
# formatting date
from datetime import datetime
from datetime import date

now = datetime.now()
print(now)

print(now.strftime("%d %m %Y %H %M %S"))  # char case matters
print(now.strftime("%d-%B-%Y %H.%M.%S")) # letter case matters
print(now.strftime('%d/%b/%Y %H:%M:%S'))



#################################################################
#################################################################
#################################################################

#Creating files
#Creating files

## Create a file
## Create a file
file = open("F:\Git_Clone_Files\python-learning-basics\data.csv", "r+")

#Write to a file and close it
#Write to a file and close it
file = open(".\data.csv", "r+")
file.write("name,id,email,address")
file.write("name,id,email,address\n")
file.write("jamal,01,jamal@email,jamaladd\n")
file.write("martin,03,martin@email,martinaddress\n")
file.close()
file = open(".\data.csv", "a") #append
file.write("jamal,01,jamal@email,jamaladd\n")
file.write("martin,03,martin@email,martinaddress\n")
file.close() # must close after work is done
# for writing only file = open("F:\Git_Clone_Files\python-learning-basics\data.csv", "w")

# readinr & writing


# Read from a file
# Read from a file

file = open(".\data.csv", "r")
#print(file.read())
#file.readline()   # all lines
print(file.readlines())
for line in file:
    print(line)
file.close()

#better way to work with files

#better way to work with files

import os.path

filename = "data.csv"

if os.path.isfile(filename):
    print("The file named ", filename, "exists")
    with open(".\data.csv", "r")as file:
        print(file.read())

else :
    print("The file named ", filename, "does not exists")

#Fetching Data From Internet
#Fetching Data From Internet

from urllib import request

r = request.urlopen("http://www.google.com")
print(request) #
# print(range) #
print(r)
print(r.getcode())
print(r.read())

from urllib import request

import json

# Request Module
import requests
# #- Pip & Modules
import pyttsx3
# Fetching Jokes From Internet
# Fetching Jokes From Internet
url = "https://official-joke-api.appspot.com/random_ten"

r = request.urlopen(url)
# print(r)
print(r.getcode())
# print(r.read())
data = r.read()
jsonData = json.loads(data)

#print(jsonData)


class Joke:

    def __init__(self, setup, punchline) -> None:
        self.setup = setup
        self.punchline = punchline

    def __str__(self) -> str:
        return f"setup {self.setup} punchline {self.punchline}"


jokes = []

for j in jsonData:
    setup = j["setup"]
    punchline = j["punchline"]
    joke = Joke(setup, punchline)
    jokes.append(joke)

print(f"Got {len(jokes)} jokes")

for joke in jokes:
    print(joke)
    pyttsx3.speak(joke.setup)
    pyttsx3.speak(joke.punchline)

# #- Pip & Modules








# Text To Speech













print('''
is_male = True

if is_male:
    print("Male")
''')
is_male = True

if is_male:
    print("Male")

print('''
is_male = False

if is_male:
    print("Male")
''')

print('''
is_male = False
if is_male:
    print("Male")
else:
    print(" Not Male")
''')

print('''
is_male = True
is_Tall = True

if is_male and is_male:
    print("Male")
elif is_male and not(is_Tall):
    print("male short")
elif not(is_male) and is_Tall:
    print("not male tall")
elif not(is_male) or is_Tall:
    print("not male or tall")
elif is_male or not(is_Tall):
    print("male or short")
else:
    print(" Not Male not tall")
''')
print('''
''')

is_male = True
is_Tall = True

if is_male and is_male:
    print("Male")
elif is_male and not (is_Tall):
    print("male short")
elif not (is_male) and is_Tall:
    print("not male tall")
elif not (is_male) or is_Tall:
    print("not male or tall")
elif is_male or not (is_Tall):
    print("male or short")
else:
    print(" Not Male not tall")

print('''
Comparisons
Comparisons =, <=, >=, <, >, !=
''')
print('''
Comparisons
Comparisons =, <=, >=, <, >, !=
''')
print('''
def max_num(n1, n2, n3):
    if n1>=n2 and n1>=n3:
        return n1
    elif n2>=n1 and n2>=n2:
        return n2
print(max_num(33,4,15))
''')
'''
Python 3 - Comparison Operators Example
Advertisements

 Previous PageNext Page
These operators compare the values on either side of them and decide the relation among them. They are also called Relational operators.

Assume variable a holds the value 10 and variable b holds the value 20, then −

Operator	Description	Example
==	If the values of two operands are equal, then the condition becomes true.	(a == b) is not true.
!=	If values of two operands are not equal, then condition becomes true.	(a!= b) is true.
>	If the value of left operand is greater than the value of right operand, then condition becomes true.	(a > b) is not true.
<	If the value of left operand is less than the value of right operand, then condition becomes true.	(a < b) is true.
>=	If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.	(a >= b) is not true.
<=	If the value of left operand is less than or equal to the value of right operand, then condition becomes true.	(a <= b) is true.
Example
Assume variable a holds the value 10 and variable b holds the value 20, then −

Live Demo
#!/usr/bin/python3

a = 21
b = 10

if ( a == b ):
   print ("Line 1 - a is equal to b")
else:
   print ("Line 1 - a is not equal to b")

if ( a != b ):
   print ("Line 2 - a is not equal to b")
else:
   print ("Line 2 - a is equal to b")

if ( a < b ):
   print ("Line 3 - a is less than b" )
else:
   print ("Line 3 - a is not less than b")

if ( a > b ):
   print ("Line 4 - a is greater than b")
else:
   print ("Line 4 - a is not greater than b")

a,b = b,a #values of a and b swapped. a becomes 10, b becomes 21

if ( a <= b ):
   print ("Line 5 - a is either less than or equal to  b")
else:
   print ("Line 5 - a is neither less than nor equal to  b")

if ( b >= a ):
   print ("Line 6 - b is either greater than  or equal to b")
else:
   print ("Line 6 - b is neither greater than  nor equal to b")
Output
When you execute the above program, it produces the following result −

Line 1 - a is not equal to b
Line 2 - a is not equal to b
Line 3 - a is not less than b
Line 4 - a is greater than b
Line 5 - a is either less than or equal to  b
Line 6 - b is either greater than  or equal to b
'''

'''

'''


def max_num(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n2:
        return n2


print(max_num(33, 4, 15))

print('''
a1=float(input("Enter the first number:    "))
op=input("Enter the operator or sign :          ")
b1=float(input("Enter the second number:    "))

if op=="+":
    print(str(a1),"+", str(b1), "=", a1+b1 )
elif op=="-":
     print(str(a1),"-", str(b1), "=", a1-b1 )
elif op=="/":
     print(str(a1),"/", str(b1), "=", a1/b1 )
elif op=="*":
     print(str(a1),"*", str(b1), "=", a1*b1 )
elif op=="**":
     print(str(a1),"**", str(b1), "=", a1**b1 )
elif op=="//":
     print(str(a1),"//", str(b1), "=", a1//b1 )
elif op=="%":
     print(str(a1),"%", str(b1), "=", a1%b1 )
else:
    print("invalid operator or number")
''')
'''
What are Logical Operators in Python?
Logical Operators in Python are used to perform logical operations on the values of variables. The value is either true or false. We can figure out the conditions by the result of the truth values. There are mainly three types of logical operators in python : logical AND, logical OR and logical NOT. Operators are represented by keywords or special characters.

In this tutorial, we going to learn various operators

Arithmetic Operators
Comparison Operators
Python Assignment Operators
Logical Operators or Bitwise Operators
Membership Operators
Identity Operators
Operator precedence
Arithmetic Operators
Arithmetic Operators perform various arithmetic calculations like addition, subtraction, multiplication, division, %modulus, exponent, etc. There are various methods for arithmetic calculation in Python like you can use the eval function, declare variable & calculate, or call functions.

Example: For arithmetic operators we will take simple example of addition where we will add two-digit 4+5=9

x= 4
y= 5
print(x + y)
Similarly, you can use other arithmetic operators like for multiplication(*), division (/), substraction (-), etc.

Comparison Operators
Comparison Operators In Python compares the values on either side of the operand and determines the relation between them. It is also referred to as relational operators. Various comparison operators in python are ( ==, != , <>, >,<=, etc.)

Example: For comparison operators we will compare the value of x to the value of y and print the result in true or false. Here in example, our value of x = 4 which is smaller than y = 5, so when we print the value as x>y, it actually compares the value of x to y and since it is not correct, it returns false.

x = 4
y = 5
print(('x > y  is',x>y))
Likewise, you can try other comparison operators (x < y, x==y, x!=y, etc.)

Python Assignment Operators
Assignment Operators in Python are used for assigning the value of the right operand to the left operand. Various assignment operators used in Python are (+=, - = , *=, /= , etc.).

Example: Python assignment operators is simply to assign the value, for example

num1 = 4
num2 = 5
print(("Line 1 - Value of num1 : ", num1))
print(("Line 2 - Value of num2 : ", num2))
Example of compound assignment operator

We can also use a compound assignment operator, where you can add, subtract, multiply right operand to left and assign addition (or any other arithmetic function) to the left operand.

Step 1: Assign value to num1 and num2
Step 2: Add value of num1 and num2 (4+5=9)
Step 3: To this result add num1 to the output of Step 2 ( 9+4)
Step 4: It will print the final result as 13
num1 = 4
num2 = 5
res = num1 + num2
res += num1
print(("Line 1 - Result of + is ", res))
Logical Operators or Bitwise Operators
Logical operators in Python are used for conditional statements are true or false. Logical operators in Python are AND, OR and NOT. For logical operators following condition are applied.

For AND operator – It returns TRUE if both the operands (right side and left side) are true
For OR operator- It returns TRUE if either of the operand (right side or left side) is true
For NOT operator- returns TRUE if operand is false
Example: Here in example we get true or false based on the value of a and b

a = True
b = False
print(('a and b is',a and b))
print(('a or b is',a or b))
print(('not a is',not a))
Membership Operators
These operators test for membership in a sequence such as lists, strings or tuples. There are two membership operators that are used in Python. (in, not in). It gives the result based on the variable present in specified sequence or string

Example: For example here we check whether the value of x=4 and value of y=8 is available in list or not, by using in and not in operators.

x = 4
y = 8
list = [1, 2, 3, 4, 5 ];
if ( x in list ):
   print("Line 1 - x is available in the given list")
else:
   print("Line 1 - x is not available in the given list")
if ( y not in list ):
   print("Line 2 - y is not available in the given list")
else:
   print("Line 2 - y is available in the given list")
Declare the value for x and y
Declare the value of list
Use the "in" operator in code with if statement to check the value of x existing in the list and print the result accordingly
Use the "not in" operator in code with if statement to check the value of y exist in the list and print the result accordingly
Run the code- When the code run it gives the desired output
Identity Operators
Identity Operators in Python are used to compare the memory location of two objects. The two identity operators used in Python are (is, is not).

Operator is: It returns true if two variables point the same object and false otherwise
Operator is not: It returns false if two variables point the same object and true otherwise
Following operands are in decreasing order of precedence.

Operators in the same box evaluate left to right

Operators (Decreasing order of precedence)	Meaning
**	Exponent
*, /, //, %	Multiplication, Division, Floor division, Modulus
+, -	Addition, Subtraction
<= < > >=	Comparison operators
= %= /= //= -= += *= **=	Assignment Operators
is is not	Identity operators
in not in	Membership operators
not or and	Logical operators
Example:

x = 20
y = 20
if ( x is y ):
	print("x & y  SAME identity")
y=30
if ( x is not y ):
	print("x & y have DIFFERENT identity")
Declare the value for variable x and y
Use the operator "is" in code to check if value of x is same as y
Next we use the operator "is not" in code if value of x is not same as y
Run the code- The output of the result is as expected
Operator precedence
The operator precedence determines which operators need to be evaluated first. To avoid ambiguity in values, precedence operators are necessary. Just like in normal multiplication method, multiplication has a higher precedence than addition. For example in 3+ 4*5, the answer is 23, to change the order of precedence we use a parentheses (3+4)*5, now the answer is 35. Precedence operator used in Python are (unary + - ~, **, * / %, + - , &) etc.

v = 4
w = 5
x = 8
y = 2
z = 0
z = (v+w) * x / y;
print("Value of (v+w) * x/ y is ",  z)
Declare the value of variable v,w…z
Now apply the formula and run the code
The code will execute and calculate the variable with higher precedence and will give the output
Python 2 Example
Above examples are Python 3 codes, if you want to use Python 2, please consider following codes

#Arithmetic Operators
x= 4
y= 5
print x + y

#Comparison Operators
x = 4
y = 5
print('x > y  is',x>y)

#Assignment Operators
num1 = 4
num2 = 5
print ("Line 1 - Value of num1 : ", num1)
print ("Line 2 - Value of num2 : ", num2)

#compound assignment operator
num1 = 4
num2 = 5
res = num1 + num2
res += num1
print ("Line 1 - Result of + is ", res)

#Logical Operators
a = True
b = False
print('a and b is',a and b)
print('a or b is',a or b)
print('not a is',not a)

#Membership Operators
x = 4
y = 8
list = [1, 2, 3, 4, 5 ];
if ( x in list ):
   print "Line 1 - x is available in the given list"
else:
   print "Line 1 - x is not available in the given list"
if ( y not in list ):
   print "Line 2 - y is not available in the given list"
else:
   print "Line 2 - y is available in the given list"

#Identity Operators
x = 20
y = 20
if ( x is y ):
	print "x & y  SAME identity"
y=30
if ( x is not y ):
	print "x & y have DIFFERENT identity"

#Operator precedence
v = 4
w = 5
x = 8
y = 2
z = 0
z = (v+w) * x / y;
print "Value of (v+w) * x/ y is ",  z
Summary:
Operators in a programming language are used to perform various operations on values and variables. In Python, you can use operators like

There are various methods for arithmetic calculation in Python as you can use the eval function, declare variable & calculate, or call functions
Comparison operators often referred as relational operators are used to compare the values on either side of them and determine the relation between them
Python assignment operators are simply to assign the value to variable
Python also allows you to use a compound assignment operator, in a complicated arithmetic calculation, where you can assign the result of one operand to the other
For AND operator – It returns TRUE if both the operands (right side and left side) are true
For OR operator- It returns TRUE if either of the operand (right side or left side) is true
For NOT operator- returns TRUE if operand is false
There are two membership operators that are used in Python. (in, not in).
It gives the result based on the variable present in specified sequence or string
The two identify operators used in Python are (is, is not)
It returns true if two variables point the same object and false otherwise
Precedence operator can be useful when you have to set priority for which calculation need to be done first in a complex calculation.

=============================================================================

Python Logical Operators
Logical operators are used to combine conditional statements:

Operator	Description	Example	Try it
and 	Returns True if both statements are true	x < 5 and  x < 10
or	Returns True if one of the statements is true	x < 5 or x < 4
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)


Python 3 – Logical Operators
Last Updated : 10 Jul, 2020
Logical Operators are used to perform certain logical operations on values and variables. These are the special reserved keywords that carry out some logical computations. The value the operator operates on is known as Operand. In Python, they are used on conditional statements (either True or False), and as a result, they return boolean only (True or False). They are used to combine conditional statements

There are following logical operators supported by Python language:

Logical AND
Logical OR
Logical NOT
Logical AND
Logical operator AND returns True only if both the operands are True else it returns False. It is a binary operator, which means to return some value, it has to be operated between two operators (i.e, two operators are required)

Truth Table:

Operator A	Operator B	Logical AND result
True	True	True
True	False	False
False	True	False
False	False	False
Example 1:





a = 12
b = 26
c = 4

if a > b and a > c:
    print("Number a is larger")

if b > a and b > c:
    print("Number b is larger")

if c > a and c > b:
    print("Number c is larger")
Output:

Number b is larger
Example 2:


a = 10

if (a == 0 and "Hello"):
    print("a has value zero(0)")
else:
    print("a is not equal to zero")
Output:

a is not equal to zero
If the first expression evaluated to be false while using and operator, then further expressions are not evaluated. Also, any string is always considered a true statement. In the above example, the first condition is false and hence it will not check the second condition and hence, it will not check for another condition and it will go to else statement.

Logical OR
The logical operator OR returns False only if both the operands are False else it returns True. It is a binary operator, which means to return some value, it has to be operated between two operators (i.e, two operators are required)

Truth Table:

Operator A	Operator B	Logical OR Result
True	True	True
True	False	True
False	True	True
False	False	False
Example 1:


a = 10
b = -5

if a < 0 or b < 0:
  print("Their product will be negative")
else:
  print("Their product will be positive")
Output:



Their product will be negative
Example 2:


a = 10

if (a == 0 or "GeeksForGeeks"):
  print("Is Awesome")
else:
  ("Try Again!")
Output:

Is Awesome
Here, in the OR Logical operator, even if the first expression evaluated is false while using and operator, then also the further expressions are evaluated. Also, any string is always considered a true statement. In the above example, the first statement is false but then too, it will evaluate the second statement because it returns False only if both the operands are False and since the string is considered as True statement, thus, it will be evaluated and the below print statement will be printed.

Logical NOT
Logical NOT operator works with the single boolean value and returns the value as True if the boolean value is False and vice-versa (that is the opposite of it).  It is a unary operator, which means to return some value, it has to be operated on one operator only. (i.e, only operator is required)

Truth Table:

Operator A	Logical NOT Result
True	False
False	True
Example 1:


a = 10

if not a == 10:
  print ("a not equals 10")
else:
  print("a equals 10")
Output:

a equals 10
Here, a is equal to 10 the boolean a == 10 return the value True. Hence, the boolean not a == 10 will return the value as False and since the if condition is not satisfied, it will jump to else statement.

Example 2:


a = 10

if not a%5 == 0:
  print("a is not perfectly divisible by 5")
else:
  print("a is perfectly divisible by 5")
Output:

a is perfectly divisible by 5

'''
print("(num /=2) == (num = num/2)")
print("(num +=1) == (num = num+1)")
print("(num -+1) == (num = num-1)")
print("(num *= 3) == (num = num * 3)")
print("(num **= 2) == (num = num ** 2)")

# (num +=1) == (num = num+1)

# (num -+1) == (num = num-1)

# (num *= 3) == (num = num * 3)

# (num /=2) == (num = num/2)



# if statement calculator # if statement
# if statement # Calculator if statement





a1 = float(input("Enter the first number:    "))
op = input("Enter the operator or sign :          ")
b1 = float(input("Enter the second number:    "))



if op == "+":
    print(str(a1), "+", str(b1), "=", a1 + b1)
elif op == "-":
    print(str(a1), "-", str(b1), "=", a1 - b1)
elif op == "/":
    print(str(a1), "/", str(b1), "=", a1 / b1)
elif op == "*":
    print(str(a1), "*", str(b1), "=", a1 * b1)
elif op == "**":
    print(str(a1), "**", str(b1), "=", a1 ** b1)
elif op == "//":
    print(str(a1), "//", str(b1), "=", a1 // b1)
elif op == "%":
    print(str(a1), "%", str(b1), "=", a1 % b1)
else:
    print("invalid operator or number")

print('''
print(eval(input()))
''')
print(eval(input()))

print('''
op=input( """please input a calculating or math operetion:
like 12+14 or 14*30 or 34//22 etc
                  """ )
print(eval(op))
''')

op = input("""please input a calculating or math operetion:
like 12+14 or 14*30 or 34//22 etc
                  """)
print(eval(op))

print('''

''')
# if statement calculator # if statement
# if statement # Calculator if statement




print("""
codex=input('''     please input your code by typing
copy paste will not work till now     :
 ''')


                 """)
codex = input('''     please input your code by typing
copy paste will not work till now     :


                 ''')
print("""
print(codex)
print("The above code that you typed -  will give output")
exec(codex)
""")
print(codex)
print("The above code that you typed -  will give output")
exec(codex)

print("While loop")
print("""
i=1
while i<=10:
      print(i)
      i+=1
print("end")
""")
i = 1
while i <= 10:
    print(i)
    i += 1

# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     30/03/2019
# Copyright:   (c) User 2019
# Licence:     <your licence>
# -------------------------------------------------------------------------------

print('''
secret_word="girrafe"
guess=""

while guess!= secret_word:
      guess=input("""Enter guess, Guessing game1.11""")
print("you win")
''')
print("Guessing game 1")
print("Guessing game 1.11")

secret_word = "girrafe"
guess = ""

while guess != secret_word:
    guess = input("""Enter guess, Guessing game1.11""")
print("you win")

print("Guessing game 1.22")
print("Guessing game 1.22")

print('''
esc = False
secret_word="girrafe"
guess=""
win=False
while guess!= secret_word and not(esc):
      if guess!="e":
         guess=input("""Enter guess, Guessing game1.22 or
         enter e to exit:       """)
      else:
        esc=True
if esc:
   print("You exit")
else:
     print("you win")
''')
esc = False
secret_word = "girrafe"
guess = ""
while guess != secret_word and not (esc):
    if guess != "e":
        guess = input("""Enter guess, Guessing game1.22 or
         enter e to exit:       """)
    else:
        esc = True
if esc:
    print("You exit")
else:
    print("you win")

print("Guessing game 2")
print("Guessing game 2.1")

print('''

secret_word="girrafe2"
guess=""
guess_count=0
out_of_guesses=False
guess_limit=3
while guess!= secret_word and not(out_of_guesses):
      if guess_count< guess_limit:
        guess=input("Enter guess, for guessing game 2.1, maximum 3 times:   ")
        guess_count+=1
      else:
         out_of_guesses=True

if out_of_guesses:
   print("you lose")
else:
 print("you win")
''')

secret_word = "girrafe2"
guess = ""
guess_count = 0
out_of_guesses = False
guess_limit = 3
while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess, for guessing game 2.1, maximum 3 times:   ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("you lose")
else:
    print("you win")

# +++++++++++++++++++++++++++++++++++++++++++++++++++
print('''
fr=["jim", "Ken", "Lom"]

for fr in fr:
    print(fr)
print(" \n ")
print(fr)
''')
fr = ["jim", "Ken", "Lom"]

for fr in fr:
    print(fr)

print(" \n ")

print(fr)

print(" \n ")
print('''
fr=["jim", "Ken", "Lom"]
for n in fr:
    print(n)
''')

fr = ["jim", "Ken", "Lom"]
for n in fr:
    print(n)

print(''' to print out all the members-
fr=["jim", "Ken", "Lom"]
for index in range(len(fr)):
    print(fr[index])
''')
fr = ["jim", "Ken", "Lom"]
for index in range(len(fr)):
    print(fr[index])

print('''
fr=["jim", "Ken", "Lom"]
for index in range(5):
    if index==0:
       print("first one")
    else:
         print("not 1st")

''')
fr = ["jim", "Ken", "Lom"]
for index in range(5):
    if index == 0:
        print("first one")
    else:
        print("not 1st")

print('''
Exponent code
Exponent code
''')
print('''
def answer2(number, power):
    result=1
    for index in range(power):
        result=result * number
    return result
print(answer2(3,2))
''')
print('''

''')


def answer2(number, power):
    result = 1
    for index in range(power):
        result = result * number
    return result


print(answer2(3, 2))

print('''
2D Lists and Nested Loops
2D Lists and Nested Loops
matrix_grid=[
[1,2,3],
[4,5,6],
[7,8,9],
[0]
]
''')
matrix_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print('''
print(matrix_grid[0][0])
print(matrix_grid[2][1])
''')
print(matrix_grid[0][0])
print(matrix_grid[2][1])
print('''
for row in matrix_grid:
    print(row)
''')
for row in matrix_grid:
    print(row)

print('''
for r in matrix_grid:
    print(r)
''')
for r in matrix_grid:
    print(r)

print('''
for r in matrix_grid:
    for c in r:
        print(c)
''')

for r in matrix_grid:
    for c in r:
        print(c)

# translationcode.py

print('''
Basic translator in python
''')
print('''
Basic translator in python
''')

print('''
evry vowel in the phrase will become g
like example, gog will ggg, dog will be dgg, bag will be bgg, etc
''')

print('''
Basic translator in python v 1.11
''')
print('''
Basic translator in python v 1.11
''')

print('''
def translation(words):
 translation=""
 for letter in words:
    if letter in "AEIOUaeiou":
        translation= translation + "g"
    else:
         translation= translation + letter
 return translation
print(translation(input("please input word/s:   " )))

''')


def translation(words):
    translation = ""
    for letter in words:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translation(input("please input word/s:   ")))

print('''
Basic translator in python v 1.22
''')
print('''
Basic translator in python v 1.22

def translation(words):
 translation=""
 for letter in words:
    if letter.lower() in "aeiou":
       if letter.isupper():
          translation= translation + "G"
       else:
         translation= translation + "g"
    else:
         translation= translation + letter
 return translation
words=input("please input word/s:   " )
print("you entered - ", words)
print( " The translation is " , translation(words))
''')


def translation(words):
    translation = ""
    for letter in words:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


words = input("please input word/s:   ")
print("you entered - ", words)
print(" The translation is ", translation(words))

'''print('''
''')'''

print("vol 1.11")
try:
    num = int(input("Please enter a number:  "))
    print(num)
except:  # this will catch ay error
    print("Invalid input")

print("vol 1.22")
# value=10/0
print(" this will show zero division error")
try:
    num = int(input("Please enter a number:  "))
    print(num)
except:
    print("Invalid input")

print("vol 1.33")

try:
    value = 10 / 0
    print(''' this will also catch error of value=10/0,
    and print invalid iputwhich is unwanted.''')
    num = int(input("Please enter a number:  "))
    print(num)
except:

    print("Invalid input")

print("vol 2.00")

try:
    value = 10 / 0
    print(''' this will also catch error of value=10/0,
    and print invalid iputwhich is unwanted.''')
    num = int(input("Please enter a number:  "))
    print(num)
except ZeroDivisionError:
    print("division by zero")
except ValueError:
    print("Invalid input")

try:
    value = 10 / 0
    print(''' this will also catch error of value=10/0,
    and print invalid iputwhich is unwanted.''')
    num = int(input("Please enter a number:  "))
    print(num)
except ZeroDivisionError as err:
    print("err")  # to print the actual error.
    print("division by zero")
except ValueError:
    print("Invalid input")

print('''
''')

print('''
''')

print('''[
Python String | replace()
replace() is an inbuilt function in Python programming language
 that returns a copy of the string where all occurrences of a
 substring is replaced with another substring.

Syntax :

string.replace(old, new, count)
Parameters :





old – old substring you want to replace.
new – new substring which would replace the old substring.

count – the number of times you want to replace the old substring with
the new substring. (Optional )

Return Value :
It returns a copy of the string where all occurrences of a substring
 is replaced with another substring.

Below is the code demonstrating replace() :

filter_none
edit
play_arrow

brightness_4
# Python3 program to demonstrate the
# use of replace() method

string = "geeks for geeks geeks geeks geeks"

# Prints the string by replacing geeks by Geeks
print(string.replace("geeks", "Geeks"))

# Prints the string by replacing only 3 occurence of Geeks
print(string.replace("geeks", "GeeksforGeeks", 3))
Output :

Geeks for Geeks Geeks Geeks Geeks
GeeksforGeeks for GeeksforGeeks GeeksforGeeks geeks geeks]

''')


def say_hi(name, age):
    print("Hellow", name, "you are ", age)


say_hi("mike", 30)
say_hi("hall", "50")

print('''
def say_hi(name , age):
    print("Hellow", name , "you are " ,  age )


say_hi("mike" , 30)
say_hi("hall" , "50")
''')

print('''
''')

print('''
''')

print("end")

print('''
''')

print('''
''')

print('''
''')

import turtle

tut = turtle.pen()
tut = turtle.forward(200)
tut = turtle.left(200)
tut = turtle.forward(20)
tut = turtle.left(20)
tut = turtle.forward(120)
tut = turtle.right(20)
tut = turtle.forward(120)
tut = turtle.left(20)
tut = turtle.forward(120)
tut = turtle.right(20)
tut = turtle.forward(120)
tut = turtle.right(20)
tut = turtle.back(120)
tut = exit()
exit()

print("""     The End The End The End

                       The End ?   """)

print("""     The End The End The End

                       The End ?   """)

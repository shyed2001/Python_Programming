Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("start at home 04-03-2019========================")
start at home 04-03-2019========================
>>> print(3**2)
9
>>> print(3.0**2)
9.0
>>> 
>>> 
KeyboardInterrupt
>>> print((3**2)+ "=" + str(3**2))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print((3**2)+ "=" + str(3**2))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print("(3**2)"+ "=" + str(3**2))
(3**2)=9
>>> rint("(3.0**2)"+ "=" + str(3.0**2))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    rint("(3.0**2)"+ "=" + str(3.0**2))
NameError: name 'rint' is not defined
>>> print("(3.0**2)"+ "=" + str(3.0**2))
(3.0**2)=9.0
>>> rint("(3.0**2.0)"+ "=" + str(3.0**2.0))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    rint("(3.0**2.0)"+ "=" + str(3.0**2.0))
NameError: name 'rint' is not defined
>>> print("(3.0**2)"+ "=" + str(3.0**2))
(3.0**2)=9.0
>>> print("(3.0**2.0)"+ "=" + str(3.0**2.0))
(3.0**2.0)=9.0
>>> print("('OK'** 2)"+ "=" + str('OK" ** 2))
				  
SyntaxError: EOL while scanning string literal
>>> print("(OK ** 2)"+ "=" + str("OK" ** 2))
				  
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print("(OK ** 2)"+ "=" + str("OK" ** 2))
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> print("(OK * 2)"+ "=" + str("OK" * 2))
				  
(OK * 2)=OKOK
>>> print("(OK * 2 )"+ "=" + ("OK" * 2))
				  
(OK * 2 )=OKOK
>>> print("(OK * 2.0 )"+ "=" + ("Error"))
				  
(OK * 2.0 )=Error
>>> print("(OK * 2 )"+ "=" + ("OK" * 2.0))
				  
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print("(OK * 2 )"+ "=" + ("OK" * 2.0))
TypeError: can't multiply sequence by non-int of type 'float'
>>> print(("(\"Fun\" * 0)")+ "=" + str(("Fun" * 0)))
				  
("Fun" * 0)=
>>> print(("(\"9\" * 0)")+ "=" + str("9" * 0))
				  
("9" * 0)=
>>> float(input("Enter a number:   ")) + float(input(Enter a number:   "))
						     
SyntaxError: invalid syntax
>>> float(input("Enter a number:   ")) + float(input(Enter a number:   "))
						     
SyntaxError: invalid syntax
>>> float(input("Enter a number:   ")) + float(input("Enter a number:   "))
						     
Enter a number:   70
Enter a number:   50
120.0
>>> float(input("Enter a number:   ")) + float(input(Enter a number:   "))
						     
SyntaxError: invalid syntax
>>> float(input("Enter a number:   ")) + float(input("Enter a number:   "))
						     
Enter a number:   6.0
Enter a number:   77.0
83.0
>>> print(float(input("Enter a number:   ")) + float(input("Enter a number:   ")))
						     
Enter a number:   9.0
Enter a number:   5
14.0
>>> float("210" * int(input("Enter a number:  ")))
						     
Enter a number:  3
210210210.0
>>> float("210" * int(input("Enter a number:  ")))
						     
Enter a number:  5.0
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    float("210" * int(input("Enter a number:  ")))
ValueError: invalid literal for int() with base 10: '5.0'
>>> float("210" * int(input("Enter a intiger number :  ")))
						     
Enter a intiger number :  7
2.1021021021021022e+20
>>> float("210" * int(input("Enter a intiger number :  ")))
						     
Enter a intiger number :  y
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    float("210" * int(input("Enter a intiger number :  ")))
ValueError: invalid literal for int() with base 10: 'y'
>>> print("Variables")
						     
Variables
>>> x=7
print(X)
						     
SyntaxError: multiple statements found while compiling a single statement
>>> x=7
						     
>>> print(X)
						     
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined
>>> x = 7
						     
>>> print(x)
						     
7
>>> print(X) + print(X)
						     
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print(X) + print(X)
NameError: name 'X' is not defined
>>> x =7
						     
>>> print(X) + print(X)
						     
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(X) + print(X)
NameError: name 'X' is not defined
>>> x = 7
						     
>>> print(X) + print(X)
						     
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print(X) + print(X)
NameError: name 'X' is not defined
>>> x=7
						     
>>> print(X)
						     
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined
>>> x =7
						     
>>> print(X)
						     
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined
>>> x = 7
						     
>>> print(X)
						     
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined
>>> x = 7
						     
>>> print(x)
						     
7
>>> x =7
						     
>>> print(x)
						     
7
>>> x=7
						     
>>> print(x)
						     
7
>>> x=7
						     
>>> print(x+5)
						     
12
>>> x=3
						     
>>> y=4
						     
>>> z=5
						     
>>> print(x+y+z)
						     
12
>>> x= "This is a string"
						     
>>> print(x + "!")
						     
This is a string!
>>> x= This is a string
						     
SyntaxError: invalid syntax
>>> print("x" + "!")
						     
x!
>>> x= "This is a string"
						     
>>> print("x" + "!")
						     
x!
>>> x= "This is a string"
						     
>>> print('x' + "!")
						     
x!
>>> print(x + "!")
						     
This is a string!
>>> lastname=3
						     
>>> Lastname=4
						     
>>> print(lastname + Lastname)
						     
7
>>> foo=input("Pleae the value of foo:  ")
						     
Pleae the value of foo:  r
>>> 
						     
>>> foo=input("Pleae the value of foo:  ")
						     
Pleae the value of foo:  5
>>> print(foo)
						     
5
>>> foo=input("Pleae the value of foo:  ")
						     
Pleae the value of foo:  t
>>> print(foo)
						     
t
>>> print("foo")
						     
foo
>>> print("in place operators")
						     
in place operators
>>> 

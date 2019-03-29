Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("File name is - py Allin.py")
File name is - py Allin.py
>>> 
print("Hallow  world")
Hallow  world
>>> print("Mathematical operator order is - BEDMAS")


Mathematical operator order is - BEDMAS
>>> print("BEDMAS" "=" "Brackets, Exponents, Division, Multiplication, Addition, Subtraction")
BEDMAS=Brackets, Exponents, Division, Multiplication, Addition, Subtraction
>>> 
>>> print(“(2+(3-1))”+ "=" + str(2+(3-1)))
SyntaxError: invalid character in identifier
>>> print("(2+(3-1))"+ "=" + str(2+(3-1)))
(2+(3-1))=4
>>> print(("9/3")+ "=" + str(9/3))
9/3=3.0
>>> print(("9/3.0")+ "=" + str(9/3.0))
9/3.0=3.0
>>> print(("9.0/3")+ "=" + str(9.0/3))
9.0/3=3.0
>>> print(("9.0*3")+ "=" + str(9.0*3))
9.0*3=27.0
>>> print(("9*3")+ "=" + str(9*3))
9*3=27
>>> rint(("9*3.0")+ "=" + str(9*3.03))
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    rint(("9*3.0")+ "=" + str(9*3.03))
NameError: name 'rint' is not defined
>>> print(("9*3.0")+ "=" + str(9*3.0))
9*3.0=27.0
>>> print(("((9-1+2)+(9/3*3))")+ "=" + str((9-1+2)+(9/3*3)))
((9-1+2)+(9/3*3))=19.0
>>> print(("(((-9)-1+2)+(9/3*(-3)))")+ "=" + str(((-9)-1+2)+(9/3*(-3))))
(((-9)-1+2)+(9/3*(-3)))=-17.0
>>> print((-9)*(-3))
27
>>> print(("-9/-3")+ "=" + str(-9/-3))
-9/-3=3.0
>>> print(("(-9)/(-3)")+ "=" + str((-9)/(-3)))
(-9)/(-3)=3.0
>>> print(("-9*-3")+ "=" + str(-9*-3))
-9*-3=27
>>> print(("(-9)*(-3)")+ "=" + str((-9)*(-3)))
(-9)*(-3)=27
>>> 

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

num1=input('Please enter a number:   ')
num2=input('Please enter another number:   ')
result=float(num1)+float(num2)
print(result)


print("""Mathematical operator order is - BEDMAS
or PEDMAS""")

print("""print("BEDMAS" "=") will show  , ("BEDMAS" "=") """)
print("BEDMAS" "=" """"Brackets, Exponents, Division,
 Multiplication, Addition, Subtraction""")

print("""PEDMAS = Parenthecis (), Exponents **, Division /,
 Multiplication *, Addition + , Subtraction - """)

print("""left to right or left associative rule
 for * / - + operators""")
print(("print(6-3+2) =") + str(6-3+2))
print(("print(6-3+2) =") + str(6-3+2))

print(("print(6-3+2) =") + str(6-3+2))

print(("print(6/3*2) =") + str(6/3*2))
print("left to right or left associative rule for * / - + operators")
#----------------------
print("but for ** right to left or right associative rule for * / - + operators")
print(("print(2**3**2) =") + str(2**3**2))


print(("2+3")+ "=" + str(2+3))

print(2+(3-1))
print("(2+(3-1))"+ "=" + str(2+(3-1)))

print(9/3)
print(("9/3")+ "=" + str(9/3))
print(9/3.0)
print(("9/3.0")+ "=" + str(9/3.0))
print(9.0/3)
print(("9.0/3")+ "=" + str(9.0/3))

print(9*3)
print(("9*3")+ "=" + str(9*3))
print(9.0*3)

print(9*3.0)
print(("9*3.0")+ "=" + str(9*3.0))

print((9-1+2)+(9/3*3))
print(("((9-1+2)+(9/3*3))")+ "=" + str((9-1+2)+(9/3*3)))
print(("(((-9)-1+2)+(9/3*(-3)))")+ "=" + str(((-9)-1+2)+(9/3*(-3))))

print((-9)*(-3))
print(("(-9)*(-3)")+ "=" + str((-9)*(-3)))
print(("(-9)/(-3)")+ "=" + str((-9)/(-3)))
print(("-9/-3")+ "=" + str(-9/-3))
print(("-9*-3")+ "=" + str(-9*-3))

print("idleAllin2.py")
print("================03-03-2019=====================04-03-2019=========\n==========================\n=====================")
print(("10/3")+ "=" + str(10/3))

print(("-10/3")+ "=" + str(-10/3))
print(("10/-3")+ "=" + str(10/-3))

print(9.73800000000)
print(("9.73800000000")+ "=" + str(9.73800000000))
print(("9.738043625475237500")+ "=" + str(9.738043625475237500))
print(("9.73804362547523750082364862865821")+ "=" + str(9.73804362547523750082364862865821))

print(("10**3")+ "=" + str(10**3))

print((" Quotient of " ) + ( " 10//3 ")+ " = " + str(10//3))

print((" Remainder of " ) + ( " 10%3 " )+ " = " + str(10%3))


A=14
B=40
print(""" IF input is A=14 and B=40 then,
 modolous // and remainder % is """)
print("print(A//B) = " , A//B)
print("print(A%B) = " , (A%B))




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

op=input( """please input a calculating or math operetion:
like 12+14 or 14*30 or 34//22 etc
                  """ )
print(eval(op))



print('''

''')

print("""
codex=input('''     please input your code by typing
copy paste will not work till now     :
 ''')


                 """    )
codex=input('''     please input your code by typing
copy paste will not work till now     :


                 '''       )
print("""
print(codex)
print("The above code that you typed -  will give output")
exec(codex)
""")
print(codex)
print("The above code that you typed -  will give output")
exec(codex)
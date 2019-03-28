#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     23/03/2019
# Copyright:   (c) User 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
print ("""entered value inside input function will
always get out as string""")
print ("""entered value inside input function will
always get out as string""")
name=input('Please enter your anme:   ')
age=input(' Please enter your age:    ')
print(" Hello" ,  name , "you are " , age)

n = input("please input your age")

print(float(n)/2)

print ("""entered value inside input function will
always get out as string""")
print ("""entered value inside input function will
always get out as string""")
primelist2=[]
lower=int(input("please enter the 'lower' or first value: " ))
upper=int(input("please enter the 'upper' or last value: " ))
for num in range (lower, upper+1):
    if num>1:
       for i in range (2, num):
           if num%i==0:
            break
       else:
        primelist2.append(num)
print("""After entering the values those codes will show prime number
list between """ ,
 lower, "and", upper, ''' numbers''' )
print(primelist2)

print(''' But we can reduce the output time by setting range of the diviser to
square root of a number''')
primelist3=[]
lower2=int(input("please enter the 'lower2' or first value: " ))
upper2=int(input("please enter the 'upper2' or last value: " ))
for num in range (lower2, upper2+1):
    if num>1:
       for i in range (2, int(num**.5)+1):
           if num%i==0:
            break
       else:
        primelist3.append(num)
print("""After entering the values those codes will show prime number
list between """ ,
 lower2, "and", upper2, ''' numbers''' )
print(primelist3)
print('#----------------------------------------')

print("foo")

foo=input("Pleae enter the value of foo:  ")
print(foo)

print(float("210" * int(input("Enter a intiger number :  "))))

float(input("Enter a number:   ")) + float(input("Enter a number:   "))

float(input("Enter a number fia:   ")) + float(input("Enter a number fib:   "))

print(float(input("Enter a number pfic1 :   ")) + float(input("Enter a number pfic2 :   ")))
print(int(input("Enter a number piic1 :   ")) + int(input("Enter a number piic2 :   ")))
input('To continue to the end of programm \n- Please Enter something :____ ')
print (input('To continue to the end of programm \n- Please Enter something :____ '))

codex=input('''     please input your code by typing
copy paste will not work till now     :


                 '''       )

print(codex)
print("The above code that you typed -  will give output")
exec(codex)

name=input('Please enter your anme:   ')
age=input(' Please enter your age:    ')
print(" Hello" ,  name , "you are " , age)

num1=input('Please enter a number:   ')
num2=input('Please enter another number:   ')
result=float(num1)+float(num2)
print(result)
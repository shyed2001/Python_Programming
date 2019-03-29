
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
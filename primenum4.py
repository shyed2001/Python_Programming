print(''' But we can reduce the output time by setting range of the diviser to
square root of a number''')
primelist3=[]
#lower2=int(input("please enter the 'lower2' or first value: " ))
#upper2=int(input("please enter the 'upper2' or last value: " ))
for num in range (2, 22222):
    if num>1:
       for i in range (2, int(num**.5)+1):
           if num%i==0:
            break
       else:
        primelist3.append(num)
#print("""After entering the values those codes will show prime number
#list between """ ,  lower2, "and", upper2, ''' numbers''' )
print("""After entering the values those codes will show prime number
list between """ , 2, "and", 22222, ''' numbers''' )
print(primelist3)
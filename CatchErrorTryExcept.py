print("vol 1.11")
try:
    num = int(input("Please enter a number:  "))
    print(num)
except: # this will catch ay error
       print("Invalid input")


print("vol 1.22")
#value=10/0
print(" this will show zero division error")
try:
    num = int(input("Please enter a number:  "))
    print(num)
except:
       print("Invalid input")


print("vol 1.33")

try:
    value=10/0
    print(''' this will also catch error of value=10/0,
    and print invalid iputwhich is unwanted.''')
    num = int(input("Please enter a number:  "))
    print(num)
except:

       print("Invalid input")

print("vol 2.00")

try:
    value=10/0
    print(''' this will also catch error of value=10/0,
    and print invalid iputwhich is unwanted.''')
    num = int(input("Please enter a number:  "))
    print(num)
except ZeroDivisionError :
    print("division by zero")
except ValueError:
       print("Invalid input")

try:
    value=10/0
    print(''' this will also catch error of value=10/0,
    and print invalid iputwhich is unwanted.''')
    num = int(input("Please enter a number:  "))
    print(num)
except ZeroDivisionError as err :
    print("err") # to print the actual error.
    print("division by zero")
except ValueError:
       print("Invalid input")
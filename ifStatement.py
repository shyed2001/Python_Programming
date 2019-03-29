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

def max_num(n1, n2, n3):
    if n1>=n2 and n1>=n3:
        return n1
    elif n2>=n1 and n2>=n2:
        return n2
print(max_num(33,4,15))



print('''
''')
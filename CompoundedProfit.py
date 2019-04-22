print("""
Calculating:-
A=Total money after years of compounded profit earnings
P=Principal amount, the initial investment.
r= Annual nominal interest rate, as decimal.
n=Nuber of times the profit is compunded or added.
t=number of yours
Formula is A=P(1+(r/n))**(n*t)
or
a=(1+(r/n))
b=(n*t)
A=P*a**b
print(A)
P=float(input("Please enter Principal amount the initial investment:  "))
print("P=Principal amount, the initial investment.", P)
r=float(input("Please enter Annual nominal interest rate, written decimal:  "))
print(" r Annual nominal interest rate, written decimal ", r)
n=float(input("Please enter Nuber of times the profit gets compunded/ added  per year:   "))
print("n Nuber of times the profit gets compunded/ added  per year ", n)
t=float(input("Please enter, number of yours :   "))
print("t number of yours  ", t)
#A1=P(1+(r/n))**(n*t)
print("A1= P(1+(r/n))**(n*t) = ", A)
print('''
a=(1+(r/n))
b=(n*t)
A2=P*a**b
print(A2)
''')
a=(1+(r/n))
b=(n*t)
A=P*a**b
print(A)
""")
P=float(input("Please enter Principal amount the initial investment:  "))
print("P=Principal amount, the initial investment.", P)
r=float(input("Please enter Annual nominal interest rate, written decimal:  "))
print(" r Annual nominal interest rate, written decimal ", r)
n=float(input("Please enter Nuber of times the profit gets compunded/ added  per year:   "))
print("n Nuber of times the profit gets compunded/ added  per year ", n)
t=float(input("Please enter, number of yours :   "))
print("t number of yours  ", t)
#A1=P(1+(r/n))**(n*t)

print('''
a=(1+(r/n))
b=(n*t)
A2=P*a**b
print(A2)
''')
a=(1+(r/n))
b=(n*t)
A=P*a**b
print(A)
print("A= P(1+(r/n))**(n*t) = ", A)

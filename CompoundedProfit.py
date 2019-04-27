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

def final_amount(p, r, n, t):
    a = p * (1 + r/n) ** (n*t)
    return a

print("""
def final_amount(p, r, n, t):
    a = p * (1 + r/n) ** (n*t)
    return a
 Apply the compound interest formula to p
to produce the final amount.
toInvest = float(input("How much do you want to invest?"))
fnl = final_amount(toInvest, 0.08, 12, 5)
print("At the end of the period you'll have", fnl)

""" )
# This is new, and makes the function fruitful.
# now that we have the function above, let us call it.

toInvest = float(input("How much do you want to invest?"))
fnl = final_amount(toInvest, 0.08, 12, 5)
print("At the end of the period you'll have", fnl)


print('''primelist1=[]
for x in range (2, 22222):
 isPrime=True
 for y in range (2,x):
    if x%y==0:
       isPrime=False
       break
 if isPrime:
    primelist.append(x)
 print(primelist1)
 Those codes with " break in for loop" will show   prime nuber list between 2 to 22222''' )

primelist1=[]
for x in range (2, 22222):
 isPrime=True
 for y in range (2,x):
    if x%y==0:
       isPrime=False
       break
 if isPrime:
    primelist1.append(x)
print(primelist1)

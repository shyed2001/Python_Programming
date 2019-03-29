print('Prime number generator in three types of code')

print('''for x in range (2, 22222):
 isPrime=True
 for y in range (2,x):
    if x%y==0:
       isPrime=False
       break
 if isPrime:
  print(x)
this without " break in for loop" code will produce = ''')
for x in range (2, 22222):
 isPrime=True
 for y in range (2,x):
    if x%y==0:
       isPrime=False
 if isPrime:
  print(x)


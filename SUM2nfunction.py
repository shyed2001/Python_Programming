n = input("Enter Number to calculate sum")
n = int (n)
#average = 0.
# sum = 0
sum = 0.
for num in range(0,n+1,1):
   sum = sum+num
print("SUM of first ", n, "numbers is: ", sum )

# Print sum of numbers from 1 to N inclusive

def sum2N(N):
    r = 0
    for i in range(N+1):
     #for i in range(0,N+1,1):
        #r+=i
        r=r+i
    return(r)

print(sum2N(10))

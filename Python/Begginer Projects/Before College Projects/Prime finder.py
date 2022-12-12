def prime(n):
    if(n==0 or n==1):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
        else: 
            return True

N = int(input("Enter a number: "))
for i in range(1,N+1):
    if(prime(i)):
        print(i,end=" ")
        
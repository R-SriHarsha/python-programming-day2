#to check whether given no is perfect number
N=int(input())
sum=0
for i in range(1,N):
    if N%i==0:
        sum+=i
if(sum==N):
    print("perfect number")
else:
    print("not perfect number")
    

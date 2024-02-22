#is prime or not
'''
N=int(input())
for i in range(2,N):
    if(N%i==0):
        print("is not prime")
        break
    
if i==N-1:
    print("is prime")
'''
#using for else loop

'''
N=int(input())
for i in range(2,N):
    if(N%i==0):
        print("is not prime")
        break
    
else:
    print("is prime")
'''


#using while loop
'''
# print no of factors and check if number is prime or not
N=int(input())
factors=0
i=1
while i<(1,N+1):#we can use N//2 and N**0.5 to reduce the no of iterations
    if(N%i==0):
        factors+=1
    i+=1
    
print(factors)

if factors==2:
    print("prime")
elif factors<=1:
    print("not defined")
else:
    print("not prime")
    

'''

#using for loop


# print no of factors and check if number is prime or not
N=int(input())
factors=0
for i in range(1,N+1):#we can use N//2 and N**0.5 to reduce the no of iterations
    if(N%i==0):
        factors+=1

print(factors)

if factors==2:
    print("prime")
elif factors<=1:
    print("not defined")
else:
    print("not prime")
    

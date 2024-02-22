# strong number in rannge of given
'''
def strong(n):
    sum=0
    x=n
    digit=0
    while n>0:
        digit=n%10
        fact=1
        for i in range(1,digit+1):
            fact*=i
        sum+= fact
        n//=10

    if sum==x:
        print(x)


    
n,m=int(input()),int(input())

for i in range(n,m+1):
    strong(i)
'''

def strong(n,m):
    for i in range(n,m+1):
        sum=0
        x=i
        digit=0
        while i>0:
            digit=i%10
            fact=1
            for j in range(1,digit+1):
                fact*=j
            sum+= fact
            i//=10

        if sum==x:
            print(x)


    
n,m=int(input()),int(input())


strong(n,m)

#program to check for strong number using functions

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
        print("strong number")
    else:
        print("weak number")
n=int(input())
strong(n)





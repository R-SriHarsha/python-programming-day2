#program to check if given number is armstrong number

n=int(input())
s=0
digit=0
while n>0:
    digit=n%10
    s+=digit**3
    n//=10

if(s==n):
    print("armstrong number")
else:
    print("not an armstrong number")
    

    

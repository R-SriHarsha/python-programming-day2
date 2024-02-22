#python program to print armstrong numbers in a range using functions

def armstrong():
    s=0
    digit=0
    while n>0:
        digit=n%10
        s+=digit**3
        n//=10

    if(s==n):
        print(s)
st,en=map(int,input().split(" "))


for i in range(st,en):
    armstrong(i)

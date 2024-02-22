#write a python program to print the reverse of a number
#using while loop
'''
N=int(input())
s=0

while N>0:
    s*=10
    s+=N%10
    N//=10

print(s)
    
'''


#using for loop
N=int(input())
s=0

for i in range(N):
    if N==0:
        break
    s*=10
    s+=N%10
    N//=10

print(s)

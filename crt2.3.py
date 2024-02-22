#print no's which are not divisible by 6,7,8
'''
start,end=map(int,input().split(" "))
print("The numbers which are not Divisible by 6,7,8:")
for i in range(start,end):
    if i%6!=0 and i%7!=0 and i%8!=0:
        print(i)
'''
start,end=map(int,input().split(" "))
print("The numbers which are not Divisible by 6,7,8:")
i=start
while(i<=end):
    if i%6!=0 and i%7!=0 and i%8!=0:
        print(i)
    i+=1

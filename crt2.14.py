#write a python program to print count of vovels in both even position ans odd position
s="aeiouAEIOU"
s2=input()
counte=0
counto=0
for i in range(len(s2)):
    if i%2==0:
        if s2[i] in s:
            counte+=1
    else:
        if s2[i] in s:
            counto+=1

print(counte,counto)


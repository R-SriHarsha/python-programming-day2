#write a python program to remove duplicates in a given string
s=input()
s2=""
for i in s:
    if i not in s2:
        s2+=i

print(s2)
        

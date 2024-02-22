#write a python program to remove consecutive duplicates in a string

s=input()
s2=s[0]
for i in range(1,len(s)):
    if s[i-1]!=s[i]:
        s2+=s[i]

print(s2)
    

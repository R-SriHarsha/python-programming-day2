#program to print prime numbers in a range using functions

def prime(n,m):
    
    for i in range(n,m+1):
        fact=0
        for j in range(1,i+1):

            if i%j==0:
                fact+=1

            if fact>2:
                break
        
        if(fact==2):
            print(i)

    

n,m=map(int,input().split())
prime(n,m)
                
    

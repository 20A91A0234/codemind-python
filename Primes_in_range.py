from math import *
def prime(n):
    # if( n == 1 ):
    #     return False
    # cnt = 0
    # for i in range(1,n+1):
    #     if( n%i == 0 ):
    #       cnt+=1
    
    # if( cnt == 2 ):
    #     return True
    # return False
    
    if( n <= 1 ):
        return False
        
    sq = int(sqrt(n))
    
    for i in range(2,sq+1):
        if( n%i == 0 ):
            return False
    
    return True



a=int(input())
b=int(input())
c = 0
for i in range(a,b+1):
    if( prime(i) ):
        c+=1
print(c)
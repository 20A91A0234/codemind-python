m=int(input())
n=int(input())
k=[]
for i in range(m,n+1):
    m=i
    a=m
    z=str(a)
    l=len(z)
    s=True
    for j in range(1,l+1):
        x=a%10
        if x!=0:
            if m%x!=0:
                s=False
        if x%10==0:
            s=False
        a=a//10
    if s==True:
        k=k+[i]
print(*k)
            
            
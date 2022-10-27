x=int(input())
c=int(input())
for i in range(x,c):
    s=0
    v=i
    while i>0:
        r=i%10
        s=s*10+r
        i=i//10
    if v==s:
        print(v,end=" ")
n=int(input())
for i in range(n):
    D,d,P,Q=map(int,input().split())
    x=D//d
    y=D%d
    s=0
    for j in range(x):
        s+=(P+j*Q)*d
    s+=(P+x*Q)*y
    print(s)
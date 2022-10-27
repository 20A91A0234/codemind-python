n=int(input())
s=0
for i in range(1,n+1):
    if n%i==0:
        s=s+i
if n==1 or s==n+1:
    print("prime")
else:
    print("not a prime")
n=int(input())
a=0
b=1
for i in range(2,n):
    c=a+b
    a=b
    b=c
    if c>=n:
        break
if n-a==b-n:
    print(a,b)
elif n-a>b-n:
    print(b)
elif n-a<b-n:
    print(a)
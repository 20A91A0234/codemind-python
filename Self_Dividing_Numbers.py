a=int(input())
b=int(input())

s=[]
for i in range(a,b+1):
    x=i
    while x>0:
        r=x%10
        if r==0 or i%r!=0:
            break
        x=x//10
    if x==0:
        s.append(i)
for i in range (0,len(s)):
    print(s[i],end=" ")
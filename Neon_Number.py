a=int(input())
x=a*a
s=0
while x>0:
    s=s+x%10
    x=x//10
if (a==s):
    print("Neon Number")
else:
    print("Not Neon Number")
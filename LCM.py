a,b=map(int,input().split())
if a>b:
    c=a
else:
    c=b
while a:
    if c%a==0 and c%b==0:
        lcm=c
        break
    c+=1
        
            
print(c)  
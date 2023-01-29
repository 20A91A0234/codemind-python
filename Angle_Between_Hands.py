v,s=map(int,input().split(':'))
x=abs(30*v-(11/2)*s)
if x>180:
    print(360-x)
else:
    print(x)
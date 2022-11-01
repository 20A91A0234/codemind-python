import math
x=int(input())
for i in range(x):
    b=input()
    o=int(b,2)
    o=oct(o)
    print(o[2:])
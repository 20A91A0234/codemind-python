def sum_of(n):
    s=0
    while n>0:
        s=s+n%10
        n=n//10
    if s > 9:
        return sum_of(s)
    return s
n=int(input())
print(sum_of(n))
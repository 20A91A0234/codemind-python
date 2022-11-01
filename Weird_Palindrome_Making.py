for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    n1=0
    for j in arr:
        if j%2:
            n1+=1
    print(n1//2)
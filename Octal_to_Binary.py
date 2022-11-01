a=int(input())
for i in range(a):
    ono=input()
    bno=int(ono,8)
    bno=bin(bno)
    print(bno[2:])
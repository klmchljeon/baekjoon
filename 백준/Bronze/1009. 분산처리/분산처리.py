t = int(input())
for case in range(t):
    a,b = map(int,input().split())

    tmp = a%10
    for i in range(b-1):
        tmp *= a%10
        tmp %= 10

    if tmp == 0:
        print(10)
    else:
        print(tmp)
while True:
    n = int(input())
    if n == 0: break
    lst = list(map(int,input().split()))

    p = 0
    for i in lst:
        if p+i <= 300:
            p += i

    print(p)
while True:
    n = int(input())
    if not n: break

    lst = list(map(int,input().split()))
    cur = 0
    for i in range(3):
        cur += lst[i]

    res = cur
    for i in range(3,n):
        cur += lst[i]
        cur -= lst[i-3]
        res = max(res,cur)

    print(res)
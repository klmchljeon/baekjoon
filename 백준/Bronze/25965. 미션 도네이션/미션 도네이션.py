n = int(input())
for case in range(n):
    m = int(input())
    lst = []
    for _ in range(m):
        k,d,a = map(int,input().split())
        lst.append((k,d,a))

    k,d,a = map(int,input().split())

    res = 0
    for i in lst:
        p = k * i[0] - d * i[1] + a * i[2]
        res += max(0,p)

    print(res)
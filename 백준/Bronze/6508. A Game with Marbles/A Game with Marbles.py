while True:
    n = int(input())
    if n == 0:
        break

    lst = list(map(int,input().split()))
    res = 0
    while lst:
        tmp = lst.pop()
        res += tmp
        for i in range(len(lst)):
            lst[i] += tmp

    print(res)
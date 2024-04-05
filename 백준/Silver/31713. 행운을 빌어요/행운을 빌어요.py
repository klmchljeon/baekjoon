t = int(input())
for case in range(t):
    a,b = map(int,input().split())
    res = int(1e9)
    four = 0
    while four<=a or four*4<=b:
        ca,cb = a,b
        ca -= four
        cb -= four*4

        if cb > 0:
            div,mod = divmod(cb,3)
            ca -= div
            cb -= div*3

            if mod:
                ca -= 1
                cb -= 3

        if ca > 0:
            cb -= ca*3
            ca = 0

        res = min(res, -(ca+cb))
        four += 1

    print(res)
while True:
    n = int(input())
    if n == 0: break

    n -= 1
    res = []
    i = 0
    while 1<<i <= n:
        if n&(1<<i):
            res.append(3**i)

        i += 1

    if not res:
        print('{ }')
    else:
        print('{ ', end='')
        print(*res, sep=', ', end='')
        print(' }')
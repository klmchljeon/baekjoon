t = int(input())
for case in range(t):
    n = int(input())

    res = 0
    while n > 1:
        n,mod = divmod(n,2)
        res += mod
        n += mod

    print(res)
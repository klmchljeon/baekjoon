t = int(input())
for case in range(t):
    n,st = input().split()
    n = int(n)

    sa = list(range(n))
    rank = [ord(i) for i in st]
    if n == 1: rank = [0]

    tmp = [0]*n

    o = 1
    while o < n:
        f = lambda x:(rank[x],rank[(x+o)%n])
        sa.sort(key = f)

        tmp[sa[0]] = 0
        for i in range(1,n):
            tmp[sa[i]] = tmp[sa[i-1]]
            if f(sa[i]) != f(sa[i-1]):
                tmp[sa[i]] += 1

        rank[:] = tmp[:]
        o *= 2

    print(sa[0])
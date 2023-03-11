def find(num):
    st = str(num)
    l = len(st)
    res = set()
    for i in range(l):
        tmp = ''
        for j in range(i,l):
            tmp += st[j]
            res.add(int(tmp))

    res.discard(0)
    res.discard(num)
    return res

n = int(input())
g = [False]*(n+1)
prev = [None]*(n+1)

for i in range(10,n+1):
    lst = sorted(find(i))
    for j in lst:
        if not g[i-j]:
            g[i] = True
            prev[i] = j
            break

print(prev[n] if g[n] else -1)
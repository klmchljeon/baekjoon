st = input()
n = len(st)

sa = list(range(n))
rank = [ord(i) for i in st]
tmp = [0]*n

o = 1
while o < n:
    f = lambda x:(rank[x],rank[x+o] if x+o<n else -1)
    sa.sort(key = f)

    tmp[sa[0]] = 0
    for i in range(1,n):
        tmp[sa[i]] = tmp[sa[i-1]]
        if f(sa[i]) != f(sa[i-1]):
            tmp[sa[i]] += 1

    rank[:] = tmp[:]
    o *= 2

print(*sa,sep='\n')
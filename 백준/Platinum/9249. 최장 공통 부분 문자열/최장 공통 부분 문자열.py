st1 = input()
st2 = input()
m = len(st1)

st = st1 + ' ' + st2
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

for i in range(n-1):
    a = sa[i]
    b = sa[i+1]

lcp = [0]*n
h = 0

res = 0
idx = -1
for i in range(n):
    if rank[i] == 0: continue

    a = sa[rank[i]]
    b = sa[rank[i]-1]
    while a+h<n and b+h<n and st[a+h]==st[b+h]:
        h += 1

    lcp[rank[i]] = h
    if (a>m)^(b>m) and res < h:
        res = h
        idx = a

    if h > 0:
        h -= 1

print(res)
print(st[idx:idx+res])
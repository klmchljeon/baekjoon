import sys
input = sys.stdin.readline

n,k = map(int,input().split())
st = [int(input()) for _ in range(n)]

sa = list(range(n))
rank = st[:]
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

lcp = [0]*n
h = 0
for i in range(n):
    if rank[i] == 0: continue

    a = sa[rank[i]]
    b = sa[rank[i]-1]
    while a+h<n and b+h<n and st[a+h]==st[b+h]:
        h += 1

    lcp[rank[i]] = h
    if h > 0:
        h -= 1

res = 0
stack = []
for i in range(n):
    cnt = 0
    while stack and stack[-1][0] > lcp[i]:
        val,c = stack.pop()
        cnt += c
        if cnt+1 >= k:
            res = max(res,val)

    if lcp[i]:
        stack.append((lcp[i],cnt+1))

cnt = 0
while stack:
    val,c = stack.pop()
    cnt += c
    if cnt+1 >= k:
        res = max(res,val)

print(res)
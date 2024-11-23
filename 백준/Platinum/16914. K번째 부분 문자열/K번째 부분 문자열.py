
st = input()
n = len(st)

sa = list(range(n))
rank = [ord(i) for i in st]
if len(st) == 1:
    rank = [0]

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
for i in range(n):
    if rank[i] == 0: continue

    a = sa[rank[i]]
    b = sa[rank[i]-1]
    while a+h<n and b+h<n and st[a+h]==st[b+h]:
        h += 1

    lcp[rank[i]] = h
    if h > 0:
        h -= 1

lst = [0]
for i in range(n):
    lst.append(lst[-1] + (n-sa[i]) - lcp[i])

q = int(input())
for query in range(q):
    k = int(input())
    if lst[-1] < k: 
        print(-1)
        continue
    
    s,e = 0,len(lst)-1
    while s+1<e:
        mid = (s+e)//2

        if lst[mid] >= k:
            e = mid

        else:
            s = mid

    idx = e

    i = sa[idx-1]
    print(st[i:n-(lst[idx]-k)])
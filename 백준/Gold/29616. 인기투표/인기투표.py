from math import gcd

n,p = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

prev = []
gcda = gcd(*a)
for i in a:
    prev.append(i//gcda)

gcdb = gcd(*b)
m = 1
for i in range(n):
    tmp = b[i]//gcdb
    if tmp == 0: continue

    p = prev[i]//tmp + bool(prev[i]%tmp)
    m = max(m,p)

cur = []
for i in b:
    cur.append(i//gcdb*m)

print(sum(prev),sum(cur))
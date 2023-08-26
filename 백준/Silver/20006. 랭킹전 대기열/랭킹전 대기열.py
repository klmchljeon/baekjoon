#랭킹전 대기열
from collections import deque

f = lambda x:x[1]

p,m = map(int,input().split())
d = []
for _ in range(p):
    l,n = input().split()
    l = int(l)

    for i in range(len(d)):
        fir = d[i][0]
        if fir-10 <= l <= fir+10 and len(d[i][1])<m:
            d[i][1].append((l,n))
            break

    else:
        d.append([l,[(l,n)]])

for i in d:
    res = 'Started!' if len(i[1])==m else 'Waiting!'
    
    print(res)
    for j in sorted(i[1],key=f):
        print(*j)
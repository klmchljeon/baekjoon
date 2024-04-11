import sys
input = sys.stdin.readline

n,m = map(int,input().split())
d = [int(input()) for _ in range(n)]
d.sort()
lst = [d[i+1]-d[i] for i in range(n-1)]

e = 0
tmp = 0
res = d[-1] - d[0]
for s in range(n-1):
    while e<n-1 and tmp<m:
        tmp += lst[e]
        e += 1
    
    if tmp >= m:
        res = min(res,tmp)

    tmp -= lst[s]

print(res)
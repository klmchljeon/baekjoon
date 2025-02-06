n,x = map(int,input().split())
res = -1
for _ in range(n):
    s,t = map(int,input().split())
    if s+t <= x:
        res = max(res,s)

print(res)
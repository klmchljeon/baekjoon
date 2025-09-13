n,k = map(int,input().split())
lst = list(map(int,input().split()))
res = []
for i in lst:
    if i-1 <= n-i:
        res.append(1)
    else:
        res.append(n)

print(*res)
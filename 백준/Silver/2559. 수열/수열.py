n,k = map(int,input().split())
lst = list(map(int,input().split()))

s = 0
for i in range(k):
    s += lst[i]

res = s
tmp = res
for i in range(k,n):
    tmp += lst[i]
    tmp -= lst[i-k]
    res = max(res, tmp)

print(res)
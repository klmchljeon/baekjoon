n,m = map(int,input().split())
lst = list(map(int,input().split()))

tmp = 0
for i in range(m):
    tmp += lst[i]

res = tmp
for i in range(m,n):
    tmp += lst[i]
    tmp -= lst[i-m]
    res = max(res,tmp)

print(res)
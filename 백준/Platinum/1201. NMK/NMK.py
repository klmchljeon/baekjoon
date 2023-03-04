n,m,k = map(int,input().split())
flag1 = n+1 < m+k
flag2 = m*k < n

if flag1 or flag2:
    print(-1)
    exit()

res = list(range(n-m+1,n+1))

idx = n-m
lst = []
tmp = []
while idx:
    tmp.append(idx)
    idx -= 1

    if len(tmp) == k-1:
        lst.append(tmp)
        tmp = []
if tmp: lst.append(tmp)

for i in lst[::-1]:
    res.extend(i)

print(*res)
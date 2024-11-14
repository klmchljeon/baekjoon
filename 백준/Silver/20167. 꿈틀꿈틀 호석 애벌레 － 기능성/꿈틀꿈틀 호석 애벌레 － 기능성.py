n,k = map(int,input().split())
lst = list(map(int,input().split()))

res = 0
for i in range(1<<n):
    tmp = 0
    p = 0
    for j in range(n):
        if i&(1<<j):
            tmp += lst[j]
            if tmp >= k:
                p += tmp-k
                tmp = 0

    res = max(res,p)

print(res)
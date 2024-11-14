n,k = map(int,input().split())
lst = list(map(int,input().split()))

res = 0
for i in range(1<<n):
    tmp = 0
    p = 0
    idx = 0
    for j in range(n):
        if not i&(1<<j): continue
        if idx > j: continue

        idx = j
        while idx < n:
            tmp += lst[idx]
            idx += 1
            if tmp >= k:
                p += tmp-k
                tmp = 0
                break

    res = max(res,p)

print(res)
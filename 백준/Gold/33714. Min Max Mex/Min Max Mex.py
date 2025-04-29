n,k = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()

p = k
prev = -1
cnt = int(1e9) + 1
for i in range(n):
    if prev == lst[i]:
        cnt += 1
    else:
        if cnt <= k:
            res1 = prev
            break

        if prev + 1 != lst[i]:
            res1 = prev+1
            break

        cnt = 1
        prev = lst[i]

else:
    res1 = prev + (cnt > k)

q = k
prev = -1
for i in range(n):
    if prev == lst[i]: continue

    if lst[i]-prev-1 <= q:
        q -= lst[i]-prev-1
        prev = lst[i]
    else:
        prev += q
        q = 0

res2 = prev+q+1

print(res1,res2,sep='\n')
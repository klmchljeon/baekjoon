n,d,k = map(int,input().split())
lst = list(map(int,input().split()))
p = max(lst)
cnt = 0
res = 0
for i in range(d):
    if cnt + p > k:
        cnt = 0
        res += 1

    cnt += p

print(res)
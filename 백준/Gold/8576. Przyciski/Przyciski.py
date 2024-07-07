n,m = map(int,input().split())
lst = list(map(int,input().split()))

cnt = [0]*(n+1)
max_ = 0
cur = 0

for i in lst:
    if i <= n:
        cnt[i] = max(cnt[i], cur) + 1
        max_ = max(max_, cnt[i])

    else:
        cur = max_

for i in range(1,n+1):
    if cnt[i] < cur:
        cnt[i] = cur

print(*cnt[1:])
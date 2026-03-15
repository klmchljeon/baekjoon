n,p = map(int,input().split())
cnt = [0]*1001
cnt[n] += 1

cur = n
for _ in range(200):
    cur *= n
    cur %= p

    cnt[cur] += 1

res = 0
for i in cnt:
    res += i>1

print(res)
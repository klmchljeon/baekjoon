n = int(input())
cnt = [0]*(10001)
for _ in range(n):
    x = int(input())
    cnt[x] += 1

res = -1
val = -1
for x in range(1,10001):
    if val < cnt[x]:
        val = cnt[x]
        res = x

print(res)
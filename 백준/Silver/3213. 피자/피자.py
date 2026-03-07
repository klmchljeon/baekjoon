n = int(input())
cnt = [0]*3
for _ in range(n):
    a,b = map(int,input().split('/'))
    if b == 2:
        a *= 2

    a -= 1

    cnt[a] += 1

res = cnt[2]
cnt[0] = max(0,cnt[0]-cnt[2])
cnt[2] = 0

res += cnt[1]//2
cnt[1] %= 2

if cnt[1]:
    res += 1
    cnt[0] = max(0,cnt[0]-2)

res += cnt[0]//4 + bool(cnt[0]%4)
cnt[0] = 0

print(res)
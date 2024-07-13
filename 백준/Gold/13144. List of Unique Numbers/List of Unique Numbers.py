max_ = 100000

n = int(input())
lst = list(map(int,input().split()))

res = 0
cnt = [0]*(max_+1)
e = 0
for s in range(n):
    while e < n and cnt[lst[e]] != 1:
        cnt[lst[e]] += 1
        e += 1

    cnt[lst[s]] -= 1
    res += e-s

print(res)
lst = list(map(int,input().split()))
n = int(input())

res = 0
for i in range(n):
    cnt = [0]*3
    for _ in range(3):
        tmp = list(map(int,input().split()))
        for j in range(3):
            cnt[j] += tmp[j]

    p = 0
    for j in range(3):
        p += lst[j]*cnt[j]

    res = max(res,p)

print(res)
#홍준 프로그래밍 대회
m = 2000000

n = int(input())
d = list(map(int,input().split()))

num = [0]*(m+1)
for i in d:
    num[i] += 1

res = n
for i in range(2,m+1):
    cnt = 0
    for j in range(i,m+1,i):
        cnt += num[j]

    if cnt < 2: continue

    res = max(res, cnt*i)

print(res)
import sys
input = sys.stdin.readline

n,d,k,c = map(int,input().split())
lst = [int(input()) for _ in range(n)]

cnt = 0
tmp = [0]*(d+1)
tmp[c] += 1
cnt += 1

for i in range(k):
    tmp[lst[i]] += 1
    if tmp[lst[i]] == 1:
        cnt += 1

res = 0
for i in range(n):
    tmp[lst[i]] -= 1
    if tmp[lst[i]] == 0:
        cnt -= 1

    tmp[lst[(i+k)%n]] += 1
    if tmp[lst[(i+k)%n]] == 1:
        cnt += 1

    res = max(res,cnt)

print(res)
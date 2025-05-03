n = int(input())
res = 0
cnt = 0
for i in range(n):
    a,b = map(int,input().split())
    if a+b == 0:
        cnt += 1

    else:
        res = max(res,cnt*2)
        cnt = 0

if cnt:
    res = max(res,cnt*2)

print(res)
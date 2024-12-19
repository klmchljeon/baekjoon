n = int(input())
lst = list(map(int,input().split()))
res = 0
cnt = 0
for i in lst:
    if i:
        cnt += 1
    else:
        res = max(res,cnt)
        cnt = 0

res = max(res,cnt)
print(res)
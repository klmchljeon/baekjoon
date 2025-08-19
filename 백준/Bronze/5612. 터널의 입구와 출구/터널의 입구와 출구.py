n = int(input())
cur = int(input())
res = cur
for _ in range(n):
    a,b = map(int,input().split())
    cur += a - b
    if cur < 0:
        print(0)
        break

    res = max(res,cur)

else:
    print(res)
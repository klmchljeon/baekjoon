#숫자 정사각형
n,m = map(int,input().split())
d = [list(map(int,input())) for _ in range(n)]

res = 1
for x in range(n):
    for y in range(m):
        t = d[x][y]

        for i in range(max(n,m)):
            if x+i>=n or y+i>=m: break

            if t != d[x+i][y]: continue
            if t != d[x][y+i]: continue
            if t != d[x+i][y+i]: continue

            res = max(res,(i+1)**2)

print(res)
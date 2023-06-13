#직사각형 네개의 합집합의 면적 구하기
d = [[0]*101 for _ in range(101)]

for _ in range(4):
    sx,sy,ex,ey = map(int,input().split())
    for i in range(sx,ex):
        for j in range(sy,ey):
            d[i][j] = 1

res = 0
for i in range(101):
    for j in range(101):
        res += d[i][j]

print(res)
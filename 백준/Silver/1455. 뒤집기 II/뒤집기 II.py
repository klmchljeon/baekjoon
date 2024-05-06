n,m = map(int,input().split())
d = [list(map(int,input())) for _ in range(n)]

cnt = 0
for i in range(n-1,-1,-1):
    for j in range(m-1,-1,-1):
        if d[i][j] == 0: continue

        cnt += 1
        for x in range(i+1):
            for y in range(j+1):
                d[x][y] ^= 1

print(cnt)
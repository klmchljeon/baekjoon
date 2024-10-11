dx = (-1,1,0,0)
dy = (0,0,-1,1)

n = int(input())
lst = [[0]*101 for _ in range(101)]
for _ in range(n):
    x,y = map(int,input().split())
    for i in range(10):
        for j in range(10):
            lst[x+i][y+j] = 1

res = 0
for x in range(101):
    for y in range(101):
        if lst[x][y] == 0: continue

        cnt = 4
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<=100 and 0<=ny<=100 and lst[nx][ny] == 1:
                cnt -= 1

        res += cnt

print(res)
#사탕 게임
def check():
    cnt = 0

    for i in range(n):
        tmp = 0

        prev = d[i][0]
        for j in range(n):
            if d[i][j] == prev:
                tmp += 1

            else:
                cnt = max(cnt,tmp)
                tmp = 1

            prev = d[i][j]

        cnt = max(cnt,tmp)

    for j in range(n):
        tmp = 0

        prev = d[0][j]
        for i in range(n):
            if d[i][j] == prev:
                tmp += 1

            else:
                cnt = max(cnt,tmp)
                tmp = 1

            prev = d[i][j]

        cnt = max(cnt,tmp)

    return cnt

n = int(input())
d = [list(input()) for _ in range(n)]

res = 0
for x in range(n):
    for y in range(n):
        for dx,dy in ((0,-1),(-1,0)):
            nx = x + dx
            ny = y + dy

            if nx>=n or ny>=n: continue
            if d[x][y]==d[nx][ny]: continue

            d[x][y],d[nx][ny] = d[nx][ny],d[x][y]
            res = max(res,check())
            d[x][y],d[nx][ny] = d[nx][ny],d[x][y]

print(res)
dx = (-1,1,0,0,-1,-1,1,1)
dy = (0,0,-1,1,-1,1,-1,1)

st = 'FOX'

n,m = map(int,input().split())
lst = [input() for _ in range(n)]

cnt = 0
for x in range(n):
    for y in range(m):
        for i in range(8):
            flag = True
            for k in range(3):
                nx = x + dx[i]*k
                ny = y + dy[i]*k
                if not (0<=nx<n and 0<=ny<m):
                    flag = False
                    break

                if not (lst[nx][ny] == st[k]):
                    flag = False
                    break

            cnt += flag

print(cnt)
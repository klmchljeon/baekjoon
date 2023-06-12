#다리 만들기
from collections import deque

def border(lst,c):
    res = [set() for _ in range(1,c+1)]
    for x in range(n):
        for y in range(n):
            if not lst[x][y]: continue

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if not (0<=nx<n and 0<=ny<n): continue

                if not lst[nx][ny]:
                    res[lst[x][y]].add((nx,ny))

    return list(map(list,res))

def island():
    visit = [[0]*n for _ in range(n)]
    
    cnt = 1
    for i in range(n):
        for j in range(n):
            if not visit[i][j] and d[i][j]:
                visit[i][j] = cnt
                queue = deque([(i,j)])

                while queue:
                    x,y = queue.popleft()

                    for dir in range(4):
                        nx = x + dx[dir]
                        ny = y + dy[dir]

                        if not (0<=nx<n and 0<=ny<n): continue

                        if not visit[nx][ny] and d[nx][ny]:
                            visit[nx][ny] = cnt
                            queue.append((nx,ny))

                cnt += 1

    return visit,cnt

dx = (0,0,-1,1)
dy = (-1,1,0,0)

n = int(input())
d = [list(map(int,input().split())) for _ in range(n)]

l,cnt = island()

blst = border(l,cnt)

res = 10000
for i in range(1,cnt):
    visit = [[-1]*n for _ in range(n)]
    queue = deque([])
    for x,y in blst[i]:
        visit[x][y] = 0
        queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        if d[x][y] == 1:
            res = min(res,visit[x][y])
            break

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if not (0<=nx<n and 0<=ny<n): continue

            if visit[nx][ny]==-1 and l[nx][ny]!=i:
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx,ny))

print(res)
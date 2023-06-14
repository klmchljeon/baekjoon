#Puyo Puyo
from collections import deque

def bfs(loc,t):
    global visit
    
    res = [loc]
    queue = deque([(loc)])
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nx<6 and 0<=ny<12): continue

            if not visit[nx][ny] and lst[nx][ny] == t:
                visit[nx][ny] = True
                
                res.append((nx,ny))
                queue.append((nx,ny))

    return res

def sim():
    global visit
    visit = [[False]*12 for _ in range(6)]
    
    bomb = []
    for i in range(6):
        for j in range(12):
            if not visit[i][j] and lst[i][j]!='.':
                visit[i][j] = True
                tmp = bfs((i,j),lst[i][j])
                if len(tmp) >= 4:
                    bomb.extend(tmp)

    if not bomb: return 0

    for x,y in bomb:
        lst[x][y] = '.'

    for i in range(6):
        for j in range(11,-1,-1):
            if lst[i][j] == '.':
                lst[i].pop(j)

    for i in range(6):
        while len(lst[i]) != 12:
            lst[i].append('.')

    return bomb

dx = (-1,1,0,0)
dy = (0,0,-1,1)

d = [list(input()) for _ in range(12)]
lst = []
for j in range(6):
    tmp = []
    for i in range(12):
        tmp.append(d[i][j])

    lst.append(tmp[::-1])

cnt = 0
while sim():
    cnt += 1

print(cnt)
from collections import deque

def bfs(loc):
    res = 0

    queue = deque([loc])
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nx<n and 0<=ny<m): continue
            if lst[nx][ny] != '#' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny))
                res += 1

    return res

dx = (-1,1,0,0)
dy = (0,0,-1,1)

t = int(input())
for case in range(t):
    n,m = map(int,input().split())
    lst = [input() for _ in range(n)]

    visited = [[False]*m for _ in range(n)]

    cnt,area = 0,0
    for i in range(n):
        for j in range(m):
            if lst[i][j] != '#' and not visited[i][j]:
                visited[i][j] = True
                cnt += 1
                area += bfs((i,j)) + 1

    st1 = 'section' if cnt==1 else 'sections'
    st2 = 'space' if area==1 else 'spaces'

    print(f'{cnt} {st1}, {area} {st2}')
from collections import deque

def solution(land):
    answer = 0
    
    dx = (-1,1,0,0)
    dy = (0,0,-1,1)

    def bfs(loc):
        miny,maxy = loc[1],loc[1]
        t = 1
        
        queue = deque([loc])
        while queue:
            x,y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if not (0<=nx<n and 0<=ny<m): continue
                
                if not visit[nx][ny] and land[nx][ny]:
                    visit[nx][ny] = True
                    miny = min(miny,ny)
                    maxy = max(maxy,ny)
                    queue.append((nx,ny))
                    t += 1
                    
        return miny,maxy,t
    
    n = len(land)
    m = len(land[0])
    res = [0]*m
    visit = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visit[i][j] and land[i][j]:
                visit[i][j] = True
                a,b,cnt = bfs((i,j))
                for k in range(a,b+1):
                    res[k] += cnt
                    
    print(res)
    
    return max(res)
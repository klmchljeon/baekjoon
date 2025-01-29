from collections import deque

n,k = map(int,input().split())
lst = []
for i in range(2):
    tmp = list(map(int,input()))
    lst.append(tmp)

x,y = (0,0)

visited = [[-1]*2 for _ in range(n)]
visited[x][y] = 0

queue = deque([(x,y)])
while queue:
    x,y = queue.popleft()

    for nx,ny in ((x+k,y^1),(x+1,y),(x-1,y)):
        if nx >= n: 
            print(1)
            exit()

        if not (visited[x][y] < nx): continue
        if visited[nx][ny] == -1 and lst[ny][nx]:
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx,ny))

print(0)
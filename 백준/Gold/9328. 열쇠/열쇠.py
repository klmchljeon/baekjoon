from collections import deque

dx = (-1,1,0,0)
dy = (0,0,-1,1)

def check(loc):
    x,y = loc
    if not (0<=x<n and 0<=y<m): return 0
    if lst[x][y] == '*': return 0
    if visited[x][y]: return 0

    if 'A' <= lst[x][y] <= 'Z':
        idx = ord(lst[x][y]) - ord('A')
        if not key[idx]:
            visited[x][y] = True
            tmp[idx].append((x,y))
            return 0
        
    if 'a' <= lst[x][y] <= 'z':
        idx = ord(lst[x][y]) - ord('a')
        key[idx] = True
        while tmp[idx]:
            nx,ny = tmp[idx].pop()
            queue.append((nx,ny))

    visited[x][y] = True
    queue.append((x,y))

    return lst[x][y] == '$'

t = int(input())
for case in range(t):
    n,m = map(int,input().split())
    lst = [input() for _ in range(n)]

    key = [False]*26
    st = input()
    if st != '0':
        for i in st:
            key[ord(i)-ord('a')] = True

    queue = deque([])
    tmp = [[] for _ in range(26)]
    visited = [[False]*m for _ in range(n)]

    res = 0
    for i in (0,n-1):
        for j in range(m):
            res += check((i,j))

    for j in (0,m-1):
        for i in range(n):
            res += check((i,j))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            res += check((nx,ny))

    print(res)
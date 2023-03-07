#알파벳
conv = lambda x: 1 << (ord(x)-ord('A'))

dx = (-1,1,0,0)
dy = (0,0,-1,1)

r,c = map(int,input().split())
d = tuple(tuple(map(conv,input())) for _ in range(r))

res = 1
stack = [((0,0),1,d[0][0])]

v = [[0]*c for _ in range(r)]
while stack:
    loc,cnt,visit = stack.pop()
    x,y = loc
    if v[x][y] == visit: continue
    
    v[x][y] = visit

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<r and 0<=ny<c and visit|d[nx][ny]!=visit:
            stack.append(((nx,ny),cnt+1,visit|d[nx][ny]))
            res = max(res,cnt+1)

print(res)
#숫자판 점프
def dfs(x,y,w:list):
    if len(w) == 6:
        st.add(''.join(w))
        return 

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0<=nx<5 and 0<=ny<5): continue
        
        w.append(d[nx][ny])
        dfs(nx,ny,w)
        w.pop()

    return 

dx = (-1,1,0,0)
dy = (0,0,-1,1)

d = [input().split() for _ in range(5)]
st = set()

for i in range(5):
    for j in range(5):
        dfs(i,j,[d[i][j]])

print(len(st))
def check(loc):
    x,y = loc
    return 0<=x<n and 0<=y<m

def find(loc):
    res = 0
    for word in lst:
        for dir in range(8):
            x,y = loc
            if word[0] != d[x][y]: continue

            for i in (1,2,3):
                x += dx[dir]
                y += dy[dir]

                if not check((x,y)): break
                if word[i] != d[x][y]: break

            else:
                res += 1
            
    return res

def cal(idx):
    res = []
    for i in range(4):
        res.append(a[idx[i]][i])

    return res

a = ['ENFP','ISTJ']
lst = []
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                lst.append(cal((i,j,k,l)))

dx = (-1,1,0,0,-1,-1,1,1)
dy = (0,0,-1,1,-1,1,-1,1)

n,m = map(int,input().split())
d = [list(input()) for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        cnt += find((i,j))

print(cnt)
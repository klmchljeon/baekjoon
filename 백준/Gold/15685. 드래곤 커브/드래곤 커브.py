#드래곤 커브
def rotate(loc):
    x,y = loc
    return [-y,x]

def move(loc,di):
    x,y = loc
    return [x+di[0],y+di[1]]

def dc(dir,k=0):
    if k==0:
        return [[0,0],[dx[dir],dy[dir]]]
    
    res = dc(dir,k-1)
    dis = mi(*res[-1])
    
    tmp = []
    for i in res:
        tmp.append(move(i,dis))

    tmp = list(map(rotate,tmp))
    for i in range(len(tmp)):
        tmp[i] = move(tmp[i],res[-1])

    return res[:-1] + tmp[::-1]

def check():
    cnt = 0
    for i in range(100):
        for j in range(100):
            cnt += lst[i][j]&lst[i+1][j]&lst[i][j+1]&lst[i+1][j+1]
            
    return cnt

mi = lambda x,y:(-x,-y)

dx = (1,0,-1,0)
dy = (0,-1,0,1)

n = int(input())
lst = [[0]*101 for _ in range(101)]

for _ in range(n):
    x,y,d,g = map(int,input().split())
    
    tmp = dc(d,g)
    for i in tmp:
        nx,ny = move(i,(x,y))
        lst[nx][ny] = 1

print(check())
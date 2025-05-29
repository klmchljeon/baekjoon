dx = (0,0,-1,1,0)
dy = (-1,1,0,0,0)

def dist(p,q):
    x1,y1 = p
    x2,y2 = q
    return abs(x1-x2) + abs(y1-y2)

def gen(p):
    x,y = p
    res = []
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        res.append((nx,ny))

    return res

n = int(input())
x,y = map(int,input().split())
cur = [[(x,y),0] for _ in range(5)]
for i in range(n):
    x,y = map(int,input().split())
    nx = gen((x,y))

    tmp = []
    #이동할 점 각각
    for j in range(5):
        val = int(1e12)
        #현재 점 순회
        for i in range(5):
            # i -> j로
            val = min(val,dist(cur[i][0],nx[j]) + cur[i][1])            
    
        tmp.append([nx[j],val])

    cur = tmp

res = int(1e12)
for _,c in cur:
    res = min(res,c)

print(res)
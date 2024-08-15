dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())
lst = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    lst.append(tmp)

res = 0
for x in range(1,n-1):
    for y in range(1,m-1):
        
        cur = lst[x][y]
        p = int(1e9) + 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            p = min(p,lst[nx][ny])

        if cur <= p:
            res += max(0,cur-1)
        else:
            res += p
        
print(res)
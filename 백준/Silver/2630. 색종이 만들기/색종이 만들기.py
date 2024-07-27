def check(loc,size,c):
    x,y = loc
    if size == 0:
        return [lst[x][y]==c]*2
    
    s = 0
    flag = True
    for i in range(4):
        nx = x + size*dx[i]
        ny = y + size*dy[i]

        cnt,b = check((nx,ny),size//2,c)
        
        s += cnt
        flag &= b
        
    if flag:
        return 1,True
    else:
        return s,False

dx = (0,0,1,1)
dy = (0,1,0,1)

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]

res = [check((0,0),n//2,i)[0] for i in (0,1)]
print(*res, sep='\n')
def btc(loc,cnt):
    global res
    x,y = loc

    if x==10:
        res = min(res,cnt)
        return 
    
    if y==10:
        btc((x+1,0),cnt)
        return
    
    if lst[x][y] == 0:
        btc((x,y+1),cnt)
        return 
    
    for k in range(5,0,-1):
        if check((x,y),k) and d[k]:
            fill((x,y),k,0)
            d[k] -= 1

            btc((x,y+1),cnt+1)
            fill((x,y),k,1)
            d[k] += 1

    return 

def check(loc,size):
    x,y = loc
    for i in range(x,x+size):
        for j in range(y,y+size):
            if not (i<n and j<n and lst[i][j]==1):
                return False
        
    return True

def fill(loc,size,a):
    x,y = loc
    for i in range(x,x+size):
        for j in range(y,y+size):
            lst[i][j] = a

n = 10
max_ = 25
lst = [list(map(int,input().split())) for _ in range(n)]
res = max_
d = [5]*6
btc((0,0),0)
print(res if res!=max_ else -1)
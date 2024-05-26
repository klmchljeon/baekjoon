inf = int(1e10)
max_ = int(1e6)

def check(num):
    dist = [inf]*(n+1)
    dist[0] = 0
    
    for i in range(n+1):
        for x,nx,cost in edges:
            tmp = dist[x] + cost
            if tmp<=num and dist[nx]>tmp:
                if i == n:
                    return True

                dist[nx] = tmp
                
    return False

n,m = map(int,input().split())
edges = []

for _ in range(m):
    t,*order = map(int,input().split())
    t = int(t)
    if t == 1:
        cost,name = order
        edges.append((0,name,cost))

    elif t == 2:
        name,cost = order
        edges.append((name,0,-cost))

    elif t == 3:
        name1,name2 = order
        edges.append((name1,name2,0))

    elif t == 4:
        name1,cost,name2 = order
        edges.append((name1,name2,cost))

    elif t == 5:
        name1,name2,cost = order
        edges.append((name1,name2,-cost))

s,e = -1,max_
while s+1<e:
    mid = (s+e)//2
    
    if check(mid):
        e = mid

    else:
        s = mid

print(e if e!=max_ else 'INF')
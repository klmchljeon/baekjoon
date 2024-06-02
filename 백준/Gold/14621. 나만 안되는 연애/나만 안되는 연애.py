def find(x):
    if parent[x]==x: return x
    parent[x] = find(parent[x])
    return parent[x]

def merge(a,b):
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n,m = map(int,input().split())
lst = [0]+[i=='M' for i in input().split()]
edge = []
for _ in range(m):
    u,v,c = map(int,input().split())
    edge.append((c,u,v))

edge.sort()

parent = list(range(n+1))

res = 0
cnt = 0
for cost,x,y in edge:
    if lst[x]^lst[y] == 0: continue
    px = find(x)
    py = find(y)

    if px == py:
        continue

    merge(px,py)
    res += cost
    cnt += 1
    if cnt == n-1:
        print(res)
        break

else:
    print(-1)
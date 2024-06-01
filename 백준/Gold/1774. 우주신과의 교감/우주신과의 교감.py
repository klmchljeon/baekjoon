def find(x):
    if parent[x]==x: return x
    parent[x] = find(parent[x])
    return parent[x]

def merge(a,b):
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def cal(l1,l2):
    res = 0
    for p,q in zip(l1,l2):
        res += abs(p-q)**2

    return res**0.5

n,m = map(int,input().split())
lst = []
for _ in range(n):
    x,y = map(float,input().split())
    lst.append((x,y))

edge = []
for i in range(n-1):
    for j in range(i+1,n):
        edge.append((cal(lst[i],lst[j]),i,j))

edge.sort()

parent = list(range(n))

res = 0
cnt = 0
for _ in range(m):
    x,y = map(int,input().split())
    x-=1;y-=1
    
    px = find(x)
    py = find(y)
    if px == py:
        continue

    merge(px,py)
    cnt += 1

for c,x,y in edge:
    px = find(x)
    py = find(y)

    if px == py:
        continue

    merge(px,py)
    res += c
    cnt += 1
    if cnt == n-1:
        break

print(f'{res:.2f}')
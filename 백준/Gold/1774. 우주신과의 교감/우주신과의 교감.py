def find(x):
    if parent[x] == x: return x
    parent[x] = find(parent[x])
    return parent[x]

def merge(a,b):
    pa = find(a)
    pb = find(b)

    if pa < pb:
        parent[pb] = pa

    elif pa > pb:
        parent[pa] = pb

def dist(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

n,m = map(int,input().split())
lst = []
for _ in range(n):
    x,y = map(int,input().split())
    lst.append((x,y))

edge = []
for i in range(n-1):
    for j in range(i+1,n):
        edge.append((i+1,j+1,dist(lst[i],lst[j])))

parent = list(range(n+1))

for _ in range(m):
    a,b = map(int,input().split())
    merge(a,b)

st = set()
for i in range(1,n+1):
    st.add(find(i))

edge.sort(key = lambda x:x[2])

n = len(st)
cnt = 0
res = 0
for a,b,c in edge:
    pa = find(a)
    pb = find(b)

    if pa == pb:
        continue

    merge(a,b)
    cnt += 1
    res += c
    if cnt == n-1:
        print(f'{res:.2f}')
        break
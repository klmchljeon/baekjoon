#친구비
import sys
input = sys.stdin.readline

def find(x):
    if x != parent[x][0]: 
        parent[x] = find(parent[x][0])
    
    return parent[x]

def merge(a,b):
    pa = find(a)
    pb = find(b)
    tmp = min(pa[1],pb[1])

    if pa[0] < pb[0]:
        parent[pb[0]] = [pa[0],tmp]
        parent[pa[0]][1] = tmp
    else:
        parent[pa[0]] = [pb[0],tmp]
        parent[pb[0]][1] = tmp
    
    return

n,m,k = map(int,input().split())
d = [0]+list(map(int,input().split()))

parent = [[i,d[i]] for i in range(n+1)]

for i in range(m):
    u,v = map(int,input().split())
    merge(u,v)

st = set()
cost = 0
for i in range(1,n+1):
    tmp = find(i)
    if not tmp[0] in st:
        st.add(tmp[0])
        cost += tmp[1]

print(cost if cost <= k else "Oh no")
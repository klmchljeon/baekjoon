#도시 건설
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x: 
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

n,m = map(int,input().split())
cost = 0
edge = []
for _ in range(m):
    a,b,c = map(int,input().split())
    edge.append((a,b,c))
    cost += c

f = lambda x:x[2]
edge.sort(key = f)

parent = [i for i in range(n+1)]

res = 0
for a,b,w in edge:
    pa = find(a)
    pb = find(b)
    
    if pa != pb:
        res += w
        if pa < pb:
            parent[pb] = pa
        else:
            parent[pa] = pb

flag = True
for i in range(2,n+1):
    flag &= find(i) == 1

print(cost-res if flag else -1)
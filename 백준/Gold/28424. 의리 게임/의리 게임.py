import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(2e5))

def find(x):
    if parent[x] == x: return x
    parent[x] = find(parent[x])
    return parent[x]
    
def merge(a,b):
    pa = find(a)
    pb = find(b)
    
    if pa < pb:
        parent[pa] = pb
    
    else:
        parent[pb] = pa
    
n,q = map(int,input().split())
d = [0] + [int(input()) for _ in range(n)] + [0]
res = [0]*(n+2)

parent = list(range(n+2))

for query in range(q):
    m,*order = map(int,input().split())
    if m == 1:
        i,x = order
        while i < n+1:
            if d[i] > res[i] + x:
                res[i] += x
                break
            
            else:
                x -= d[i] - res[i]
                res[i] = d[i]
                merge(i,i+1)
                i = find(i)
    
    else:
        print(res[order[0]])
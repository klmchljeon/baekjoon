#트리의 색깔과 쿼리 24:34
import sys
sys.setrecursionlimit(int(2e5))
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def merge(a,b):
    pa = find(a)
    pb = find(b)

    if len(col[pa]) >= len(col[pb]):
        parent[pb] = pa
        for i in col[pb]:
            col[pa].add(i)

        col[pb].clear()

    else:
        parent[pa] = pb
        for i in col[pa]:
            col[pb].add(i)

        col[pa].clear()

    return 

n,q = map(int,input().split())
p = [0]*2 + [int(input()) for _ in range(n-1)]
parent = [i for i in range(n+1)]

col = [0] + [set([int(input())]) for _ in range(n)]

query = []
for _ in range(n+q-1):
    x,a = map(int,input().split())
    query.append((x,a))

query = query[::-1]

res = []
for x,a in query:
    if x==1:
        merge(a,p[a])

    else:
        res.append(len(col[find(a)]))

print(*res[::-1],sep='\n')
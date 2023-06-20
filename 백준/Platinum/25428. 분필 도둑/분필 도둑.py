#분필 도둑
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def merge(a,b,c):
    pa = find(a)
    pb = find(b)


    if pa < pb:
        parent[pb] = pa
    elif pa > pb:
        parent[pa] = pb
    else:
        return 
    
    val[pa] = c
    cnt[pa] += cnt[pb]
    
    val[pb] = c
    cnt[pb] = cnt[pa]

f = lambda x:-x[0]

n = int(input())
cost = [0]+list(map(int,input().split()))
d = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

lst = list(zip(cost[1:],range(1,n+1)))
lst.sort(key = f)

parent = [i for i in range(n+1)]
val = cost[:]
cnt = [1]*(n+1)

res = 0
visit = [False]*(n+1)
for v,x in lst:
    visit[x] = True
    for nx in d[x]:
        if visit[nx]:
            merge(x,nx,v)

    t = find(x)
    res = max(res,val[t]*cnt[t])

print(res)
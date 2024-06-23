import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

def find(x):
    if parent[x]==x:return x
    parent[x] = find(parent[x])
    return parent[x]

def merge(a,b):
    pa,pb = map(find,(a,b))
    if pa > pb:
        parent[pa] = pb
    else:
        parent[pb] = pa

n,q = map(int,input().split())
edge = []
for _ in range(q):
    tmp = list(map(int,input().split()))
    edge.append(tmp)

edge.sort(key = lambda x:(x[2],x[3]))

parent = list(range(n+1))

cnt = 0
res = 0
time = 0
for s,e,c,t in edge:
    ps,pe = map(find,(s,e))
    if ps == pe: continue
    merge(s,e)

    cnt += 1
    res += c
    time = max(time,t)

    if cnt == n-1:
        print(time,res)
        break

else:
    print(-1)
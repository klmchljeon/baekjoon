import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

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


n,m = map(int,input().split())
edge = []
for i in range(m):
    a,b,c = map(int,input().split())
    edge.append((c,a,b,i))

edge.sort()

parent = list(range(n+1))

cur = edge[0][0]
cnt = 0

res = [0]*m
tmp = []
for i in range(m):
    if edge[i][0] != cur:
        cur = edge[i][0]
        for a,b in tmp:
            pa = find(a)
            pb = find(b)

            if pa != pb:
                merge(pa,pb)
                cnt += 1

                if cnt == n-1:
                    break

        tmp = []

    _,a,b,idx = edge[i]
    pa = find(a)
    pb = find(b)

    if pa != pb:
        tmp.append((a,b))
        res[idx] = 1

for i in res:
    print('TAK' if i else 'NIE')
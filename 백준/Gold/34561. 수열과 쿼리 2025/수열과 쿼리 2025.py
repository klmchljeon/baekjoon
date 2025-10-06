import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(4e5))
max_ = 300000

def find(x):
    if parent[x] == x: return x
    parent[x] = find(parent[x])
    return parent[x]

def merge(a,b):
    pa = find(a)
    pb = find(b)

    parent[pb] = pa

n = int(input())
lst = list(map(int,input().split()))

parent = [i for i in range(n)]

val = [None]*(max_+1)
for i in range(n):
    if val[lst[i]] == None:
        val[lst[i]] = i

    merge(val[lst[i]],i)

m = int(input())
for _ in range(m):
    q,*order = map(int,input().split())
    if q == 1:
        x,y = order
        if val[x] == None: continue

        if val[y] == None:
            val[y] = val[x]
            lst[val[y]] = y
            val[x] = None

        else:
            merge(val[y],val[x])
            lst[val[y]] = y
            val[x] = None

    else:
        z = order[0] - 1
        print(lst[find(z)])
#Cost Of Subtree
import sys
sys.setrecursionlimit(2*10**5)
input = sys.stdin.readline

def find(x):
    if parent[x][0] == x:
        return parent[x]
    
    parent[x] = find(parent[x][0])
    return parent[x]

def merge(a,b,c):
    pa = find(a)
    pb = find(b)

    tmp = [None,c,pa[2]+pb[2]+1]
    if pa[0] < pb[0]:
        tmp[0] = pa[0]

    elif pa[0] > pb[0]:
        tmp[0] = pb[0]
    
    parent[pa[0]] = tmp
    parent[pb[0]] = tmp

f = lambda x:-x[2]

n = int(input())
d = []
for _ in range(n-1):
    a,b,c = map(int,input().split())
    d.append((a,b,c))

d.sort(key = f)

parent = [[i,0,0] for i in range(n+1)]

res = 0
for a,b,c in d:
    merge(a,b,c)

    t = find(a)
    res = max(res,t[1]*t[2])

print(res)
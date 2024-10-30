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

def check(p,q):
    dist = (p[0]-q[0])**2 + (p[1]-q[1])**2
    r = (p[2] + q[2])**2
    return r >= dist

t = int(input())
for case in range(t):
    n = int(input())
    lst = []
    for i in range(n):
        x,y,r = map(int,input().split())
        lst.append((x,y,r))

    parent = [i for i in range(n)]
    for i in range(n-1):
        for j in range(i+1,n):
            if check(lst[i],lst[j]):
                merge(i,j)

    v = [False]*n
    for i in range(n):
        v[find(i)] = True

    print(sum(v))
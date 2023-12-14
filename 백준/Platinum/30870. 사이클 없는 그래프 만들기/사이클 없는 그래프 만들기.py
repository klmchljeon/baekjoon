import sys
from collections import deque
sys.setrecursionlimit(int(2e5))
input = sys.stdin.readline

def find(x):
    if x == pa[x]: return x
    pa[x] = find(pa[x])
    return pa[x]

def merge(a,b):
    if a < b:
        pa[b] = a

    elif a > b:
        pa[a] = b

def check(num):

    for i in range(1,n+1):
        pa[i] = i

    for i in range(1,n+1):
        if visit[i] <= num:
            continue

        for j in d[i]:
            if i > j or visit[j] <= num:
                continue


            pi = find(i)
            pj = find(j)

            if pi == pj:
                return False
            
            merge(pi,pj)

    return True

n,m,k = map(int,input().split())
d = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    d[u].append(v)
    d[v].append(u)

p = list(map(int,input().split()))

visit = [0]*(n+1)
for i in p:
    visit[i] = 1

queue = deque([*p])
while queue:
    x = queue.popleft()

    for nx in d[x]:
        if not visit[nx]:
            visit[nx] = visit[x] + 1
            queue.append(nx)

pa = [0]*(n+1)

s,e = 0,n
while s+1<e:
    mid = (s+e)//2

    if check(mid):
        e = mid
    
    else:
        s = mid

print(e)
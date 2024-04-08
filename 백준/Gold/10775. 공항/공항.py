#공항
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(2e5))

def merge(a,b):
    pa = find(a)
    pb = find(b)
    parent[pa] = pb

def find(x):
    if parent[x]==x: return x
    parent[x] = find(parent[x])
    return parent[x]

g = int(input())
p = int(input())
lst = [int(input()) for _ in range(p)]

parent = list(range(g+1))

for i in range(p):
    t = find(lst[i])
    if t == 0:
        print(i)
        break

    merge(t,t-1)
    
else:
    print(p)
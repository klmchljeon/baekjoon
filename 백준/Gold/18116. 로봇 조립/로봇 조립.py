import sys
input = sys.stdin.readline
t = 10**6

def find(x):
    if parent[x] == x:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def merge(a,b):
    pa = find(a)
    pb = find(b)

    if pa < pb:
        parent[pb] = pa
        size[pa] += size[pb]

    elif pb < pa:
        parent[pa] = pb
        size[pb] += size[pa]

parent = [i for i in range(t+1)]
size = [1]*(t+1)

n = int(input())
for _ in range(n):
    q,*order = input().split()
    if q=='I':
        a,b = map(int,order)
        merge(a,b)
    else:
        a = int(order[0])
        print(size[find(a)])
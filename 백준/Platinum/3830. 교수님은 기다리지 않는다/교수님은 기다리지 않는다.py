#교수님은 기다리지 않는다
import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

def find(x,wei = 0):
    if parent[x][0] == x:
        return x,wei
    
    tmp = find(parent[x][0],parent[x][1] + wei)
    parent[x] = (tmp[0],tmp[1]-wei)

    return tmp

def merge(a,b,w):
    pa,weia = find(a)
    pb,weib = find(b)

    if pa < pb:
        parent[pb] = (pa,weia+w-weib)
    elif pa > pb:
        parent[pa] = (pb,weib-w-weia)

    return 

while True:
    n,m = map(int,input().split())
    if not n: break

    parent = [(i,0) for i in range(n+1)]

    for query in range(m):
        q,*order = input().split()
        if q == '!':
            a,b,w = map(int,order)
            merge(a,b,w)

        else:
            a,b = map(int,order)
            pa,weia = find(a)
            pb,weib = find(b)
            if pa == pb:
                print(weib-weia)
            else:
                print('UNKNOWN')
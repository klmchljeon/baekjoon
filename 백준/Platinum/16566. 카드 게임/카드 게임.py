#카드 게임
def ub(num):
    s,e = -1,m-1
    while s+1<e:
        mid = (s+e)//2

        if d[mid] > num:
            e = mid

        else:
            s = mid

    return e

def find(x):
    if parent[x] == x:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def merge(a,b):
    pa = find(a)
    pb = find(b)

    if pa < pb: 
        parent[pa] = pb
    else:
        parent[pb] = pa

n,m,k = map(int,input().split())
d = sorted(map(int,input().split()))
d.append(n+1)

ilst = [-1]*(n+2)
for i in range(m):
    ilst[d[i]] = i

lst = list(map(int,input().split()))

parent = [i for i in range(n+2)]

res = [None]*k
for i in range(k):
    idx = ub(lst[i])
    tmp = find(d[idx])
    res[i] = tmp

    merge(d[ilst[tmp]],d[ilst[tmp]+1])

print(*res,sep='\n')
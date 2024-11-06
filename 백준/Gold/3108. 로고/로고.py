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

def overlap(a,b):
    if a[0] > b[0]:
        a,b = b,a

    return a[1]-b[0]

def contain(a,b):
    p = a[0] < b[0] and b[2] < a[2]
    q = a[1] < b[1] and b[3] < a[3]
    return p and q

def check(a,b):
    p = overlap((a[0],a[2]),(b[0],b[2]))
    q = overlap((a[1],a[3]),(b[1],b[3]))

    if p < 0 or q < 0:
        return False
    
    if contain(a,b) or contain(b,a):
        return False
    
    return True

n = int(input())
lst = [(0,0,0,0)]
for _ in range(n):
    lst.append(tuple(map(int,input().split())))

parent = [i for i in range(n+1)]
for i in range(n):
    for j in range(i+1,n+1):
        if check(lst[i],lst[j]):
            merge(i,j)

v = [0]*(n+1)
for i in range(n+1):
    v[find(i)] = 1

print(sum(v)-1)
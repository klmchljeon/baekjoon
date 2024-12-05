#여행 가자
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

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]

for i in range(1,n+1):
    tmp = [0] + list(map(int,input().split()))
    for j in range(1,n+1):
        if i==j: continue
        if tmp[j]:
            merge(i,j)

d = list(map(int,input().split()))
res = True
for i in d:
    res &= find(d[0]) == find(i)

print('YES' if res else 'NO')
import sys
input = sys.stdin.readline
sys.setrecursionlimit(30000)

def find(x):
    if parent[x] == x: return x
    parent[x] = find(parent[x])
    return parent[x]

def merge(a,b):
    pa = find(a)
    pb = find(b)

    if pa < pb:
        parent[pa] = pb

    elif pa > pb:
        parent[pb] = pa

    return 

n = int(input())
d = []
st = set()
for _ in range(n):
    a,b = map(int,input().split())
    d.append((a,b))
    st.add(a)
    st.add(b)

lst = sorted(st)
dic = dict(zip(lst,range(len(lst))))

for i in range(n):
    a,b = d[i]
    d[i] = (dic[a],dic[b])

m = len(lst)
parent = [i for i in range(m+1)]

res = [-1]*(m+1)
for i in range(n-1,-1,-1):
    a,b = d[i]
    idx = a
    while idx <= b:
        if res[idx] == -1:
            res[idx] = i
            merge(idx,idx+1)
            idx += 1

        else:
            idx = find(idx)

print(len(set(res[:-1])))
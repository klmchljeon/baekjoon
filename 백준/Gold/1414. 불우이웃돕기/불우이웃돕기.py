def conv(x):
    if 'a' <= x <= 'z':
        return ord(x) - ord('a') + 1

    else:
        return ord(x) - ord('A') + 26 + 1

def find(x):
    if parent[x] == x: return x
    parent[x] = find(parent[x])
    return parent[x]

def merge(a,b):
    if a < b:
        parent[b] = a
    
    else:
        parent[a] = b

n = int(input())
if n == 1:
    tmp = input()
    print(conv(tmp) if tmp!='0' else 0)
    exit()

edge = []
res = 0
for i in range(n):
    st = input()
    for j in range(n):
        if st[j] == '0': continue
        c = conv(st[j])
        res += c

        if i==j: continue
        edge.append((i,j,conv(st[j])))

parent = list(range(n))
cnt = 0

edge.sort(key = lambda x:x[2])
for a,b,c in edge:
    pa = find(a)
    pb = find(b)

    if pa != pb:
        merge(pa,pb)
        cnt += 1
        res -= c

if cnt == n-1:
    print(res)
else:
    print(-1)
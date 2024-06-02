import sys
input = sys.stdin.readline

def find(n):
    if parent[n] == n: return n
    return find(parent[n])

v,e,t = map(int,input().split())
parent = [i for i in range(v+1)]
d = []
for i in range(e):
    d.append(list(map(int,input().split())))

d.sort(key = lambda x:x[2])

result = 0
for a,b,c in d:
    pa = find(a)
    pb = find(b)

    if pa!=pb:
        if pa>pb:
            parent[pa] = pb
        else:
            parent[pb] = pa
            
        result += c

print(result + t * ((v-1)*(v-2)//2))
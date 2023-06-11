#N과 M (7)
def dfs():
    if len(s) == m:
        print(*s)
        return
    
    for i in range(n):
        s.append(d[i])
        dfs()
        s.pop()

n,m = map(int,input().split())
d = list(map(int,input().split()))
d.sort()

s = []
dfs()
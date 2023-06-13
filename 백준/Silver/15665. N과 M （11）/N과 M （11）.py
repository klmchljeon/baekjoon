#N과 M (11)
def dfs():
    if len(s) == m:
        print(*s)
        return 
    
    for i in d:
        s.append(i)
        dfs()
        s.pop()

n,m = map(int,input().split())
d = set(map(int,input().split()))

d = sorted(d)
n = len(d)

s = []
dfs()
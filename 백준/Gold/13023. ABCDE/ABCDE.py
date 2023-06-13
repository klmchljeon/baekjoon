#ABCDE 16:13
import sys
sys.setrecursionlimit(3000)
input = sys.stdin.readline

def dfs(x,st:set):
    global res
    if res: return 
    
    for nx in d[x]:
        if not nx in st:
            st.add(nx)
            if len(st) == 5:
                res = 1
                return 
            
            dfs(nx,st)
            st.remove(nx)

    return 

n,m = map(int,input().split())
d = [[] for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

res = 0
for i in range(n):
    dfs(i,set([i]))

print(res)
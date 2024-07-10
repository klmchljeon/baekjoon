import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(2e5))

def move(a,b):
    lst[a] ^= 1
    res.append(b)

def dfs(x):
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True

            #nx로 감
            move(x,nx)

            #nx에서부터 이동, 다시 nx로 돌아옴
            dfs(nx)

            #nx가 0이면 왔다갔다
            if not lst[nx]:
                move(nx,x)
                move(x,nx)

            #x로 가고, nx는 1이 됨
            move(nx,x)

n,a = map(int,input().split())
lst = [0] + list(map(int,input().rstrip()))
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False]*(n+1)
visited[a] = True

res = []
dfs(a)
if lst[a]:
    move(a,graph[a][0])

if len(res) > 4*n or not res[0] in graph[a]:
    raise AssertionError

for i in range(1,len(res)):
    if res[i-1] in graph[res[i]]: continue
    raise AssertionError

for i in lst:
    if not i: continue
    raise AssertionError

print(len(res))
print(*res)
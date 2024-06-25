import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(2e5))

def inorder(x):
    global res
    if graph[x][0] != -1:
        res += 1
        inorder(graph[x][0])

    if graph[x][1] != -1:
        res += 1
        inorder(graph[x][1])

    res += 1

def lastord(x):
    global res
    if graph[x][1] != -1:
        lastord(graph[x][1])

    res -= 1

n = int(input())
graph = [None for _ in range(n+1)]
for _ in range(n):
    a,b,c = map(int,input().split())
    graph[a] = (b,c)

visited = [False]*(n+1)

res = 0
inorder(1)
lastord(1)

print(res)
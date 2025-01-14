import sys
sys.setrecursionlimit(int(1e6))

def dfs(x):
    nx = (x+k)%n
    if v[nx] == -1:
        v[nx] = v[x]
        dfs(nx)

n,k = map(int,input().split())
lst = list(map(int,input().split()))
v = [-1]*n
for i in range(n):
    if v[i] == -1:
        v[i] = i
        dfs(i)

tmp = list(zip(lst,v))
tmp.sort()

for i in range(n):
    if tmp[i][1] != v[i]:
        print('NO')
        break

else:
    print('YES')
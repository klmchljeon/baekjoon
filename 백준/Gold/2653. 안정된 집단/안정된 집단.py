def dfs(x):
    d = [x]
    for nx in range(n):
        if not visited[nx] and lst[x][nx] == 0:
            visited[nx] = True
            d += dfs(nx)

    return d

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]

visited = [False]*n
res = []
for i in range(n):
    if not visited[i]:
        visited[i] = True
        res.append(dfs(i))

flag = True
for idx in range(len(res)):
    flag &= len(res[idx]) >= 2

for i in range(n):
    for j in range(n):
        flag &= lst[i][j] == lst[j][i]

if not flag:
    print(0)
    exit()

print(len(res))
for i in res:
    print(*map(lambda x:x+1,sorted(i)))
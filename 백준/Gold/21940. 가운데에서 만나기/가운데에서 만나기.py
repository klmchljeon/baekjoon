inf = int(1e9)

n,m = map(int,input().split())
lst = [[inf]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    lst[a][b] = c

for i in range(1,n+1):
    lst[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            lst[i][j] = min(lst[i][j], lst[i][k]+lst[k][j])

k = int(input())
d = list(map(int,input().split()))
num = inf
res = []
for i in range(1,n+1):
    tmp = 0
    for j in d:
        tmp = max(tmp, lst[i][j]+lst[j][i])

    if num == tmp:
        res.append(i)
    elif num > tmp:
        num = tmp
        res = [i]

print(*res)
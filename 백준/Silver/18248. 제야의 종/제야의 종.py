#제야의 종
n,m = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(n)]
idx = [[0,i] for i in range(n)]

for i in range(n):
    for j in range(m):
        if d[i][j]:
            idx[i][0] += 1

idx.sort(reverse=True)

flag = True
tmp = [True]*m
for _,i in idx:
    for j in range(m):
        if not tmp[j] and d[i][j]:
            flag = False

        tmp[j] &= bool(d[i][j])

print('YES' if flag else 'NO')
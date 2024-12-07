n,k = map(int,input().split())
lst = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    lst.append(tmp)

res = [[0]*(n*k) for _ in range(n*k)]
for i in range(n):
    for j in range(n):
        for x in range(i*k,i*k+k):
            for y in range(j*k,j*k+k):
                res[x][y] = lst[i][j]

for i in res:
    print(*i)
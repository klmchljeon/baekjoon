n,m = map(int,input().split())
a,b = map(int,input().split())

lst = [[j=='#' for j in input()] for _ in range(n)]

res = int(1e9)
for k in range(1,7):
    for x in range(n-3*k+1):
        for y in range(m-3*k+1):
            tmp = [[0]*m for _ in range(n)]
            for i in range(3):
                for j in range(3):
                    if i==1 and j>0: continue

                    for ii in range(k):
                        for jj in range(k):
                            tmp[x+i*k+ii][y+j*k+jj] = 1

            cost = 0
            for i in range(n):
                for j in range(m):
                    if lst[i][j] == tmp[i][j]: continue

                    cost += a if tmp[i][j] else b

            res = min(res,cost)

print(res)
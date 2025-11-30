dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())
tmpp = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    tmpp.append(tmp)

r1,c1,r2,c2 = map(int,input().split())
tmpp[r1-1][c1-1],tmpp[r2-1][c2-1] = tmpp[r2-1][c2-1],tmpp[r1-1][c1-1]

lst = [[None]*n for _ in range(m)]
for i in range(n):
    for j in range(m):
        lst[j][n-i-1] = tmpp[i][j]

n,m = m,n

cnt = 0

activate = [[False]*m for _ in range(n)]
while True:
    flag = False
    check = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(1,m-1):
            if lst[i][j] <= 0: continue

            if lst[i][j] == lst[i][j+1] == lst[i][j-1]:
                check[i][j] = True
                check[i][j+1] = True
                check[i][j-1] = True
                flag = True

    for j in range(m):
        for i in range(1,n-1):
            if lst[i][j] <= 0: continue

            if lst[i][j] == lst[i+1][j] == lst[i-1][j]:
                check[i][j] = True
                check[i+1][j] = True
                check[i-1][j] = True
                flag = True
    
    nlst = []
    for i in range(n):
        tmp = []
        c = False #c가 True가 된 시점부터는 모두 내려옴. 따라서 폭탄을 재배치
        for j in range(m):
            if check[i][j]: 
                c = True
                cnt += 1
                continue

            if c:
                activate[i][len(tmp)] = False
                activate[i][len(tmp)] |= lst[i][j] == 0

            tmp.append(lst[i][j])

        tmp += [-2]*(m - len(tmp))
        nlst.append(tmp)

    for i in range(n):
        lst[i] = nlst[i]

    if flag: continue
    
    flag2 = False
    check2 = [[False]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if not activate[x][y]: continue

            flag2 = True
            check2[x][y] = True
            for i in range(4):
                k = 1
                while True:
                    nx = x + k*dx[i]
                    ny = y + k*dy[i]

                    if not (0 <= nx < n and 0 <= ny < m): break
                    if lst[nx][ny] == -1: break

                    if lst[nx][ny] != -2:
                        check2[nx][ny] = True

                    k += 1

    if not flag2:
        break

    activate = [[False]*m for _ in range(n)]
    nlst = []
    for i in range(n):
        tmp = []
        c = False #c가 True가 된 시점부터는 모두 내려옴. 따라서 폭탄을 재배치
        for j in range(m):
            if check2[i][j]: 
                c = True
                flag2 = True
                cnt += 1
                continue

            if c:
                activate[i][len(tmp)] = False
                activate[i][len(tmp)] |= lst[i][j] == 0
                
            tmp.append(lst[i][j])

        tmp += [-2]*(m - len(tmp))
        nlst.append(tmp)

    for i in range(n):
        lst[i] = nlst[i]

print(cnt)
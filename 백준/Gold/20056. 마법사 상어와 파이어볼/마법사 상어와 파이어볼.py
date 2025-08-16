dx = (-1,-1,0,1,1,1,0,-1)
dy = (0,1,1,1,0,-1,-1,-1)

p = ((1,3,5,7),(0,2,4,6))

n,m_,k = map(int,input().split())
lst = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m_):
    r,c,m,s,d = map(int,input().split())
    r -= 1; c -= 1
    lst[r][c].append((m,s,d))

for _ in range(k):
    tmp = [[None]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            for m,s,i in lst[x][y]:
                nx = (x + dx[i]*s)%n
                ny = (y + dy[i]*s)%n
                if tmp[nx][ny] == None:
                    tmp[nx][ny] = [m,s,1,[i,True]]

                else:
                    tmp[nx][ny][0] += m
                    tmp[nx][ny][1] += s
                    tmp[nx][ny][2] += 1
                    tmp[nx][ny][3][1] &= i%2 == tmp[nx][ny][3][0]%2

    for x in range(n):
        for y in range(n):
            lst[x][y] = []
            if tmp[x][y] == None:
                continue

            m,s,cnt,d = tmp[x][y]
            if cnt == 1:
                lst[x][y].append((m,s,d[0]))
                continue

            nm = m//5
            if nm == 0: continue

            ns = s//cnt
            for i in p[d[1]]:
                lst[x][y].append((nm,ns,i))

res = 0
for x in range(n):
    for y in range(n):
        for m,*_ in lst[x][y]:
            res += m

print(res)
n,m,r,c = map(int,input().split())
lst = []
for i in range(n):
    tmp = list(map(int,input().split()))
    lst.append(tmp)

p = []
for i in range(r):
    tmp = list(map(int,input().split()))
    p.append(tmp)

cnt = 0
for x in range(n-r+1):
    for y in range(m-c+1):
        k = lst[x][y]-p[0][0]
        flag = True
        for i in range(r):
            for j in range(c):
                flag &= lst[x+i][y+j]-p[i][j]==k

        cnt += flag

print(cnt)
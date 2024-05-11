def f(n, start):
    r, c = start
    if n == 1:
        w[r][c] = '*'
        return 
    
    nxtn = n//3
    for i,j in idx:
        nr = r+i*(nxtn)
        nc = c+j*(nxtn)
        f(nxtn, (nr,nc))

N = int(input())

w = [[' ']*N for i in range(N)]
idx = []
for i in range(3):
    for j in range(3):
        if i==1 and j==1: continue

        idx.append((i,j))

f(N, (0,0))

for i in range(N):
    for j in range(N):
        print(w[i][j], end='')
    print()
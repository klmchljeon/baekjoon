#내가 살게, 아냐 내가 살게
n,m,k = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(n)]

lst = [0]*n
for j in range(m):
    for i in range(n):
        lst[i] += d[i][j]
        if lst[i] >= k:
            print(i+1,j+1)
            exit()
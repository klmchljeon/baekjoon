n,m = map(int,input().split())
lst = [list(map(int,input())) for _ in range(n)]
res = False
for i in range(n-1):
    for j in range(m-1):
        res |= (lst[i][j]+lst[i+1][j]+lst[i][j+1]+lst[i+1][j+1])==4
        
print(int(res))
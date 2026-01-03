n,m = map(int,input().split())
lst = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    lst.append(tmp)

if n%2!=0 and m%2!=0:
    print('No')
    exit()

print('Yes')
if n%2 == 0:
    for i in range(0,n,2):
        for j in range(m):
            lst[i][j],lst[i+1][j] = lst[i+1][j],lst[i][j]

elif m%2 == 0:
    for j in range(0,m,2):
        for i in range(n):
            lst[i][j],lst[i][j+1] = lst[i][j+1],lst[i][j]

for i in lst:
    print(*i)
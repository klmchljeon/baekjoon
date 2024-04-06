#상어 초등학교
dx = (-1,1,0,0)
dy = (0,0,-1,1)

def cal(loc,p):
    x,y = loc
    cntf = 0
    cnte = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0<=nx<n and 0<=ny<n):
            continue

        if lst[nx][ny] == None:
            cnte += 1

        else:
            cntf += lst[nx][ny] in fav[p]

    return [cntf,cnte,(x,y)]

def max_(a,b):
    if a[0]!=b[0]:
        return a if a[0]>b[0] else b
    
    if a[1]!=b[1]:
        return a if a[1]>b[1] else b

    if a[2][0]!=b[2][0]: 
        return a if a[2][0]<b[2][0] else b
    
    return a if a[2][1]<b[2][1] else b

def score(m):
    if m == 0:
        return 0
    
    return 10**(m-1)

n = int(input())
order = []
fav = [None]*(n**2+1)

for _ in range(n**2):
    num,*d = map(int,input().split())
    fav[num] = d
    order.append(num)

res = 0

lst = [[None]*n for _ in range(n)]
for num in order:

    tmp = [-1,-1,(n+1,n+1)]
    for i in range(n):
        for j in range(n):
            if lst[i][j]!=None:
                continue
            
            k = cal((i,j),num)

            tmp = max_(tmp,k)

    x,y = tmp[2]
    lst[x][y] = num


res = 0
for i in range(n):
    for j in range(n):
        k = cal((i,j),lst[i][j])
        res += score(k[0])

print(res)
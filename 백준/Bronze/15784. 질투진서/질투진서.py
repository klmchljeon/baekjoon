dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,a,b = map(int,input().split())
lst = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    lst.append(tmp)

x,y = a-1,b-1
p = lst[a-1][b-1]

flag = True
for i in range(4):
    k = 1
    while True:
        nx = x + k*dx[i]
        ny = y + k*dy[i]

        if 0<=nx<n and 0<=ny<n:
            if p < lst[nx][ny]:
                flag = False
        else:
            break

        k += 1

print('HAPPY' if flag else 'ANGRY')
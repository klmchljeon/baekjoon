def dist(loc):
    a,b = loc
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

n,m = map(int,input().split())
lst = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    lst.append(tmp)

loc = []
for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:
            loc.append((i,j))

print(dist(loc))
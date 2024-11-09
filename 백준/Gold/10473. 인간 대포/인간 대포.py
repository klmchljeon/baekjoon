inf = 1e9

def cal(a,b):
    p = dist(a,b)**0.5
    t1 = p / 5
    t2 = 2 + (abs(p-50) / 5)
    return min(t1,t2)

def dist(a,b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

s = tuple(map(float,input().split()))
e = tuple(map(float,input().split()))

n = int(input())
lst = []
for i in range(n):
    x,y = map(float,input().split())
    lst.append((x,y))

d = [[inf]*(n+2) for _ in range(n+2)]
for i in range(n):
    for j in range(n):
        d[i+1][j+1] = cal(lst[i],lst[j])

for j in range(n):
    for i,loc in ((0,s),(n+1,e)):
        d[i][j+1] = dist(loc,lst[j])**0.5 / 5
        d[j+1][i] = cal(loc,lst[j])

d[0][n+1] = dist(s,e)**0.5 / 5
d[n+1][0] = dist(s,e)**0.5 / 5

for k in range(n+2):
    for i in range(n+2):
        for j in range(n+2):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

print(d[0][n+1])
loc = tuple(map(int,input().split()))

n = int(input())
res = int(1e9)
p = None
for i in range(n):
    x,y = map(int,input().split())
    dist = abs(loc[0]-x) + abs(loc[1]-y)
    if res > dist:
        res = dist
        p = (x,y)

print(*p)
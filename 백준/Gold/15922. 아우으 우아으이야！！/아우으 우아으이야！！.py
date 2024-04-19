import sys
input = sys.stdin.readline

n = int(input())
d = []
for _ in range(n):
    x,y = map(int,input().split())
    d.append((x,y))

res = 0
tmp = -int(1e11)
tail = tmp
for h,t in d:
    if tail < h:
        res += tail - tmp
        tmp = h
        tail = t
    else:
        tail = max(tail,t)

res += tail - tmp
print(res)
import sys
input = sys.stdin.readline

x,y = map(int,input().split())
up = [-1]*(x+1)
down = [0]*(x+1)

n = int(input())
lst = []
u,d = 0,0
for _ in range(n):
    a,b = map(int,input().split())
    lst.append((a,b))

    if up[a] == -1:
        u += 1

    up[a] = max(up[a],b)

lst.sort(key = lambda x:x[1])

val = x-1
for i in up:
    val += max(0,i)*2

idx = 0
res = val
for i in range(1,y):
    tmp = []
    while idx < n and lst[idx][1] < i:
        tmp.append(lst[idx])
        idx += 1

    for a,b in tmp:
        if down[a] == 0:
            down[a] = 1
            d += 1

        if up[a] == b:
            up[a] = -1
            u -= 1

    val += d*2
    val -= u*2
    res = min(res,val)

print(res)
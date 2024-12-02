import sys
input = sys.stdin.readline

n,q = map(int,input().split())
lst = []
for _ in range(n):
    a,b = map(int,input().split())
    lst.append((a,b))

lst.sort()

for _ in range(q):
    u,v,x,y = map(int,input().split())

    s,e = -1,n-1
    while s+1<e:
        mid = (s+e)//2

        if lst[mid][0] >= u:
            e = mid

        else:
            s = mid

    idx = e
    cnt = 0
    while idx < n and lst[idx][0] <= v:
        cnt += x<=lst[idx][1]<=y
        idx += 1

    print(cnt)
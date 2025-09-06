import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = []
for _ in range(n):
    a,b = map(int,input().split())
    lst.append((a,b))

for _ in range(m):
    g,x,y = map(int,input().split())
    cnt = 0
    for a,b in lst:
        cnt += x<=a and y<=b and (a+b<=g)

    print(cnt)
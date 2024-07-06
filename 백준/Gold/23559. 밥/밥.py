import sys
input = sys.stdin.readline

n,x = map(int,input().split())
lst = []
for _ in range(n):
    a,b = map(int,input().split())
    lst.append((a,b))

lst.sort(key = lambda x:-(x[0]-x[1]))

cnt = (x - (1000)*n) // 4000

res = 0
for a,b in lst:
    if b >= a:
        res += b

    else:
        if cnt > 0:
            cnt -= 1
            res += a

        else:
            res += b

print(res)
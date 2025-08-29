import sys
input = sys.stdin.readline

n,k,l = map(int,input().split())
res = []
for _ in range(n):
    a,b,c = map(int,input().split())
    for i in (a,b,c):
        if i < l:
            break

    else:
        if a+b+c >= k:
            res.append(a)
            res.append(b)
            res.append(c)

print(len(res)//3)
print(*res)
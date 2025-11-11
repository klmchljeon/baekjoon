p,m,c = map(int,input().split())
x = int(input())
res = int(1e18)
for i in range(1,p+1):
    for j in range(1,m+1):
        for k in range(1,c+1):
            res = min(res,abs((i+j)*(j+k)-x))

print(res)
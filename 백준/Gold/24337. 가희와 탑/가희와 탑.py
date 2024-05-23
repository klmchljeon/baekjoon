n,a,b = map(int,input().split())
if a+b > n+1:
    print(-1)
    exit()

one = n+1 - (a+b)

res = [1]*one
for i in range(1,a+1):
    res.append(i)

if a < b:
    if a == 1:
        res[0] = b

    else:
        res[-1] = b

for i in range(b-1,0,-1):
    res.append(i)

print(*res)
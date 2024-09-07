n,x1,y1,x2,y2 = map(int,input().split())

x,y = x2-x1,y2-y1
if x < 0 or y < 0:
    print(-1)
    exit()

if y == 0:
    print('R'*n)
    exit()

if x == 0:
    if y < n:
        print('U'*y + 'R'*(n-y))
    else:
        print('U'*n)

    exit()

res = 'U'*100
px,py = x,y
for i in range(1,n):
    j = n - i
    x,y = px,py

    m = min(x//i,y//j)
    x -= m*i
    y -= m*j

    if x > i or y > j:
        continue

    res = min(res,'R'*x + 'U'*y + 'R'*(i-x) + 'U'*(j-y))

print(res if res!='U'*100 else -1)

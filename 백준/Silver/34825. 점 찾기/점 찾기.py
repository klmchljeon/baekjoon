x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
a = x2-x1
b = y2-y1
tmp = abs(a) + abs(b)
if tmp%2 == 1:
    print(-1)
    exit()

if tmp == 0:
    print(x1,y1)
    exit()

k = tmp//2
if abs(a) >= k:
    print(x2-k*(a//abs(a)),y2)
else:
    print(x2,y2-k*(b//abs(b)))
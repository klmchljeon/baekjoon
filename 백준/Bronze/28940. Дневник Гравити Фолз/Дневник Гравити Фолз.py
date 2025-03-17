w,h = map(int,input().split())
n,a,b = map(int,input().split())

cnt = (w//a)*(h//b)
if cnt == 0:
    print(-1)
else:
    print(n//cnt + bool(n%cnt))
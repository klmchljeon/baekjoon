#대회 or 인턴
n,m,k = map(int,input().split())

t = min(n//2,m)
tmp = n+m - t*3 - k

if tmp >= 0:
    print(t)
else:
    tmp = -tmp
    t -= tmp//3 + (tmp%3!=0)
    print(t)
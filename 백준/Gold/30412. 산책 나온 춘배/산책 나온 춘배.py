inf = int(1e10)

n,x = map(int,input().split())
lst = [-inf] + list(map(int,input().split())) + [-inf]

res = inf
for i in range(1,n+1):
    a,b,c = lst[i],lst[i+1],lst[i-1]
    if b>c: b,c = c,b

    #a가 고정
    p1 = max(0,a+x-b) + max(0,a+x-c)

    #a만 증가
    p2 = max(0,c+x-a)

    #a,c 증가
    tmp = max(0,b+x-a)
    a += tmp
    p3 = tmp + max(0,a+x-c)

    res = min(res,p1,p2,p3)

print(res)
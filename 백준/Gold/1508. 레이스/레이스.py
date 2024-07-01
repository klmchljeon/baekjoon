def check(num):
    res = [0]*k
    res[0] = 1

    prev = lst[0]
    cnt = 1
    for i in range(1,k):
        if lst[i] - prev >= num:
            prev = lst[i]
            res[i] = 1
            cnt += 1

            if cnt == m:
                return True,res
            
    return False,None

n,m,k = map(int,input().split())
lst = list(map(int,input().split()))

s,e = 0,n+1
res = None
while s+1<e:
    mid = (s+e)//2

    tmp = check(mid)
    if tmp[0]:
        s = mid
        res = tmp[1]
    else:
        e = mid

print(*res,sep='')
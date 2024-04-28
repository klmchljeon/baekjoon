def bt(depth,cnt):
    global res
    if depth == n+1:
        res += cnt
        return 
    
    k = depth
    for i in (0,1,2):
        if d[i] >= k:
            d[i] -= k
            bt(depth+1,cnt)
            d[i] += k

    if depth%2 == 0:
        k = depth//2
        for i,j in ((0,1),(0,2),(1,2)):
            if d[i] >= k and d[j] >= k:
                d[i] -= k
                d[j] -= k
                bt(depth+1,cnt*c[depth][1])
                d[i] += k
                d[j] += k

    if depth%3 == 0:
        k = depth//3
        flag = True
        for i in (0,1,2):
            flag &= d[i]>=k

        if flag:
            for i in (0,1,2):
                d[i] -= k
            bt(depth+1,cnt*c[depth][2])
            for i in (0,1,2):
                d[i] += k

    return

res = 0
n,*d = map(int,input().split())

f = [1]*(n+1)
for i in range(2,n+1):
    f[i] = f[i-1]*i

c = [[1] for _ in range(n+1)]
for i in range(1,n+1):
    if i%2 == 0:
        c[i].append(f[i]//(f[i//2]**2))
    else:
        c[i].append(0)

    if i%3 == 0:
        c[i].append(f[i]//(f[i//3]**3))
    else:
        c[i].append(0)

bt(1,1)
print(res)
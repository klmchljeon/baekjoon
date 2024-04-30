n = int(input())
d = list(map(int,input().split()))
d.sort()

res = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        s,e = j,n-1
        while s+1<e:
            mid = (s+e)//2

            if d[mid] >= -(d[i]+d[j]):
                e = mid
            else:
                s = mid

        lower = e

        s,e = j+1,n
        while s+1<e:
            mid = (s+e)//2

            if d[mid] <= -(d[i]+d[j]):
                s = mid
            else:
                e = mid

        upper = s
        
        if d[lower]!=d[upper]: continue
        if d[lower]+d[i]+d[j] != 0: continue
        res += upper - lower + 1

print(res)
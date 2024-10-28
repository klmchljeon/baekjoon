n,m = map(int,input().split())
lst = list(map(int,input().split()))

res = int(1e18)
for k in range(m,n+1):
    for i in range(n-k+1):
        s = 0
        for j in range(i,i+k):
            s += lst[j]

        mean = s
        v = 0
        for j in range(i,i+k):
            v += (k*lst[j]-mean)**2

        tmp = (v/k**3)**0.5
        res = min(res,tmp)

print(res)
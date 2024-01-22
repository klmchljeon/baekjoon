n,k,p = map(int,input().split())
d = list(map(int,input().split()))
res = 0
for i in range(0,n*k,k):
    cnt = 0
    for idx in range(i,i+k):
        cnt += d[idx]==0

    res += cnt < p

print(res)
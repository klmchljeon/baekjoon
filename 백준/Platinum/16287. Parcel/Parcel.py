#Parcel
w,n = map(int,input().split())
d = list(map(int,input().split()))
d.sort()

dp = [False]*w
for i in range(n):
    for j in range(i+1,n):
        tar = w - (d[i]+d[j])
        if tar >= 0 and dp[tar]:
            print('YES')
            exit()

    for j in range(i):
        if d[i]+d[j]<w:
            dp[d[i]+d[j]] = True 

print('NO')
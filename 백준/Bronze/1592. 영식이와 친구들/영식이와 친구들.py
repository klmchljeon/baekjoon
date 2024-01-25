n,m,l = map(int,input().split())
idx = 0
cnt = [0]*n
ans = -1
while max(cnt) < m:
    if cnt[idx]%2 == 0:
        idx = (idx+n-l)%n
        
    else:
        idx = (idx+l)%n

    cnt[idx] += 1
    ans += 1


print(ans)
#폭탄 피하기
mod = 1000000007
max_ = 2*10**6

fact = [1]*(max_+1)
for i in range(2,max_+1):
    fact[i] = (fact[i-1]*i)%mod

inv = [1]*(max_+1)
for i in range(2,max_+1):
    inv[i] = (inv[mod%i]*(mod-mod//i))%mod

finv = [1]*(max_+1)
for i in range(2,max_+1):
    finv[i] = (finv[i-1]*inv[i])%mod

n,m,k = map(int,input().split())
loc = []
for i in range(k):
    x,y = map(int,input().split())
    loc.append((x,y))

loc.sort()

ans = 0
for i in range(1<<k):
    tmp = []
    for j in range(k):
        if i&(1<<j):
            tmp.append(loc[j])

    st = (0,0)
    res = 1
    for x,y in tmp:
        if st[1] > y:
            res = 0
            break

        a = x-st[0]
        b = y-st[1]
        
        res *= (fact[a+b]*finv[a]*finv[b])%mod
        st = (x,y)

    a = n-st[0]
    b = m-st[1]
    res *= (fact[a+b]*finv[a]*finv[b])%mod

    if len(tmp)&1:
        ans -= res
    else:
        ans += res
    
print(ans%mod)
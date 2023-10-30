mod = 1000000007

def fpow(C,n):
    if n == 1:
        return C

    x = fpow(C,n//2)
    if n&1:
        return x*x*C%mod
    else:
        return x*x%mod

a,b = map(int,input().split())

if a==1:
    print(b%mod)
else:
    m = fpow((a-1),mod-2)

    tmp = (fpow(a,b)-1)*m%mod
    print(tmp)
#이항 계수 3

n,k = map(int,input().split())
mod = 1000000007

def fact(n):
    result = 1
    for i in range(2,n+1):
        result = (result*i)%mod
    return result

def fpow(C,k):
    if k==1:
        return C

    x = fpow(C,k//2)
    if k%2 == 0:
        return (x*x)%mod
    else:
        return (x*x*C)%mod

up = fact(n)
down = (fact(n-k)*fact(k))%mod

print((up%mod * fpow(down,mod-2)%mod)%mod)
#A
mod = 1000000007

def fpow(c,n,p):
    if n==1:
        return c%p
    
    x = fpow(c,n//2,p)
    if n&1:
        return (x*x*c)%p
    else:
        return (x*x)%p

a = int(input())
x = int(input())
print(fpow(a,x,mod))
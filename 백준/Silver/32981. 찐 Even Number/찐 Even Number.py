import sys
input = sys.stdin.readline
mod = int(1e9)+7

def fpow(c,n):
    if n == 1:
        return c

    x = fpow(c,n//2)
    if n%2:
        return (x*x*c)%mod
    else:
        return (x*x)%mod

q = int(input())
for _ in range(q):
    n = int(input())
    if n == 1:
        print(5)
    else:
        print(4*fpow(5,n-1)%mod)
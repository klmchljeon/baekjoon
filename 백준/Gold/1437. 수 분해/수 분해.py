mod = 10007

n = int(input())
res = 1
while n > 4:
    res = (res*3)%mod
    n -= 3

print((res*n)%mod)
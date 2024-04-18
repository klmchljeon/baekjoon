mod = 987654321

n = int(input())
sieve = [True]*(n+1)
for i in range(2,n+1):
    if not sieve[i]: continue
    for j in range(i+i,n+1,i):
        sieve[j] = False

prime = [i for i in range(2,n+1) if sieve[i]]
res = 1
for i in prime:
    tmp = i
    while tmp*i <= n:
        tmp = (tmp*i)%mod

    res = (res*tmp)%mod

print(res)
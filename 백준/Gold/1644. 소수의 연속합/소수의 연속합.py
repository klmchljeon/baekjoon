#소수의 연속합

import math

n = int(input()); m = math.floor(math.sqrt(n))
sieve = [True]*(n+1); sieve[0] = sieve[1] = False
for i in range(2,m+1):
    if sieve[i]:
        for j in range(i+i,n+1,i):
            sieve[j] = False

prime = [i for i in range(2,n+1) if sieve[i]]

p = len(prime)
count = 0
for i in range(p):
    s = 0
    for j in range(i,p):
        s += prime[j]

        if s == n:
            count += 1
            break

        elif s > n:
            break
print(count)
import sys
input = sys.stdin.readline
max_ = 1299709

sieve = [True]*(max_+1)
for i in range(2,max_+1):
    if not sieve[i]: continue

    for j in range(i+i,max_+1,i):
        sieve[j] = False

prime = [i for i in range(2,max_+1) if sieve[i]]

t = int(input())
for case in range(t):
    k = int(input())

    s,e = -1,len(prime)
    while s+1<e:
        mid = (s+e)//2

        if prime[mid] <= k:
            s = mid

        else:
            e = mid

    if s == -1:
        print(0)
        continue

    if prime[s] == k:
        print(0)
    else:
        print(prime[e]-prime[s])
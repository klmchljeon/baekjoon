max_ = 10**7
sieve = [True]*(max_+1)
for i in range(2,max_+1):
    if sieve[i]:
        for j in range(2*i,max_+1,i):
            sieve[j] = False

prime = [i for i in range(2,max_+1) if sieve[i]]

a,b = map(int,input().split())
res = 0
for i in prime:
    num = i**2
    while num <= b:
        if a <= num:
            res += 1

        num *= i

print(res)
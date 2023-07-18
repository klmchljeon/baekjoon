#가짜소수
def fpow(C,n):
    if n == 1:
        return C

    x = fpow(C,n//2)
    if n&1:
        return (x*x*C)%p
    else:
        return (x*x)%p

tmp = int(1000000000**0.5)+1
sieve = [True]*(tmp+1)
for i in range(2,tmp+1):
    if sieve[i]:
        for j in range(i+i,tmp+1,i):
            sieve[j] = False

prime = [i for i in range(2,tmp+1) if sieve[i]]

while True:
    p,a = map(int,input().split())
    if p == 0: break

    flag = True
    for i in prime:
        if i >= p: break

        if p%i == 0:
            flag = False
            break

    if flag:
        print('no')
        continue

    if fpow(a,p) == a:
        print('yes')
    else:
        print('no')
#골드바흐의 추측
import sys
input = sys.stdin.readline
m = 1000001

sieve = [True]*(m+1)
for i in range(3,m+1,2):
    if sieve[i]:
        for j in range(i+i,m+1,i):
            sieve[j] = False

prime = [i for i in range(3,m//2,2) if sieve[i]]

while True:
    n = int(input())
    if not n: break

    for i in prime:
        if sieve[n-i]:
            print(f'{n} = {i} + {n-i}')
            break
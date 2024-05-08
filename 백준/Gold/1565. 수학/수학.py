from math import *

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

p = lcm(*a)
q = gcd(*b)

if q%p != 0:
    print(0)
    exit()

k = q//p
cnt = 0
for i in range(1,int(k**0.5)+1):
    if k%i == 0:
        cnt += 2
        if i == k//i:
            cnt -= 1

print(cnt)
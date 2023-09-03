import sys
from math import gcd
input = sys.stdin.readline

n = int(input())

d = []
prev = int(input())
for i in range(n-1):
    tmp = int(input())
    d.append(tmp-prev)
    prev = tmp

g = gcd(*d)
res = 0
for i in d:
    res += i//g - 1

print(res)
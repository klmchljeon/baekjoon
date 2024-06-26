import sys
from math import gcd

d = sys.stdin.readlines()
lst = []
for i in d:
    lst.extend(list(map(int,i.split())))

n = len(lst)

res = 1
for i in range(n-1):
    for j in range(i+1,n):
        res = max(res, gcd(lst[i],lst[j]))

print(res)
import sys
from functools import cmp_to_key
input = sys.stdin.readline

def f(a,b):
    p = a[0]*b[1]
    q = b[0]*a[1]

    if p != q:
        return (p>q) - (p<q)
    else:
        return (a[2]>b[2]) - (a[2]>b[2])

n = int(input())
lst = []
for i in range(n):
    x,y,v = map(int,input().split())
    lst.append((x**2+y**2,v**2,i+1))

lst.sort(key = cmp_to_key(f))
for i in lst:
    print(i[2])
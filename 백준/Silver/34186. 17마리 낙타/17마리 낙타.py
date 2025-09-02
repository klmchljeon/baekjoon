import sys
from math import gcd,lcm
input = sys.stdin.readline

t = int(input())
for case in range(t):
    n,a,b,c = map(int,input().split())

    l = lcm(a,b,c)
    up = l//a + l//b + l//c

    if up > l: 
        print(-1)
        continue

    if n%up == 0:
        tmp = n//up
        print(l*tmp - n)
    else:
        print(-1)
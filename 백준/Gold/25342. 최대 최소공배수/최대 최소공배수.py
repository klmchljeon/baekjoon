from math import lcm

t = int(input())
for case in range(t):
    n = int(input())

    if n%2 == 0:
        a = lcm(n,n-1,n-3)
        b = lcm(n-1,n-2,n-3)
        print(max(a,b))

    else:
        a = lcm(n,n-1,n-2)
        print(a)
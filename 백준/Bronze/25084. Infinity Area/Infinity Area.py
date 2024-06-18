import math
pi = math.pi

t = int(input())
for case in range(t):
    r,a,b = map(int,input().split())
    res = 0
    di = 1
    while r:
        res += r**2
        if di:
            r *= a
        else:
            r //= b

        di ^= 1

    print(f'Case #{case+1}: {res*pi}')
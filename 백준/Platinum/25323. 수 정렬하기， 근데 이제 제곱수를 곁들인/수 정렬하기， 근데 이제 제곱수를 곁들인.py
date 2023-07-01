from math import gcd

def check(num):
    low,high = -1,2**32
    while low + 1 < high:
        mid = (low + high)//2

        if mid**2 >= num:
            high = mid

        else:
            low = mid

    return high**2 != num

n = int(input())
a = list(map(int,input().split()))

b = sorted(a)

for i in range(n):
    if a[i]==b[i]: continue

    g = gcd(a[i],b[i])
    a[i] //= g
    b[i] //= g

    if check(a[i]) or check(b[i]):
        print('NO')
        break

else:
    print('YES')
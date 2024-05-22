import math

n = int(input())
a = list(map(int,input().split()))

b = [a[i+1]-a[i] for i in range(n-1)]
res = math.gcd(*b)
print(res)
import math

a,b,h = map(int,input().split())
h2 = h*a/(b-a)

f = lambda p,q:p**2 + q**2
print((f(h2+h,b)-f(h2,a))*math.pi)
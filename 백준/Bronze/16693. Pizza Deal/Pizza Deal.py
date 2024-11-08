import math

a,p1 = map(int,input().split())
r,p2 = map(int,input().split())

b = r**2 * math.pi

if a*p2 > b*p1:
    print('Slice of pizza')
else:
    print('Whole pizza')
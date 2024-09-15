from math import gcd

a,b = map(int,input().split())
g = gcd(a,b)

lst = []
for i in range(1,int(g**0.5)+1):
    if g%i == 0:
        lst.append(i)
        if i**2 != g:
            lst.append(g//i)

for i in lst:
    print(i,a//i,b//i)
n = int(input())
lst = list(map(float,input().split()))
while lst and lst[0]==0:
    lst.pop(0)
    n -= 1

if lst[0] < 0:
    for i in range(n+1):
        lst[i] = -lst[i]

k = int(input())

s,e = -33,0
for _ in range(60):
    mid = (s+e)/2

    tmp = lst[0]
    p = mid**2
    for i in range(n):
        tmp = tmp*p + lst[i+1]

    if tmp > 0:
        s = mid

    else:
        e = mid

a,b = s,-s
dist = (b-a)/k

res = 0
e = a+dist/2
for i in range(k//2):
    tmp = lst[0]
    p = e**2
    for i in range(n):
        tmp = tmp*p + lst[i+1]

    res += tmp
    e += dist

print(-res*dist*2)
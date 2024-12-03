a,b = map(int,input().split())
if b < 0:
    b = -b
    m = -1
else:
    m = 1

q,r = divmod(a,b)
print(m*q)
print(r)
a,b = map(int,input().split())
p = -a - int((a**2-b)**0.5)
q = -a + int((a**2-b)**0.5)
if p == q:
    print(p)
else:
    print(p,q)
x,y,d,t = map(int,input().split())
if d <= t:
    print((x**2 + y**2)**0.5)
    exit()

dist = x**2 + y**2
if dist < d**2:
    a = dist**0.5
    b = 2*t
    c = (d - dist**0.5) + t
    print(min(a,b,c))
    exit()

cnt = dist**0.5 // d
a = (cnt+1)*t
b = (dist**0.5 - d*cnt) + cnt*t
print(min(a,b))
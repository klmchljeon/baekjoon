n = int(input())
d,m = 100,0
prev = 100
t1,t2 = 0,int(1e9)
for i in range(n):
    a = int(input())
    if a > prev:
        t1 = max(t1,a)
        
        if t2 != int(1e9):
            d = m/t2
            t2 = int(1e9)
            m = 0

    elif a < prev:
        t2 = min(t2,a)
        
        if t1 != 0:
            m = d*t1
            t1 = 0
            d = 0

    prev = a

if t2 != int(1e9):
    d = m/t2

print(d)
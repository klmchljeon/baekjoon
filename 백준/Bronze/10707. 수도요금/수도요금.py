#수도요금
a,b,c,d,p = [int(input()) for _ in range(5)]

x = p*a
y = b
if p >= c:
    y += (p-c)*d

print(min(x,y))
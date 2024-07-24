n = int(input())
a,pa,b,pb = map(int,input().split())


m = 0
res = [0,0]

x = n // pa
while x >= 0:
    y = (n-pa*x) // pb

    if m < a*x + b*y:
        m = a*x + b*y
        res = [x,y]

    x -= 1

print(*res)
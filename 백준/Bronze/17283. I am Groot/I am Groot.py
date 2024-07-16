l = int(input())
r = int(input())

res = 0
p = 1
while True:
    l = (l*r)//100
    p *= 2

    if l <= 5:
        break
    
    res += l*p

print(res)
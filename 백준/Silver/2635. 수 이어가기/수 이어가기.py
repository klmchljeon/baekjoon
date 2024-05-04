def p(a,b):
    d = [a,b]
    while True:
        tmp = d[-2] - d[-1]
        if tmp >= 0:
            d.append(tmp)
        else:
            return d

n = int(input())

res = 0
lst = None
for m in range(1,n+1):
    d = p(n,m)
    if res < len(d):
        res = len(d)
        lst = d 

print(res)
print(*lst)
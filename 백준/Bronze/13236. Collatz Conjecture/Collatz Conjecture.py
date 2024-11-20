n = int(input())
res = [n]
while res[-1] != 1:
    m = res[-1]
    if m%2 == 0:
        res.append(m//2)
    else:
        res.append(3*m+1)

print(*res)
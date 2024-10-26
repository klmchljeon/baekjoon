n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

res = []
sa = 0
sb = 0
for num in range(100,0,-1):
    ia = sa
    ib = sb
    while ia < n and ib < m:
        if a[ia] == num and b[ib] == num:
            res.append(num)
            ia += 1
            ib += 1
            sa = ia
            sb = ib

        elif a[ia] == num:
            ib += 1

        elif b[ib] == num:
            ia += 1

        else:
            ia += 1
            ib += 1

print(len(res))
print(*res)
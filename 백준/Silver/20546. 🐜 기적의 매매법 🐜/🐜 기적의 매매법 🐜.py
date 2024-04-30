num = int(input())
d = list(map(int,input().split()))

a = [num,0]
b = [num,0]
lcnt = 0
hcnt = 0
prev = d[0]
for i in d:
    if prev == i:
        lcnt = 0
        hcnt = 0 
    elif prev < i:
        lcnt = 0
        hcnt += 1
    else:
        lcnt += 1
        hcnt = 0

    prev = i

    tmp = a[0]//i
    a[0] -= tmp*i
    a[1] += tmp

    if hcnt >= 3:
        b[0] += b[1]*i
        b[1] = 0

    if lcnt >= 3:
        tmp = b[0]//i
        b[0] -= tmp*i
        b[1] += tmp

resa = a[0] + a[1]*d[-1]
resb = b[0] + b[1]*d[-1]

if resa > resb:
    print('BNP')
elif resa == resb:
    print('SAMESAME')
else:
    print('TIMING')
y,m,d = map(int,input().split('-'))
n = int(input())

d += n
n,d = divmod(d,30)

m += n
n,m = divmod(m,12)

y += n

if d <= 0:
    m -= 1
    d += 30

if m <= 0:
    y -= 1
    m += 12

print(f'{y}-{m:02}-{d:02}')
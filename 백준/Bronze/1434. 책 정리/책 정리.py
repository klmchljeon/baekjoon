n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

idx = 0
i = 0
while i < m:
    if a[idx] >= b[i]:
        a[idx] -= b[i]
        i += 1
    else:
        idx += 1

print(sum(a))
#수열 03:11
n = int(input())
d = list(map(int,input().split()))

res = 0

lis = 0
prev = d[0]
for i in d:
    if prev <= i:
        lis += 1

    else:
        lis = 1

    prev = i

    res = max(res,lis)

lds = 0
prev = d[0]
for i in d:
    if prev >= i:
        lds += 1

    else:
        lds = 1

    prev = i

    res = max(res,lds)

print(res)
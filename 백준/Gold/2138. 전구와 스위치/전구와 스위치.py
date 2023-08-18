#전구와 스위치
max_ = int(1e6)

n = int(input())
a = list(map(int,input()))
b = list(map(int,input()))

res = max_

t1 = a[:]
cnt = 1
t1[0] ^= 1
t1[1] ^= 1
for i in range(1,n-1):
    if t1[i-1] != b[i-1]:
        for j in (i-1,i,i+1):
            t1[j] ^= 1

        cnt += 1

if t1[n-2] != b[n-2]:
    t1[n-2] ^= 1
    t1[n-1] ^= 1

    cnt += 1

if t1[n-1] == b[n-1]:
    res = min(res,cnt)

t2 = a[:]
cnt = 0
for i in range(1,n-1):
    if t2[i-1] != b[i-1]:
        for j in (i-1,i,i+1):
            t2[j] ^= 1

        cnt += 1

if t2[n-2] != b[n-2]:
    t2[n-2] ^= 1
    t2[n-1] ^= 1

    cnt += 1

if t2[n-1] == b[n-1]:
    res = min(res,cnt)

print(res if res!=max_ else -1)
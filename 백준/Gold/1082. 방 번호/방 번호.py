n = int(input())
p = list(map(int,input().split()))
m = int(input())
tm = m

val = 51
idx = -1
for i in range(1,n):
    if val >= p[i] and p[i] <= m:
        val = p[i]
        idx = i

if idx == -1:
    print(0)
    exit()

if val <= p[0]:
    tmp = [idx]*(m//val)
    m -= val*(m//val)
    ti = 0
    for i in range(idx+1,n)[::-1]:
        while m >= (p[i]-p[idx]) and ti < len(tmp):
            m -= (p[i]-p[idx])
            tmp[ti] = i
            ti += 1

    print(*sorted(tmp)[::-1],sep='')
    exit()

tmp1 = [0]*((m-p[idx])//p[0]) + [idx]
m -= p[0]*((m-p[idx])//p[0]) + p[idx]
ti = 0
for i in range(1,n)[::-1]:
    while m >= (p[i]-p[0]) and ti < len(tmp1):
        m -= (p[i]-p[0])
        tmp1[ti] = i
        ti += 1

m = tm
tmp2 = [idx] + [0]*((m-p[idx])//p[0])
m -= p[idx] + p[0]*((m-p[idx])//p[0])
ti = 0
for i in range(idx+1,n)[::-1]:
    if m >= (p[i]-p[idx]):
        m -= (p[i]-p[idx])
        tmp2[ti] = i
        ti += 1
        break

for i in range(1,n)[::-1]:
    while m >= (p[i]-p[0]) and ti < len(tmp2):
        m -= (p[i]-p[0])
        tmp2[ti] = i
        ti += 1

print(*max(sorted(tmp1)[::-1],sorted(tmp2)[::-1]),sep='')
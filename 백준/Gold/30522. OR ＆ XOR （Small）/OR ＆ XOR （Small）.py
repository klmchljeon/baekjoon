m = 1<<10

n,p = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

cnta = [0]*m
for i in a:
    cnta[i] += 1

cntb = [0]*m
for i in b:
    cntb[i] += 1

lst = []
for i in range(m):
    for j in range(i,m):
        lst.append(((i|j)-(i^j),i,j))

lst.sort(reverse = True)

res = 0
for v,i,j in lst:
    cnt = cnta[i]*cntb[j]
    if p > cnt:
        res += cnt*(i|j)
        p -= cnt
    else:
        res += p*(i|j) + (cnt-p)*(i^j)
        p = 0

    if i==j: continue

    cnt = cnta[j]*cntb[i]
    if p > cnt:
        res += cnt*(i|j)
        p -= cnt
    else:
        res += p*(i|j) + (cnt-p)*(i^j)
        p = 0

print(res)
#백설공주와 난쟁이
def find(half):
    for i in range(1,c+1):
        if lst[i] > half:
            return f'yes {i}'
        
    return 'no'

n,c = map(int,input().split())
d = (0,) + tuple(map(int,input().split()))
sqn = int(n**0.5)+1
sqc = int(c**0.5)+1

m = int(input())
query = []
for i in range(m):
    a,b = map(int,input().split())
    query.append((i,a,b))

k = lambda x:(x[1]//sqn,x[2])
query.sort(key = k)

lst = [0]*(c+1)
res = [0]*m

idx,pa,pb = query[0]
flag = (pb-pa+1)//2
for i in range(pa,pb+1):
    lst[d[i]] += 1

res[idx] = find(flag)

for i in range(1,m):
    idx,a,b = query[i]
    flag = (b-a+1)//2

    while pa < a:
        lst[d[pa]] -= 1
        pa += 1

    while a < pa:
        pa -= 1
        lst[d[pa]] += 1

    while pb < b:
        pb += 1
        lst[d[pb]] += 1

    while b < pb:
        lst[d[pb]] -= 1
        pb -= 1
        
    res[idx] = find(flag)

print(*res,sep='\n')
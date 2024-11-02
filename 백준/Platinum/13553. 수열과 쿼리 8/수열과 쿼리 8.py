#수열과 쿼리 8
import sys
input = sys.stdin.readline
t = 100000

def cal(idx):
    idx = min(idx,t)
    res = 0
    while idx > 0:
        res += tree[idx]
        idx -= idx & -idx
    
    return res

def update(idx,val):
    while idx <= t:
        tree[idx] += val
        idx += idx & -idx

    return 

n,k = map(int,input().split())
sqn = int(n**0.5) + 1

lst = [0]*(t+1)
tree = [0]*(t+1)

d = (0,) + tuple(map(int,input().split()))

m = int(input())
query = []
for i in range(m):
    a,b = map(int,input().split())
    query.append((i,a,b))

f = lambda x:(x[1]//sqn,x[2])
query.sort(key = f)

res = [0]*m

tmp = 0
idx,pa,pb = query[0]
for i in range(pa,pb+1):
    tmp += cal(d[i]+k) - cal(d[i]-k-1)
    lst[d[i]] += 1
    update(d[i],1)

res[idx] = tmp

for i in range(1,m):
    idx,a,b = query[i]

    while pa < a:
        lst[d[pa]] -= 1
        update(d[pa],-1)
        tmp -= cal(d[pa]+k) - cal(d[pa]-k-1)
        pa += 1

    while a < pa:
        pa -= 1
        tmp += cal(d[pa]+k) - cal(d[pa]-k-1)
        lst[d[pa]] += 1
        update(d[pa],1)

    while pb < b:
        pb += 1
        tmp += cal(d[pb]+k) - cal(d[pb]-k-1)
        lst[d[pb]] += 1
        update(d[pb],1)

    while b < pb:
        lst[d[pb]] -= 1
        update(d[pb],-1)
        tmp -= cal(d[pb]+k) - cal(d[pb]-k-1)
        pb -= 1

    res[idx] = tmp

print(*res,sep='\n')
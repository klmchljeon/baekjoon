#수열과 쿼리 18
import sys
input = sys.stdin.readline

def find(num,i):
    s,e = -1,len(bucket[i])
    while s+1<e:
        mid = (s+e)//2

        if bucket[i][mid] <= num:
            s = mid

        else:
            e = mid

    return s

def update(i,v):
    i-=1
    bki = i//sqn
    bucket[bki].insert(find(v,bki)+1,v)
    bucket[bki].pop(find(d[i],bki))
    d[i] = v
    return

def cal(l,r,k):
    l-=1
    r-=1
    res = 0
    while l%sqn and l<=r:
        if d[l] > k:
            res += 1

        l += 1

    while (r+1)%sqn and l<=r:
        if d[r] > k:
            res += 1
        
        r -= 1

    while l<=r:
        bki = l//sqn
        res += len(bucket[bki]) - (find(k,bki)+1)

        l += sqn

    return res

n = int(input())
d = list(map(int,input().split()))

sqn = int(n**0.5) + 1

bucket = [[] for _ in range(sqn)]
for i in range(n):
    bucket[i//sqn].append(d[i])

for i in range(sqn):
    bucket[i].sort()

m = int(input())
for query in range(m):
    q,*order = map(int,input().split())
    if q==1:
        print(cal(*order))
    else:
        update(*order)
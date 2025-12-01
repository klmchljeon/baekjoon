from heapq import *
max_ = int(2e18)

#횟수가 num 이하일 때 모두가 find(num) 이상의 체력을 가짐
def find(num,k):
    s,e = k,max_
    scnt = 0
    while s+1<e:
        mid = (s+e)//2

        cnt = 0
        for i in range(n):
            tmp = max(0, mid - a[i])
            cnt += tmp//b[i] + bool(tmp%b[i])

        if cnt <= num:
            s = mid
            scnt = cnt

        else:
            e = mid

    return scnt,s

n,x = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
k = min(a)

cnt,s = find(x,k)
for i in range(n):
    tmp = max(0,s-a[i])
    c = tmp//b[i] + bool(tmp%b[i])
    a[i] += c*b[i]

heap = []
for i in range(n):
    heappush(heap,(a[i],i))
    
for _ in range(cnt,x):
    h,idx = heappop(heap)
    h += b[idx]
    heappush(heap,(h,idx))

res = [0]*n
for h,idx in heap:
    res[idx] = h

print(*res)
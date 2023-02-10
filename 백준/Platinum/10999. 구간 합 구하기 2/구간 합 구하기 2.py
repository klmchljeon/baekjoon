#구간 합 구하기2
import sys
input = sys.stdin.readline

def update(l,r,val):
    while l%sqn and l<=r:
        lst[l] += val
        bucket[l//sqn] += val
        l += 1

    while (r+1)%sqn and l<=r:
        lst[r] += val
        bucket[r//sqn] += val
        r -= 1

    while l<=r:
        e = min(n+1,l+sqn)
        bucket[l//sqn] += (e-l)*val
        lazy[l//sqn] += val
        l += sqn

    return 

def cal(l,r):
    res = 0

    while l%sqn and l<=r:
        res += lst[l] + lazy[l//sqn]
        l += 1

    while (r+1)%sqn and l<=r:
        res += lst[r] + lazy[r//sqn]
        r -= 1

    while l<=r:
        res += bucket[l//sqn]
        l += sqn

    return res
    
n,m,k = map(int,input().split())
lst = [0]*(n+1)
sqn = int(n**0.5)+2

bucket = [0]*sqn
lazy = [0]*sqn

for i in range(1,n+1):
    num = int(input())
    lst[i] = num
    bucket[i//sqn] += num

for query in range(m+k):
    q,*order = map(int,input().split())
    if q == 1:
        update(*order)
    else:
        print(cal(*order))
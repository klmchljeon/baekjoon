#수 찾기
n = int(input())
d = list(map(int,input().split()))
d.sort()

m = int(input())
lst = list(map(int,input().split()))

for i in range(m):
    lo,hi = 0,n
    while lo+1 < hi:
        mid = (lo+hi)//2

        if d[mid] <= lst[i]:
            lo = mid

        else:
            hi = mid

    print(1 if d[lo] == lst[i] else 0)
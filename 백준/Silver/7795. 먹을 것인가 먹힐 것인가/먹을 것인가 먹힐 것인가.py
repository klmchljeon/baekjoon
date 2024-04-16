def find(num):
    s,e = -1,n
    while s+1<e:
        mid = (s+e)//2

        if a[mid] > num:
            e = mid
        else:
            s = mid

    return n-e

t = int(input())
for case in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    a.sort()
    print(sum(map(find,b)))
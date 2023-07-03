#홍준이의 행렬
max_ = int(1e9)

def find(num,x):
    lo,hi = -1,n
    while lo+1<hi:
        mid = (lo+hi)//2

        if b[mid]*x <= num:
            lo = mid
        
        else:
            hi = mid

    return lo+1

def check(num):
    cnt = 0
    for i in a:
        cnt += find(num,i)

    return cnt >= k

n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

b.sort()

s,e = 0,max_**2
while s+1<e:
    m = (s+e)//2

    if check(m):
        e = m

    else:
        s = m

print(e)
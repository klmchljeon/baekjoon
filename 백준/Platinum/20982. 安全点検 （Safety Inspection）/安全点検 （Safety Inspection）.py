def check(num):
    tmp = b[:]
    r = 0
    cnt = 0
    while tmp:
        if r >= tmp[-1]:
            r -= tmp[-1]
            tmp.pop()
            continue

        tmp[-1] -= r
        r = 0

        w = num - a[len(tmp)-1]
        if w <= 0: return False

        cnt += tmp[-1]//w
        
        tmp[-1] %= w
        if tmp[-1]:
            cnt += 1
            r = w - tmp[-1]

        tmp.pop()

    return cnt <= k

n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

s,e = 0,sum(b)+a[-1]
while s+1<e:
    mid = (s+e)//2

    if check(mid):
        e = mid

    else:
        s = mid

print(e)
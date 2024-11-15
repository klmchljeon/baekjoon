def check(num):
    cnt = 0
    for i in lst:
        if i <= num: continue

        p = i-num
        cnt += p//k + bool(p%k)

    return cnt <= num

n = int(input())
lst = list(map(int,input().split()))
k = int(input())
k -= 1
if k == 0:
    print(max(lst))
    exit()

s,e = 0,int(1e9)
while s+1<e:
    mid = (s+e)//2

    if check(mid):
        e = mid

    else:
        s = mid

print(e)
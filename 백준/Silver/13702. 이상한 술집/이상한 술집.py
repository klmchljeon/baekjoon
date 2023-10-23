def check(num):
    cnt = 0
    for i in d:
        cnt += i//num

    return cnt >= k

n,k = map(int,input().split())
d = [int(input()) for _ in range(n)]

s,e = 0,2**31
while s+1<e:
    mid = (s+e)//2

    if check(mid):
        s = mid
    else: 
        e = mid

print(s)
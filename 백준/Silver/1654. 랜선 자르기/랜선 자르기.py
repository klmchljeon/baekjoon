import sys
input = sys.stdin.readline

def check(num):
    cnt = 0
    for i in d:
        cnt += i//num

    return cnt >= n

k,n = map(int,input().split())
d = [int(input()) for _ in range(k)]

s,e = -1,2**31
while s+1<e:
    mid = (s+e)//2

    if check(mid):
        s = mid

    else:
        e = mid

print(s)
import sys
input = sys.stdin.readline

def check(num):
    cnt = 1
    tmp = 0
    for i in range(n):
        if tmp + lst[i] <= num:
            tmp += lst[i]
        else:
            tmp = lst[i]
            cnt += 1

    return cnt <= m

n,m = map(int,input().split())
lst = [int(input()) for _ in range(n)]

s,e = max(lst)-1,int(1e9)
while s+1<e:
    mid = (s+e)//2

    if check(mid):
        e = mid

    else:
        s = mid

print(e)
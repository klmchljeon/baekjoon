import sys
input = sys.stdin.readline

def check(num):
    cnt = 0
    for i in lst:
        cnt += i//num

    return cnt >= c

n,c = map(int,input().split())
lst = [int(input()) for _ in range(n)]

s,e = 0,int(1e18)
while s+1<e:
    mid = (s+e)//2

    if check(mid):
        s = mid

    else:
        e = mid

print(sum(lst) - s*c)
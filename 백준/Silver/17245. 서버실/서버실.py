import sys
input = sys.stdin.readline

def check(num):
    c = 0
    for i in d:
        c += min(i,num)

    return half <= c

n = int(input())
d = []
for i in range(n):
    tmp = list(map(int,input().split()))
    d.extend(tmp)

sum_ = sum(d)
half = sum_//2 + sum_%2

s,e = -1,int(1e8)
while s+1<e:
    mid = (s+e)//2

    if check(mid):
        e = mid

    else:
        s = mid

print(e)
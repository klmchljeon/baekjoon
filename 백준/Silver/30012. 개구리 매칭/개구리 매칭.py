import sys
input = sys.stdin.readline
max_ = int(1e18)

s,n = map(int,input().split())
d = list(map(int,input().split()))
k,l = map(int,input().split())

res = [max_,0]
for i in range(n):
    dis = abs(s-d[i])

    tmp = None
    if dis >= 2*k:
        tmp = (dis-2*k)*l
    else:
        tmp = 2*k-dis

    if res[0] > tmp:
        res = [tmp,i+1]

print(*res)
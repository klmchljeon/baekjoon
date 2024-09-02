def cal(num):
    if b - (num-1)*k <= 0:
        num = b//k + 1

    dist = num*b - k*num*(num-1)//2
    return dist

def check(num):
    return cal(num) >= a

a,b = map(int,input().split())
c,d = map(int,input().split())
k = int(input())

s,e = -1,int(1e18)
while s+1<e:
    mid = (s+e)//2

    if check(mid):
        e = mid

    else:
        s = mid

res = a+c > e*d
print(e if res else -1)
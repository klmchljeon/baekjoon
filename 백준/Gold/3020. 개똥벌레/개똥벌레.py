import sys
input = sys.stdin.readline

def find(lst,num):
    s,e = -1,len(lst)
    while s+1<e:
        mid = (s+e)//2

        if lst[mid] >= num:
            e = mid
        else:
            s = mid

    return e

n,h = map(int,input().split())
tmp = [int(input()) for _ in range(n)]

a = sorted(tmp[::2])
b = sorted(tmp[1::2])

res = n
cnt = 0
for i in range(1,h+1):
    p = n - find(a,i) - find(b,h-i+1)
    if res > p:
        res = p
        cnt = 1
    elif res == p:
        cnt += 1

print(res,cnt)
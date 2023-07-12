#랩실에서 잘자요
n,m = map(int,input().split())
d = list(map(int,input().split()))

lst = sorted(set(range(1,n+1))-set(d))

if not lst:
    print(0)
    exit()

res = 7
prev = lst[0]
for i in lst[1:]:
    res += min((i-prev)*2,7)
    prev = i

print(res)
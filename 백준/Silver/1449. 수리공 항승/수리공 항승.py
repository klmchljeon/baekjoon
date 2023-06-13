#수리공 항승
n,l = map(int,input().split())
d = list(map(int,input().split()))
d.sort()

cnt = 1
tmp = d[0]
for i in d:
    if i - tmp >= l:
        tmp = i
        cnt += 1

print(cnt)
n = int(input())
d = tuple(map(int,input().split()))

max_ = d[0]
cnt = 0
tmp = 0
for i in range(1,n):
    if max_ > d[i]:
        tmp += 1

    else:
        max_ = d[i]
        cnt = max(cnt,tmp)
        tmp = 0

cnt = max(cnt,tmp)
print(cnt)
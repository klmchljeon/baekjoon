#님 게임
n = int(input())
d = list(map(int,input().split()))
d.sort()

cnt = 0
for i in d:
    if i==1:
        cnt += 1

if cnt==n:
    print('cubelover' if cnt&1 else 'koosaga')
else:
    if cnt and not cnt&1:
        d[-1] = 1

    tmp = 0
    for i in d:
        tmp ^= i

    print('koosaga' if tmp else 'cubelover')
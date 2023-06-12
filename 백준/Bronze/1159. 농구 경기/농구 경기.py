#농구 경기
n = int(input())
d = [input() for _ in range(n)]
d.sort()

res = []

prev = d[0][0]
cnt = 0
for i in d:
    if i[0] == prev:
        cnt += 1

    else:
        if cnt >= 5:
            res.append(prev)

        cnt = 1

    prev = i[0]

if cnt >= 5:
    res.append(prev)

if res:
    print(*res,sep='')
else:
    print('PREDAJA')
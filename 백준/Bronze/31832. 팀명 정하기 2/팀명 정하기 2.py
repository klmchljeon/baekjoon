n = int(input())
lst = [input() for _ in range(n)]
for name in lst:
    if len(name) > 10: continue

    cnt = [0,0,0]
    for i in name:
        if 'a' <= i <= 'z':
            cnt[0] += 1

        elif 'A' <= i <= 'Z':
            cnt[1] += 1

        elif not ('0' <= i <= '9'):
            cnt[2] += 1

    flag1 = cnt[0] >= cnt[1]
    flag2 = sum(cnt) >= 1

    if flag1 and flag2:
        print(name)
        break

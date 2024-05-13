t = int(input())
for case in range(t):
    n,m = map(int,input().split())
    idx = n-1

    res = []
    while idx+1 > 0:
        if m >= idx:
            res.append(idx+1)
            m -= idx
            idx -= 1
        else:
            break

    else:
        print(*res)
        continue

    res += list(range(1,idx+1))
    if m == 0:
        res.append(idx+1)
    else:
        res.insert(-m,idx+1)

    print(*res)
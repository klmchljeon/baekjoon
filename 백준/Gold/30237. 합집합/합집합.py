max_ = 50

t = int(input())
for case in range(t):
    n = int(input())
    s = [0]*(max_+1)
    lst = []
    for _ in range(n):
        tmp = [0]*(max_+1)
        k,*d = map(int,input().split())
        for i in d:
            tmp[i] = 1
            s[i] = 1

        lst.append(tmp)

    res = 0
    for num in range(1,max_+1):
        if s[num] == 0: continue

        p = [0]*(max_+1)
        for i in range(n):
            if lst[i][num] == 1: continue
            for j in range(1,max_+1):
                p[j] |= lst[i][j]

        res = max(res,sum(p))

    print(res)
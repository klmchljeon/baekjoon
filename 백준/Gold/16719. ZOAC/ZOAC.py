st = input()
n = len(st)

p = [False]*n
for _ in range(n):
    min_ = chr(ord('Z') + 1)
    idx = -1
    for i in range(n):
        if p[i]: continue
        
        tmp = []
        for j in range(n):
            if p[j] or i==j:
                tmp.append(st[j])

        s = ''.join(tmp)
        if min_ > s:
            min_ = s
            idx = i

    print(min_)
    p[idx] = True
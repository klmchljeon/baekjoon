def bt():
    global s
    if len(s) == len(st):
        res.append(s)
        return
    
    for i in range(len(st)):
        if s+st[i] in visited: continue
        if i in idx: continue

        visited.add(s+st[i])
        idx.append(i)
        s += st[i]
        bt()
        idx.pop()
        s = s[:-1]

n = int(input())
for case in range(n):
    st = sorted(input())
    visited = set()
    s = ''
    idx = []
    res = []
    bt()

    print(*sorted(res),sep='\n')
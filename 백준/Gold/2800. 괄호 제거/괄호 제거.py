st = input()

idx = []
stack = []
for i in range(len(st)):
    if st[i] == '(':
        stack.append(i)
    elif st[i] == ')':
        idx.append((stack.pop(),i))

res = []
for i in range(1,1<<len(idx)):
    p = []
    for j in range(len(idx)):
        if i&(1<<j):
            p.append(j)

    lst = []
    for k in p:
        lst += idx[k]

    tmp = ''
    for j in range(len(st)):
        if not j in lst:
            tmp += st[j]

    res.append(tmp)

print(*sorted(set(res)), sep='\n')
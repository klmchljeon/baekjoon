alpha = [chr(i + ord('A')) for i in range(26)]
dic = dict(zip(alpha,range(26)))

def bt():
    if len(res) == l:
        print(''.join(res))
        exit()

    j = len(res)
    for k in range(26):
        flag = False
        for a in d[j][k]:
            flag |= visited[a]

        if flag: continue

        res.append(alpha[k])
        for a in d[j][k]:
            visited[a] = True

        bt()

        res.pop()
        for a in d[j][k]:
            visited[a] = False



n,l = map(int,input().split())
lst = []
for _ in range(n):
    st = input()
    lst.append(st)

d = []
for j in range(l):
    tmp = []

    for k in range(26):
        p = []

        for i in range(n):
            if lst[i][j] != alpha[k]:
                p.append(i)

        tmp.append(p)

    d.append(tmp)

visited = [False]*n
res = []

bt()
print('CALL FRIEND')
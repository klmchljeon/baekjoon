alpha = 'ATGC'
dic = dict(zip(alpha,range(4)))

st = input()
prefix = [[0] for _ in range(4)]
for a in range(4):
    s = 0
    for i in st:
        s += dic[i]==a
        prefix[a].append(s)

m = int(input())
for _ in range(m):
    s,e = map(int,input().split())
    d = []
    for a in range(4):
        cnt = prefix[a][e] - prefix[a][s-1]
        d.append((cnt,a))

    d.sort(key = lambda x:(-x[0],x[1]))
    res = [alpha[d[i][1]] for i in range(4)]
    print(''.join(res))
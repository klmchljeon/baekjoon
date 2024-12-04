st = list(map(int,input()))
n = len(st)

idx = [[],[]]
for i in range(n):
    idx[st[i]].append(i)

idx[0] = idx[0][:len(idx[0])//2]
idx[1] = idx[1][len(idx[1])//2:]

lst = []
for i in range(2):
    for j in range(len(idx[i])):
        lst.append((idx[i][j],i))

lst.sort()
res = []
for _,i in lst:
    res.append(i)

print(''.join(map(str,res)))
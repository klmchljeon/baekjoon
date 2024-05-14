n = int(input())
st = input()
lst = []
idx = 0
while idx < len(st):
    tmp = st[idx]
    idx += 1
    if idx < len(st) and st[idx] in ('0','+','-'):
        tmp += st[idx]
        idx += 1

    else:
        tmp += '0'

    lst.append(tmp)

res = []
for i in range(n):
    if lst[i] in ('C+','C0','C-'):
        res.append('B')

    elif lst[i] in ('B0','B-'):
        if i==0 or lst[i-1] in ('C+','C0','C-'):
            res.append('D')

        else:
            res.append('B')

    elif lst[i] in ('A-','B+'):
        if i==0 or lst[i-1] in ('B0','B-','C+','C0','C-'):
            res.append('P')

        else:
            res.append('D')

    elif lst[i] == 'A0':
        if i==0 or lst[i-1] in ('A-','B+','B0','B-','C+','C0','C-'):
            res.append('E')

        else:
            res.append('P')

    else:
        res.append('E')

print(''.join(res))
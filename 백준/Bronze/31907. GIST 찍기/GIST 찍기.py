st = '''G...
.I.T
..S.'''

lst = list(map(list,st.split('\n')))

n = int(input())
res = []
for i in range(3):
    tmp = [j*n for j in lst[i]]
    for j in range(n):
        res.append(tmp)

for i in res:
    print(''.join(i))
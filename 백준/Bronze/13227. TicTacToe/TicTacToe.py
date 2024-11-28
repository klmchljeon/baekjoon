d = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

st = input()+input()+input()
for a,b,c in d:
    p = st[a]+st[b]+st[c]
    if p in ('OOO','XXX'):
        print('YES')
        break
    
else:
    print('NO')
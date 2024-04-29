d = sorted([input() for _ in range(3)])
st = sorted('lkp')

for i in range(3):
    if d[i][0] != st[i]:
        print('PONIX')
        break

else:
    print('GLOBAL')
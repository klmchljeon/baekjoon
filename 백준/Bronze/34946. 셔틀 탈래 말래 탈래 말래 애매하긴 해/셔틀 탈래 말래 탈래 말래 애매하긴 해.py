a,b,c,d = map(int,input().split())
f1 = a+b <= d
f2 = c <= d

if f1 and f2:
    print('~.~')
elif f1:
    print('Shuttle')
elif f2:
    print('Walk')
else:
    print('T.T')
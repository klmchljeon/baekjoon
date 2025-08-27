n,m = map(int,input().split())
x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
if n == 1 or m == 1:
    if x1==x2 and y1==y2:
        print('YES')
    else:
        print('NO')

else:
    if (x2-x1)%2 == (y2-y1)%2:
        print('YES')
    else:
        print('NO')
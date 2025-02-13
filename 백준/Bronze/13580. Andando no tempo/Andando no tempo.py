a,b,c = sorted(map(int,input().split()))
if a==b or b==c or a+b==c:
    print('S')
else:
    print('N')